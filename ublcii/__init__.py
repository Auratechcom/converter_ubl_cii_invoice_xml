# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import os
import platform
import sys
import shutil
import pkg_resources

from .__about__ import (
    __version__, __version_info__,
    __title__, __summary__, __url__,
    __author__, __email__, __license__, __copyright__,
)

__all__ = [
    '__version__', '__version_info__',
    '__title__', '__summary__', '__url__',
    '__author__', '__email__', '__license__', '__copyright__',
    'log', 'error', 'fatalerror', 'start_logging',
    'setupenv', 'egg_install', 'clean',
]


logger = logging.getLogger('ublcii')


def start_logging(level='INFO'):
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(levelname)-8s %(message)s",
            '%Y.%m.%d %H:%M:%S')
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)
    logger.setLevel(logging.getLevelName(os.environ.get('UBLCII_LOG_LEVEL', level)))


def log(*args):
    """Log all input str args to sys.stderr"""
    try:
        logger.info(''.join(args))
    except:
        logger.info(repr(args))


def error(*args):
    """Log error"""
    try:
        logger.error(''.join(args))
    except:
        logger.error(repr(args))



def fatalerror(*args):
    """Log error and exit"""
    error(*args)
    sys.exit(1)


def setupenv(botsenv='_ublcii', **kwargs):
    """Setup bots env"""

    start_logging(kwargs.get('loglevel', 'INFO'))
    log('############# UBLCII SETUP ###############')
    devel = kwargs.get('devel')
    install = kwargs.get('install')
    try:
        import bots
    except ImportError:
        if install or devel:
            return
        raise Exception('Bots is not installed')

    log('Setting up ublcii env ...')
    bots_path = os.path.abspath(os.path.dirname(bots.__file__))
    ublcii_path = os.path.abspath(os.path.dirname(__file__))

    method = kwargs.get('method')
    if not method:
        operating_system = platform.system()
        if operating_system in ['Linux', 'Darwin']:
            method = 'symlink'
        else:
            method = 'copy'
            import compileall

    update_egg_info = kwargs.get('update_egg_info', install or devel)
    additional_files = []
    pkg = pkg_resources.get_distribution('ublcii')
    bots_pkg = pkg_resources.get_distribution('bots-ediint')
    if hasattr(bots_pkg, 'zipinfo'):
        raise Exception('Zipped bots package is not compatible with ublcii')
    for botsdir in ['config', 'usersys', 'botssys']:
        origin = os.path.join(ublcii_path, 'bots', botsdir)
        target = os.path.join(bots_path, '%s%s' % (botsdir, botsenv))
        prefix = os.path.commonprefix([ublcii_path, bots_path])
        if os.path.islink(target):
            log('remove symlink: %s' % target)
            os.unlink(target)
        elif os.path.isdir(target):
            log('Remove existing directory: %s' % target)
            shutil.rmtree(target)
        if method == 'symlink' and botsdir != 'botssys':
            if install or devel:
                origin = os.path.join(os.pardir, 'ublcii', 'bots', botsdir)
                # If ublcii.egg/ublcii
                if os.path.dirname(os.path.dirname(__file__)).endswith('.egg'):
                    egg_dirname = os.path.dirname(
                        os.path.dirname(__file__)).split(os.path.sep)[-1]
                    origin = os.path.join(os.pardir, egg_dirname, 'ublcii', 'bots', botsdir)
                # If bots.egg/bots
                if os.path.dirname(os.path.dirname(bots.__file__)).endswith('.egg'):
                    origin = os.path.join(os.pardir, origin)
            elif prefix != os.path.sep:
                origin = os.path.join(os.pardir, ublcii_path.split(prefix)[1], 'bots', botsdir)
            log('Symlinking %s to %s' % (origin, target))
            os.symlink(origin, target)
            if update_egg_info:
                additional_files.append(target.split(prefix)[1])
        elif method == 'copy' or botsdir == 'botssys':
            log('Copying fixtures files: %s' % origin)
            shutil.copytree(origin, target)
            if botsdir != 'botssys':
                compileall.compile_dir(target)
            if update_egg_info:
                for (dirpath, _, filenames) in os.walk(target):
                    additional_files.extend([os.path.join(
                        dirpath.split(prefix)[1], filename) for filename in filenames])

    if update_egg_info and len(additional_files) > 0:
        # Add new files to egg-info/installed-files.txt or RECORD
        inst_files = 'installed-files.txt'
        if os.path.isfile(os.path.join(pkg.egg_info, 'WHEEL')):
            inst_files = 'RECORD'
        inst_files = os.path.join(pkg.egg_info, inst_files)
        if os.path.isfile(inst_files):
            log('Updating egg-info/%s' % os.path.basename(inst_files))
            with open(inst_files, 'a') as install_f:
                pat = '%s\r\n'
                if inst_files.endswith('RECORD'):
                    pat = '%s,,\r\n'
                install_f.write(''.join(
                    [pat % line for line in additional_files]))
    log('############# UBLCII SETUP END ###############')


def egg_install(loglevel='WARNING'):
    """Install ubcii bots env and update egg-info/RECORD"""
    setupenv(update_egg_info=True, loglevel=loglevel)


def clean():
    """Clean bots/*_ublcii"""
    try:
        import bots.config_ublcii
        setupenv()
    except ImportError:
        egg_install()
