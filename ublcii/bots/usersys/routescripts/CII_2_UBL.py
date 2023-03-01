# -*- coding: utf-8 -*-
# Author: Ludovic Watteaux
#
# bots/usersys/routescripts/CII_2_UBL.py
from __future__ import unicode_literals

try:
    from xml.etree import cElementTree as etree
except ImportError:
    from xml.etree import ElementTree as etree

from bots.botsconfig import OK
from bots import botsglobal, botslib, preprocess


def pretranslation(routedict, *args, **kwargs):
    preprocess.preprocess(routedict, cii_preprocess)


def cii_preprocess(ta_from, endstatus, *args, **kwargs):
    """Parse incoming CII to find his type"""
    try:
        # copy ta for preprocessing
        ta_to = ta_from.copyta(status=endstatus)

        # Get typecode by parsing incoming CII to /CrossIndustryInvoice /ExchangedDocument /TypeCode
        doc = etree.parse(botslib.abspathdata(ta_from.filename))
        namespaces = {
            'rsm': 'urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100',
            'ram': 'urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100',
        }
        root = doc.getroot()
        if root.tag != '{%s}CrossIndustryInvoice' % namespaces['rsm']:
            raise Exception('Incoming file is not a CrossIndustryInvoice file.')
        typecode = getattr(
            doc.find('.//rsm:ExchangedDocument/ram:TypeCode', namespaces=namespaces), 'text', None)
        botsglobal.logger.debug('CII typecode: %s', typecode)
        # 380=Invoice, 381=Avoir > UBL CreditNote
        if typecode == '381':
            ta_to.update(alt='cii2creditnote')
        # write out file
        filename = str(ta_to.idta)
        botslib.opendata_bin(filename, 'wb').write(
            botslib.opendata_bin(ta_from.filename, 'rb').read())
        # update ta
        ta_to.update(statust=OK, filename=filename)

    except:
        txt = botslib.txtexc()
        botsglobal.logger.error('CII preprocess failed: %s', txt)
        raise botslib.InMessageError('CII preprocess failed: %(error)s', error=txt)
