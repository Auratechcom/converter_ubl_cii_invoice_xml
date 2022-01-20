# -*- coding: utf-8 -*-
# Author: Ludovic Watteaux
#
# bots/usersys/routescripts/UBL_2_CII.py
from __future__ import unicode_literals

try:
    from xml.etree import cElementTree as etree
except ImportError:
    from xml.etree import ElementTree as etree

from bots.botsconfig import OK
from bots import botsglobal, botslib, preprocess


def postincommunication(routedict, *args, **kwargs):
    preprocess.preprocess(routedict, ubl_preprocess)


def ubl_preprocess(ta_from, endstatus, *args, **kwargs):
    """Parse incoming UBL to find his type"""
    try:
        # copy ta for preprocessing
        ta_to = ta_from.copyta(status=endstatus)
        # Get UBL type (/CreditNote, /Invoice)
        doc = etree.parse(botslib.abspathdata(ta_from.filename))
        root = doc.getroot()
        if not root.tag.startswith('{urn:oasis:names:specification:ubl:schema:xsd'):
            raise Exception('Incoming file is not an UBL file.')
        ubltype = root.tag.split('}')[-1]
        botsglobal.logger.debug('UBL type: %s', ubltype)
        if ubltype == 'CreditNote':
            ta_to.update(messagetype='UBL21_%s' % ubltype)
        elif ubltype != 'Invoice':
            raise Exception('Incoming UBL file is not an Invoice or CreditNote.')
        # write out file
        filename = str(ta_to.idta)
        botslib.opendata_bin(filename, 'wb').write(
            botslib.opendata_bin(ta_from.filename, 'rb').read())
        # update ta
        ta_to.update(statust=OK, filename=filename)
    
    except:
        txt = botslib.txtexc()
        botsglobal.logger.error('UBL preprocess failed: %s', txt)
        raise botslib.InMessageError('UBL preprocess failed: %(error)s', error=txt)
