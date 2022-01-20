# -*- coding: utf-8 -*-
"""
bots-grammar: xml
xml-schema: CrossIndustryInvoice_100pD16B.xsd
Author: Ludovic Watteaux
"""
from bots.botsconfig import ID, MIN, MAX, LEVEL, QUERIES

from .D16Brecords import (version, rsm, qdt, udt, ram, xsi, recorddefs)
from .D16Bsequences import sequence


syntax = {
    'merged': False,
    'indented': True,
    'rsm': rsm,
    'qdt': qdt,
    'udt': udt,
    'ram': ram,
    'xsi': xsi,
    'datetime_format': '102',
    'schema_version': version,
    'schema_location': rsm.strip('{}')+' CrossIndustryInvoice_100pD16B.xsd',
    'namespace_prefixes': [
        ('rsm', rsm.strip('{}')),
        ('qdt', qdt.strip('{}')),
        ('udt', udt.strip('{}')),
        ('ram', ram.strip('{}')),
        ('xsi', xsi.strip('{}')),
    ],
}


structure = [
{ID: rsm+'CrossIndustryInvoice', MIN: 1, MAX: 1,
    QUERIES: {
        'reference': (
            {'BOTSID': rsm+'CrossIndustryInvoice'},
            {'BOTSID': rsm+'ExchangedDocument'},
            {'BOTSID': ram+'ID', 'BOTSCONTENT': None},
        ),
        'testindicator': (
            {'BOTSID': rsm+'CrossIndustryInvoice'},
            {'BOTSID': ram+'ExchangedDocumentContextType'},
            {'BOTSID': ram+'TestIndicator'},
            {'BOTSID': udt+'Indicator', 'BOTSCONTENT': None},
        ),
        'doctype': (
            {'BOTSID': rsm+'CrossIndustryInvoice'},
            {'BOTSID': rsm+'ExchangedDocument'},
            {'BOTSID': rsm+'TypeCode', 'BOTSCONTENT': None},
        ),
    },
    LEVEL: sequence(rsm+'CrossIndustryInvoiceType'),
}]
