# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import subprocess
import sys
import traceback
from bots import botsinit
try:
    import bots.config_ublcii
except ImportError:
    from . import egg_install
    egg_install()

from . import start_logging, log, error, fatalerror


def start(route, prog):
    """Start translating"""

    start_logging()
    usage = """
Usage:
    %(prog)s input.xml output.xml

    -r          Replace output file if exist

    input:      Input file to transtate
    output:     Output translated file path
"""

    intype, outtype = prog.upper().split('2')
    usage %= {
        'prog': prog,
    }

    infile = outfile = None
    replaceexisting = False
    verbose = False
    stdout = stderr = subprocess.PIPE
    for arg in sys.argv[1:]:
        if arg in ['-r', '--replace']:
            replaceexisting = True
        elif arg == '-v':
            verbose = True
        elif arg in ['?', '/?', '-h', '--help'] or arg.startswith('-'):
            fatalerror(usage)
        elif not infile:
            infile = arg
        elif not outfile:
            outfile = arg
        else:
            fatalerror(usage)

    if not infile:
        fatalerror('No input file specified', usage)
    elif not os.path.isfile(infile):
        fatalerror("Invalid input file: '%s'" % infile)

    infile = os.path.abspath(infile)
    log("Input %s file: '%s'" % (intype, infile))

    if not outfile:
        fatalerror('No output file path specified', usage)
    elif os.path.isfile(outfile) and not replaceexisting:
        fatalerror("Output file exist: '%s'\nUse -r to replace existing file" % outfile)
    elif not os.path.isdir(os.path.dirname(outfile)):
        fatalerror('Output path is not a valid directory: %s' % outfile)

    outfile = os.path.abspath(outfile)

    os.environ.setdefault("BOTS_FILE_IN", infile)
    os.environ.setdefault("BOTS_FILE_OUT", outfile)

    config_dir = 'config_ublcii'
    config_arg = '-c%s' % config_dir

    pargs = ['bots-engine']
    pargs.append(config_arg)
    pargs.append(route)

    try:
        proc = subprocess.Popen(pargs, stdout=stdout, stderr=stderr)
        stdoutdata, stderrdata = proc.communicate()
        if verbose:
            log(stdoutdata.decode())
            log(stderrdata.decode())
        returncode = proc.returncode
        if returncode == 0:
            log("Output %s translated file: '%s'" % (outtype, outfile))
        elif returncode == 3:
            error('Another instance of translator is running, try again in a few moment')
        elif returncode == 2:
            error('ERROR during translating %s file: %s ' % (
                intype, os.path.basename(outfile)))
            botsinit.generalinit(config_dir)
            from bots.models import filereport
            filerep = filereport.objects.filter(infilename=infile).exclude(statust=3).last()
            for err in filerep.errortext.split('MessageError:')[1:]:
                err = err.rstrip(os.linesep)
                error('MessageError:%s' % err)
        elif returncode != 0:
            fatalerror('Unexpected error %s occured' % returncode,
                       'proc: %s' % repr(proc.__dict__))

    except Exception as exc:
        error(traceback.format_exc())
        fatalerror('Exception occured: %s' % exc)


def cii2ubl():
    start('CII_2_UBL', 'cii2ubl')


def ubl2cii():
    start('UBL_2_CII', 'ubl2cii')
