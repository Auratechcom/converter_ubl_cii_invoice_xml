# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import errno
import logging
import os
import subprocess
import sys
import tempfile
import traceback
try:
    from xml.etree import cElementTree as etree
except ImportError:
    from xml.etree import ElementTree as etree

from bots import botsinit
try:
    import bots.config_ublcii
except ImportError:
    from . import egg_install
    egg_install()

from . import start_logging, info, logger, error, fatalerror, __path__, __about__


STDOUT = STDERR = subprocess.PIPE
VERBOSE = DEBUG = False
VALIDATION_PATH = os.path.join(__path__[0], 'validation', 'eInvoicing-EN16931')


def popen(pargs):
    """Open a subprocess.
    return tuple: returncode:int, stdout:bytes, stderr:bytes|str"""
    try:
        proc = subprocess.Popen(pargs, stdout=STDOUT, stderr=STDERR)
        stdoutdata, stderrdata = proc.communicate()
        return proc.returncode, stdoutdata, stderrdata

    except Exception:
        err = traceback.format_exc()
        error(err)
        return 1, b'', err


def is_java_installed():
    """Look at java binary in system PATH
    return: boolean
    """
    for path in os.environ['PATH'].split(':'):
        for prog in os.listdir(path):
            if prog in ['java', 'java.exe']:
                return True
    return False


def saxon_transform(filename, xslt, outfile, **kwargs):
    """Apply a xlst transformation to a xml file thru java and Saxon-HE.jar library"""
    if not is_java_installed():
        error('java binary not found in system path !')
        fatalerror('Please install java first.')
    saxon_he_jar = os.path.join(__path__[0], 'java', 'Saxon-HE.jar')
    if not saxon_he_jar or not os.path.isfile(saxon_he_jar):
        error('Saxon-HE.jar not found, skiping.')
        return -1, None, None
    if not os.path.isfile(filename):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)
    pargs = [
        'java', '-cp', saxon_he_jar, 'net.sf.saxon.Transform',
        '-t', '-s:%s' % filename, '-xsl:%s' % xslt, '-o:%s' % outfile,
    ]
    return popen(pargs)


def build_validation_report(invoicetype, filename, outfile=None):
    """Generate invoice validation report"""
    if invoicetype not in ['ubl', 'cii']:
        raise Exception('Invalid invoice type: %s' % invoicetype)
    if not outfile:
        outfile = '%s.report.xml' % filename
    xslt = os.path.join(
        VALIDATION_PATH, invoicetype, 'xslt', 'EN16931-%s-validation.xslt' % invoicetype.upper())
    ret, out, err = saxon_transform(filename, xslt, outfile)
    if ret == 0:
        logger.debug("Invoice %s validation report created: '%s'", invoicetype.upper(), outfile)
        return outfile
    if isinstance(err, bytes):
        err = err.decode()
    if isinstance(out, bytes):
        out = out.decode()
    fatalerror("Error (%s) durring validation report creation:\n%s\n%s" % (ret, out, err))


def parse_validation_report(validation_report):
    """Parse errors in xml <svrl:schematron-output> files.
    :return boolean
    """
    if isinstance(validation_report, str):
        doc = etree.parse(validation_report)
    elif hasattr(validation_report, 'getroot'):
        doc = validation_report
    else:
        raise Exception('Invalid validation_report type.')
    namespaces = {'svrl': 'http://purl.oclc.org/dsdl/svrl'}
    active_patern = doc.find(".//svrl:active-pattern", namespaces)
    document = active_patern.attrib.get('document')
    filename = document.split('file:')[1]
    invoicetype = active_patern.attrib.get('id', '').split('-')[-2]

    fired_rules = doc.findall(".//svrl:fired-rule", namespaces)
    failed_asserts = doc.findall(".//svrl:failed-assert", namespaces)
    infos = '%4s fired rules' % (len(fired_rules) + len(failed_asserts))
    warnings_asserts = []
    fatal_asserts = []
    if failed_asserts:
        for elem in failed_asserts:
            flag = elem.attrib['flag'].strip()
            txt = ''
            for child in elem:
                txt += child.text
            err = '(%s) %s validation [%s]\n' % (flag, invoicetype, elem.attrib['id'])
            err += '%s error: %s\n' % (invoicetype, txt)
            err += 'test     : %s\nlocation : %s\n' % (elem.attrib['test'], elem.attrib['location'])
            if flag == 'warning':
                warnings_asserts.append(elem)
                logger.warning(err)
            elif flag == 'fatal':
                fatal_asserts.append(elem)
                error(err)
            else:
                error(err)
        # info('%s failed assertions' % len(failed_asserts))
        if warnings_asserts:
            logger.warning('%4s warning assertions', len(warnings_asserts))
        if fatal_asserts:
            error('%4s fatal assertions' % len(fatal_asserts))
            info(infos)
            error("Invalid %s invoice document: '%s'" % (invoicetype, os.path.basename(filename)))
            return False
    info(infos)
    info("Valid %s invoice document: '%s'" % (invoicetype, os.path.basename(filename)))
    return True


def start(route, prog, *args):
    """Start translation/validation of ubl/cii invoice"""

    start_logging()
    usage = """
%(prog)s v%(version)s

Usage: %(prog)s [options] input_%(intype)s.xml output_%(outtype)s.xml

    -R|--replace Replace output file if exist

    -r|--report  Build invoice validation report <filename>.report.xml

    -v|--validate
                 Do validation of input %(intype)s and output %(outtype)s translated.
                 (A valid installation of java is requiered.)

    --version    return version information and exit

    input:       Input %(intype)s file path to transtate
    output:      Output translated %(outtype)s file path

Author: %(author)s\
"""

    intype, outtype = prog.split('2')
    usage %= {
        'prog': prog,
        'intype': intype.upper(),
        'outtype': outtype.upper(),
        'version': __about__.__version__,
        'author': __about__.__author__,
    }

    infile = outfile = None
    replaceexisting = False
    do_validation = False
    build_report = False
    config_dir = 'config_ublcii'
    if not args:
        args = sys.argv[1:]
    for arg in args:
        if arg in ['-R', '--replace']:
            replaceexisting = True
        elif arg == '-D':
            globals()['DEBUG'] = True
            logger.setLevel(logging.DEBUG)
        elif arg == '--version':
            sys.stdout.write('%s %s%s' % (prog, __about__.__version__, os.linesep))
            return
        elif arg.startswith('-c'):
            config_dir = arg[2:]
        elif arg == '-V':
            globals()['VERBOSE'] = True
        elif arg in ['-r', '--report']:
            build_report = True
        elif arg in ['-v', '--validate']:
            do_validation = True
        elif arg in ['?', '/?', '-h', '--help'] or arg.startswith('-'):
            info(usage)
            return 0
        elif not infile:
            infile = arg
        elif not outfile:
            outfile = arg
        else:
            error(usage)
            return 4

    if not infile:
        error('No input file specified', usage)
        return 4

    infile = os.path.abspath(infile)
    if not os.path.isfile(infile):
        error("Invalid input file: '%s'" % infile)
        return 5
    info("Input %s file: '%s'" % (intype.upper(), os.path.basename(infile)))
    logger.debug("Input %s file: '%s'", intype.upper(), infile)

    # Input validation
    if do_validation or build_report:
        info("Validating input %s invoice '%s' ..." % (intype.upper(), infile))
        report = None if build_report else tempfile.mktemp()
        try:
            report = build_validation_report(intype, infile, report)
        except:
            error(traceback.format_exc(limit=0))
            return 6
        ret = int(not bool(report))
        if report and do_validation:
            is_valid = parse_validation_report(report)
            ret = int(not bool(is_valid))
        if not build_report:
            os.remove(report)
        if not outfile:
            return ret

    if not outfile:
        error('No output file path specified', usage)
        return 4
    outfile = os.path.abspath(outfile)
    if os.path.isfile(outfile) and not replaceexisting:
        error("Output file exist: '%s'\nUse -R or --replace to replace existing file" % outfile)
        return 5
    if not os.path.isdir(os.path.dirname(outfile)):
        error('Output path is not a valid directory: %s' % outfile)
        return 5

    os.environ["BOTS_FILE_IN"] = infile
    os.environ["BOTS_FILE_OUT"] = outfile

    config_arg = '-c%s' % config_dir

    pargs = ['bots-engine', config_arg, route]

    try:
        proc = subprocess.Popen(pargs, stdout=STDOUT, stderr=STDERR)
        stdoutdata, stderrdata = proc.communicate()
        if VERBOSE:
            if not isinstance(stdoutdata, str):
                stdoutdata = stdoutdata.decode()
            if not isinstance(stderrdata, str):
                stderrdata = stderrdata.decode()
            info(stdoutdata)
            info(stderrdata)
        returncode = proc.returncode
        if returncode == 0:
            info("Output %s file translated: '%s'" % (outtype.upper(), os.path.basename(outfile)))
            logger.debug("Output %s file translated: '%s'", outtype.upper(), outfile)
            # Output validation
            if do_validation or build_report:
                info("Validating output %s invoice '%s' ..." % (outtype, outfile))
                report = None if build_report else tempfile.mktemp()
                try:
                    report = build_validation_report(outtype, outfile, report)
                except:
                    error(traceback.format_exc(limit=0))
                    return 7
                if report and do_validation:
                    is_valid = parse_validation_report(report)
                    returncode = int(not bool(is_valid))
                if not build_report:
                    os.remove(report)
        elif returncode == 3:
            error('Another instance of translator is running, try again in a few moment')
        elif returncode == 2:
            error('ERROR during translating %s file: %s ' % (
                intype.upper(), os.path.basename(outfile)))
            botsinit.generalinit(config_dir)
            from bots.models import filereport

            filerep = filereport.objects.filter(
                infilename=infile).exclude(statust=3).order_by('-idta').first()
            for err in filerep.errortext.split('MessageError:')[1:]:
                err = err.strip().replace(' "BOTSCONTENT"', '').replace('Exception: ', '')
                error(err)
        elif returncode != 0:
            error('Unexpected error %s occured' % returncode, 'proc: %s' % repr(proc.__dict__))
            return returncode
        del os.environ["BOTS_FILE_IN"]
        del os.environ["BOTS_FILE_OUT"]
        return returncode

    except Exception as exc:
        error(traceback.format_exc())
        del os.environ["BOTS_FILE_IN"]
        del os.environ["BOTS_FILE_OUT"]
        error('Exception occured: %s' % exc)


def cii2ubl(*args):
    if args:
        return start('CII_2_UBL', 'cii2ubl', *args)
    sys.exit(start('CII_2_UBL', 'cii2ubl'))


def ubl2cii(*args):
    if args:
        return start('UBL_2_CII', 'ubl2cii', *args)
    sys.exit(start('UBL_2_CII', 'ubl2cii'))
