# -*- coding: utf-8 -*-
"""
bots-grammar: xml
xml-schema: CrossIndustryInvoice_100pD16B.xsd
Author: Ludovic Watteaux
"""
from bots.botsconfig import ID, MIN, MAX, LEVEL, QUERIES

from .D16Brecords import (version, rsm, qdt, udt, ram, recorddefs)
from .D16Bsequences import sequence


syntax = {
    'reference': version,
    'merged': False,
    'indented': True,
    'rsm': rsm,
    'qdt': qdt,
    'udt': udt,
    'ram': ram,
    'namespace_prefixes': [
        ('rsm', rsm.strip('{}')),
        ('qdt', qdt.strip('{}')),
        ('udt', udt.strip('{}')),
        ('ram', ram.strip('{}')),
    ],
}


structure = [
{ID: rsm+'CrossIndustryInvoice', MIN: 1, MAX: 1,
    QUERIES: {
        'testindicator': (
            {'BOTSID': rsm+'CrossIndustryInvoice'},
            {'BOTSID': ram+'ExchangedDocumentContextType'},
            {'BOTSID': ram+'TestIndicator'},
            {'BOTSID': udt+'IndicatorString', 'BOTSCONTENT': None},
            # {'BOTSID': udt+'Indicator', 'BOTSCONTENT': None},
        )
    },
    LEVEL: sequence(rsm+'CrossIndustryInvoiceType'),
}]
