# -*- coding: utf-8 -*-
# Author: Ludovic Watteaux
#
# bots/usersys/communicationscripts/bots_file_in.py

import os

from bots import botsglobal


def connect(channeldict):
    pass


def main(channeldict):
    infile = os.environ.get('BOTS_FILE_IN')
    if infile:
        botsglobal.logger.info('BOTS_FILE_IN: %s' % infile)
        if os.path.isfile(infile):
            yield infile


def disconnect(channeldict):
    pass
