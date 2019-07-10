# -*- coding: utf-8 -*-
# Author: Ludovic Watteaux
#
# bots/usersys/communicationscripts/bots_file_out.py

import os
from shutil import move
from bots import botsglobal


def connect(channeldict):
    pass


def filename(channeldict, ta, filename):
    return os.path.basename(os.environ.get("BOTS_FILE_OUT"))


def main(channeldict, filename, ta, *args, **kwargs):
    outfile = os.environ.get("BOTS_FILE_OUT")
    if outfile:
        botsglobal.logger.info('outfile: %s ...' % outfile)
        move(filename, outfile)
