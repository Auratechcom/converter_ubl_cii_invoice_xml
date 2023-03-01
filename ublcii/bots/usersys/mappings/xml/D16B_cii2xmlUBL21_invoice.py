# -*- coding: utf-8 -*-
"""
bots-mapping-script
Message: xml/D16B_CII > xml/UBL21_INVOICE
Author: Ludovic Watteaux
"""
from __future__ import unicode_literals, division

from bots import transform
from bots.grammar import grammarread


def get_grammar(msg):
    args = [msg.ta_info['editype'], msg.ta_info['messagetype']]
    if grammarread.__code__.co_argcount > 2:
        args.append('grammars')
    return grammarread(*args)


def transformdate(datestr, code=102):
    dateformat = 'CCYYMMDD'
    if code == 102:
        dateformat = 'CCYYMMDD'
    return transform.datemask(datestr, dateformat, 'CCYY-MM-DD')


CII2475_TO_UBL2005 = {
    '5': '3',
    '29': '29',
    '72': '432',
}


def cii2475_to_ubl2005(code):
    return CII2475_TO_UBL2005.get(code, code)


def main(inn, out):

    # IN Message: xml/D16B_CII
    rsm = inn.ta_info['rsm']
    qdt = inn.ta_info['qdt']
    udt = inn.ta_info['udt']
    ram = inn.ta_info['ram']

    # OUT Message: xml/UBL21_INVOICE
    out_syntax = get_grammar(out).syntax
    xmlns = out_syntax['xmlns']
    cbc = out_syntax['cbc']
    cac = out_syntax['cac']
    ext = out_syntax['ext']
    xsi = out_syntax['xsi']
    # Ubl type: Invoice or CreditNote
    ubltype = out_syntax['ubltype']

    out.ta_info['reference'] = inn.ta_info['reference']

    out.put({'BOTSID': xmlns+ubltype, xmlns+ubltype+'__xmlns:ccts': out_syntax['ccts'].strip('{}')})
    out.put({'BOTSID': xmlns+ubltype, xmlns+ubltype+'__xmlns:qdt': out_syntax['qdt'].strip('{}')})
    out.put({'BOTSID': xmlns+ubltype, xmlns+ubltype+'__xmlns:udt': out_syntax['udt'].strip('{}')})
    out.put({'BOTSID': xmlns+ubltype, xmlns+ubltype+'__'+xsi+'schemaLocation': out_syntax['schema_location']})

    # +/Invoice /UBLVersionID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'UBLVersionID', 'BOTSCONTENT': out_syntax['schema_version']})

    # -/CrossIndustryInvoice /ExchangedDocument /ID
    # +/Invoice /ID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceCurrencyCode
    invoicecurrencycode = inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceCurrencyCode', 'BOTSCONTENT': None}) or 'EUR'

    for includednote in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'IncludedNote'}):

        # -/CrossIndustryInvoice /ExchangedDocument /IncludedNote /SubjectCode
        subjectcode = includednote.get({'BOTSID': ram+'IncludedNote'}, {'BOTSID': ram+'SubjectCode', 'BOTSCONTENT': None})
        subjectcode = '#%s#' % subjectcode if subjectcode else ''

        for content in includednote.getloop({'BOTSID': ram+'IncludedNote'}, {'BOTSID': ram+'Content'}):

            note = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'Note'})

            # -/CrossIndustryInvoice /ExchangedDocument /IncludedNote /Content
            # +/Invoice /Note
            note.put({'BOTSID': cbc+'Note', 'BOTSCONTENT': '%s%s' % (subjectcode, content.get({'BOTSID': ram+'Content', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /ExchangedDocument /IssueDateTime /DateTimeString
    # +/Invoice /IssueDate
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'IssueDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'IssueDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /ExchangedDocument /TypeCode
    # +/Invoice /InvoiceTypeCode
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+ubltype+'TypeCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /ExchangedDocumentContext /BusinessProcessSpecifiedDocumentContextParameter /ID
    # +/Invoice /ProfileID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'ProfileID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocumentContext'}, {'BOTSID': ram+'BusinessProcessSpecifiedDocumentContextParameter'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /ExchangedDocumentContext /GuidelineSpecifiedDocumentContextParameter /ID
    # +/Invoice /CustomizationID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'CustomizationID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocumentContext'}, {'BOTSID': ram+'GuidelineSpecifiedDocumentContextParameter'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    for additionalreferenceddocument in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'AdditionalReferencedDocument'}):

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /IssuerAssignedID
        addrefdocissuerassignedid = additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /TypeCode
        adddocreftypecode = additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': None})

        if adddocreftypecode == '50' and addrefdocissuerassignedid:
            # BT-17
            # /Invoice /OriginatorDocumentReference
            originatordocumentreference = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'OriginatorDocumentReference'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /IssuerAssignedID
            # +/Invoice /OriginatorDocumentReference /ID
            originatordocumentreference.put({'BOTSID': cac+'OriginatorDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': addrefdocissuerassignedid})
            continue

        additionaldocumentreference = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AdditionalDocumentReference'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /AttachmentBinaryObject
        # +/Invoice /AdditionalDocumentReference /Attachment /EmbeddedDocumentBinaryObject
        additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cbc+'EmbeddedDocumentBinaryObject', 'BOTSCONTENT': additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'AttachmentBinaryObject', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /AttachmentBinaryObject /AttachmentBinaryObject__filename
        # +/Invoice /AdditionalDocumentReference /Attachment /EmbeddedDocumentBinaryObject /EmbeddedDocumentBinaryObject__filename
        additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cbc+'EmbeddedDocumentBinaryObject', cbc+'EmbeddedDocumentBinaryObject__filename': additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'AttachmentBinaryObject', ram+'AttachmentBinaryObject__filename': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /AttachmentBinaryObject /AttachmentBinaryObject__mimeCode
        # +/Invoice /AdditionalDocumentReference /Attachment /EmbeddedDocumentBinaryObject /EmbeddedDocumentBinaryObject__mimeCode
        additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cbc+'EmbeddedDocumentBinaryObject', cbc+'EmbeddedDocumentBinaryObject__mimeCode': additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'AttachmentBinaryObject', ram+'AttachmentBinaryObject__mimeCode': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /IssuerAssignedID
        # +/Invoice /AdditionalDocumentReference /ID
        additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': addrefdocissuerassignedid})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /ReferenceTypeCode
        # +/Invoice /AdditionalDocumentReference /ID /ID__schemeID
        additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'ReferenceTypeCode', 'BOTSCONTENT': None})})

        if adddocreftypecode not in [None, '', '916']:
            # +/Invoice /AdditionalDocumentReference /DocumentTypeCode
            additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'DocumentTypeCode', 'BOTSCONTENT': adddocreftypecode})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /Name
        # +/Invoice /AdditionalDocumentReference /DocumentDescription
        additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'DocumentDescription', 'BOTSCONTENT': additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /URIID
        # +/Invoice /AdditionalDocumentReference /Attachment /ExternalReference /URI
        additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cac+'ExternalReference'}, {'BOTSID': cbc+'URI', 'BOTSCONTENT': additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerOrderReferencedDocument /IssuerAssignedID
    # +/Invoice /OrderReference /ID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'OrderReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerOrderReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerReference
    # +/Invoice /BuyerReference
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'BuyerReference', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerReference', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /EmailURIUniversalCommunication /URIID
    # +/Invoice /AccountingCustomerParty /Party /Contact /ElectronicMail
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'ElectronicMail', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'EmailURIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /FaxUniversalCommunication /CompleteNumber
    # +/Invoice /AccountingCustomerParty /Party /Contact /Telefax
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Telefax', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'FaxUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /PersonName
    buyerpersonname = inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'PersonName', 'BOTSCONTENT': None}) or ''

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /DepartmentName
    buyerdptname = inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'DepartmentName', 'BOTSCONTENT': None}) or ''

    if buyerpersonname or buyerdptname:
        buyerdptname = '(%s)' % buyerdptname if buyerdptname else ''
        customercontactname = '%s%s' % (buyerpersonname, buyerdptname)

        # +/Invoice /AccountingCustomerParty /Party /Contact /Name
        out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': customercontactname})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /TelephoneUniversalCommunication /CompleteNumber
    # +/Invoice /AccountingCustomerParty /Party /Contact /Telephone
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Telephone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'TelephoneUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': None})})

    for description in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'Description'}):

        partylegalentity = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /Description
        # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyLegalForm
        partylegalentity.put({'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyLegalForm', 'BOTSCONTENT': description.get({'BOTSID': ram+'Description', 'BOTSCONTENT': None})})


    for globalid in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'GlobalID'}):

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /GlobalID
        globid = globalid.get({'BOTSID': ram+'GlobalID', 'BOTSCONTENT': None})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /GlobalID /GlobalID__schemeID
        globschemeid = globalid.get({'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': None})

        if globid and globschemeid:
            customerpartyidentification = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'})

            # +/Invoice /AccountingCustomerParty /Party /PartyIdentification /ID
            # +/Invoice /AccountingCustomerParty /Party /PartyIdentification /ID /ID__schemeID
            customerpartyidentification.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': globschemeid, 'BOTSCONTENT': globid})
            # Only one occurence if not UBL validation error occur:
            # [UBL-SR-16]-Buyer identifier shall occur maximum once
            break

    for id in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'ID'}):

        if out.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None}):
            # [UBL-SR-16]-Buyer identifier shall occur maximum once
            break
        customerpartyidentification2 = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /ID
        # +/Invoice /AccountingCustomerParty /Party /PartyIdentification /ID
        customerpartyidentification2.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': id.get({'BOTSID': ram+'ID', 'BOTSCONTENT': None})})
        break

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /Name
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'RegistrationName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CityName
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /CityName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountryID
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /Country /IdentificationCode
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountryName
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /Country /Name
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountrySubDivisionName
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /CountrySubentity
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineOne
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /StreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineThree
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /AddressLine /Line
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineTwo
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /AdditionalStreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /PostcodeCode
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /PostalZone
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /ID
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyID /CompanyID__schemeID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CityName
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /CityName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryID
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /Country /IdentificationCode
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryName
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /Country /Name
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountrySubDivisionName
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /CountrySubentity
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineOne
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /StreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineThree
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /AddressLine /Line
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineTwo
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /AdditionalStreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /PostcodeCode
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /PostalZone
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    # +/Invoice /AccountingCustomerParty /Party /PartyName /Name
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /URIUniversalCommunication /URIID
    # +/Invoice /AccountingCustomerParty /Party /EndpointID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /URIUniversalCommunication /URIID /URIID__schemeID
    # +/Invoice /AccountingCustomerParty /Party /EndpointID /EndpointID__schemeID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', cbc+'EndpointID__schemeID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', ram+'URIID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /ContractReferencedDocument /IssuerAssignedID
    # +/Invoice /ContractDocumentReference /ID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'ContractDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'ContractReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /ContractReferencedDocument /ReferenceTypeCode
    reftypecode = inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'ContractReferencedDocument'}, {'BOTSID': ram+'ReferenceTypeCode', 'BOTSCONTENT': None})

    documenttypecode = None
    if reftypecode == 'BC':
        documenttypecode = 'Bon de commande'
    elif reftypecode == 'CT':
        documenttypecode = 'Contrat'

    # +/Invoice /ContractDocumentReference /DocumentTypeCode
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'ContractDocumentReference'}, {'BOTSID': cbc+'DocumentTypeCode', 'BOTSCONTENT': documenttypecode})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerOrderReferencedDocument /IssuerAssignedID
    # +/Invoice /OrderReference /SalesOrderID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'OrderReference'}, {'BOTSID': cbc+'SalesOrderID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerOrderReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CityName
    # +/Invoice /TaxRepresentativeParty /PostalAddress /CityName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CountryID
    # +/Invoice /TaxRepresentativeParty /PostalAddress /Country /IdentificationCode
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CountrySubDivisionName
    # +/Invoice /TaxRepresentativeParty /PostalAddress /CountrySubentity
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineOne
    # +/Invoice /TaxRepresentativeParty /PostalAddress /StreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineThree
    # +/Invoice /TaxRepresentativeParty /PostalAddress /AddressLine /Line
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineTwo
    # +/Invoice /TaxRepresentativeParty /PostalAddress /AdditionalStreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /PostcodeCode
    # +/Invoice /TaxRepresentativeParty /PostalAddress /PostalZone
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /Name
    # +/Invoice /TaxRepresentativeParty /PartyName /Name
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

    for specifiedtaxregistration in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'}):

        partytaxscheme3 = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PartyTaxScheme'})

        # Fixed: 'VAT'
        # +/Invoice /TaxRepresentativeParty /PartyTaxScheme /TaxScheme /ID
        partytaxscheme3.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': 'VAT'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /SpecifiedTaxRegistration /ID
        # +/Invoice /TaxRepresentativeParty /PartyTaxScheme /CompanyID
        partytaxscheme3.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': specifiedtaxregistration.get({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /EmailURIUniversalCommunication /URIID
    # +/Invoice /AccountingSupplierParty /Party /Contact /ElectronicMail
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'ElectronicMail', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'EmailURIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /FaxUniversalCommunication /CompleteNumber
    # +/Invoice /AccountingSupplierParty /Party /Contact /Telefax
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Telefax', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'FaxUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /PersonName
    sellerpersonname = inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'PersonName', 'BOTSCONTENT': None}) or ''

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /DepartmentName
    sellerdptname = inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'DepartmentName', 'BOTSCONTENT': None}) or ''

    if sellerpersonname or sellerdptname:
        sellerdptname = '(%s)' % sellerdptname if sellerdptname else ''
        suppliercontactname = '%s%s' % (sellerpersonname, sellerdptname)

        # +/Invoice /AccountingSupplierParty /Party /Contact /Name
        out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': suppliercontactname})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /TelephoneUniversalCommunication /CompleteNumber
    # +/Invoice /AccountingSupplierParty /Party /Contact /Telephone
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Telephone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'TelephoneUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': None})})

    for description2 in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'Description'}):

        partylegalentity2 = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /Description
        # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyLegalForm
        partylegalentity2.put({'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyLegalForm', 'BOTSCONTENT': description2.get({'BOTSID': ram+'Description', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /URIUniversalCommunication /URIID
    # +/Invoice /AccountingSupplierParty /Party /EndpointID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /URIUniversalCommunication /URIID /URIID__schemeID
    # +/Invoice /AccountingSupplierParty /Party /EndpointID /EndpointID__schemeID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', cbc+'EndpointID__schemeID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', ram+'URIID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /CreditorReferenceID
    creditorreferenceid = inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'CreditorReferenceID', 'BOTSCONTENT': None})
    # +/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': 'SEPA', 'BOTSCONTENT': creditorreferenceid})

    for globalid in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'GlobalID'}):

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /GlobalID
        globid = globalid.get({'BOTSID': ram+'GlobalID', 'BOTSCONTENT': None})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /GlobalID /GlobalID__schemeID
        globschemeid = globalid.get({'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': None})

        if globid and globschemeid:
            supplierpartyidentification2 = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'})

            # +/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID
            # +/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID /ID__schemeID
            supplierpartyidentification2.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': globschemeid, 'BOTSCONTENT': globid})

    for sellertradepartyid in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'ID'}):

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /ID
        sellertradeid = sellertradepartyid.get({'BOTSID': ram+'ID', 'BOTSCONTENT': None})

        if sellertradeid:
            supplierpartyidentification3 = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'})

            # +/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID
            supplierpartyidentification3.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': sellertradeid})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /Name
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'RegistrationName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CityName
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /CityName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountryID
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /Country /IdentificationCode
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountryName
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /Country /Name
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountrySubDivisionName
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /CountrySubentity
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineOne
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /StreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineThree
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /AddressLine /Line
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineTwo
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /AdditionalStreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /PostcodeCode
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /PostalZone
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /ID
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyID /CompanyID__schemeID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CityName
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /CityName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryID
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /Country /IdentificationCode
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryName
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /Country /Name
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountrySubDivisionName
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /CountrySubentity
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineOne
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /StreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineThree
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /AddressLine /Line
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineTwo
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /AdditionalStreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /PostcodeCode
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /PostalZone
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    # +/Invoice /AccountingSupplierParty /Party /PartyName /Name
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': None})})

    for sellertaxregistration in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'}):

        suppliertaxscheme = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyTaxScheme'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedTaxRegistration /ID
        # +/Invoice /AccountingSupplierParty /Party /PartyTaxScheme /CompanyID
        suppliertaxscheme.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': sellertaxregistration.get({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        # Fixed: 'VAT'
        # +/Invoice /AccountingSupplierParty /Party /PartyTaxScheme /TaxScheme /ID
        suppliertaxscheme.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': 'VAT'})

    for buyertaxregistration in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'}):

        customertaxscheme = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyTaxScheme'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedTaxRegistration /ID
        # +/Invoice /AccountingCustomerParty /Party /PartyTaxScheme /CompanyID
        customertaxscheme.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': buyertaxregistration.get({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        # Fixed: 'VAT'
        # +/Invoice /AccountingCustomerParty /Party /PartyTaxScheme /TaxScheme /ID
        customertaxscheme.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': 'VAT'})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SpecifiedProcuringProject /ID
    specifiedprocuringprojectid = inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SpecifiedProcuringProject'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})

    if specifiedprocuringprojectid:
        if ubltype == 'Invoice':
            # +/Invoice /ProjectReference /ID
            out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'ProjectReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': specifiedprocuringprojectid})

        elif ubltype == 'CreditNote':
            # + /Invoice /AdditionalDocumentReference
            additionaldocumentreference = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AdditionalDocumentReference'})

            # + /Invoice /AdditionalDocumentReference /ID
            additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': specifiedprocuringprojectid})

            # + /Invoice /AdditionalDocumentReference /DocumentTypeCode
            # - Fixed: '50'
            additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'DocumentTypeCode', 'BOTSCONTENT': '50'})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ActualDeliverySupplyChainEvent /OccurrenceDateTime /DateTimeString
    # +/Invoice /Delivery /ActualDeliveryDate
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cbc+'ActualDeliveryDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ActualDeliverySupplyChainEvent'}, {'BOTSID': ram+'OccurrenceDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /DespatchAdviceReferencedDocument /IssuerAssignedID
    # +/Invoice /DespatchDocumentReference /ID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'DespatchDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'DespatchAdviceReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ReceivingAdviceReferencedDocument /IssuerAssignedID
    # +/Invoice /ReceiptDocumentReference /ID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'ReceiptDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ReceivingAdviceReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    for shiptotradepartydescription in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'Description'}):

        deliverydescription = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'Description'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /Description
        # +/Invoice /Delivery /DeliveryLocation /Description
        deliverydescription.put({'BOTSID': cbc+'Description', 'BOTSCONTENT': shiptotradepartydescription.get({'BOTSID': ram+'Description', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /GlobalID
    # +/Invoice /Delivery /DeliveryLocation /ID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'GlobalID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /GlobalID /GlobalID__schemeID
    # +/Invoice /Delivery /DeliveryLocation /ID /ID__schemeID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': None})})

    if not out.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None}):
        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /ID
        # +/Invoice /Delivery /DeliveryLocation /ID
        out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /Name
    # +/Invoice /Delivery /DeliveryParty /PartyName /Name
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CityName
    # +/Invoice /Delivery /DeliveryLocation /Address /CityName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CountryID
    # +/Invoice /Delivery /DeliveryLocation /Address /Country /IdentificationCode
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CountrySubDivisionName
    # +/Invoice /Delivery /DeliveryLocation /Address /CountrySubentity
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineOne
    # +/Invoice /Delivery /DeliveryLocation /Address /StreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineThree
    # +/Invoice /Delivery /DeliveryLocation /Address /AddressLine /Line
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineTwo
    # +/Invoice /Delivery /DeliveryLocation /Address /AdditionalStreetName
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /PostcodeCode
    # +/Invoice /Delivery /DeliveryLocation /Address /PostalZone
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # update for nocheck
    taxtotal = None

    for taxtotalamount in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxTotalAmount'}):

        taxtotal = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxTotal'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxTotalAmount
        # +/Invoice /TaxTotal /TaxAmount
        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxTotalAmount /TaxTotalAmount__currencyID
        # +/Invoice /TaxTotal /TaxAmount /TaxAmount__currencyID
        taxtotal.put({'BOTSID': cac+'TaxTotal'}, {'BOTSID': cbc+'TaxAmount', 'BOTSCONTENT': taxtotalamount.get({'BOTSID': ram+'TaxTotalAmount', 'BOTSCONTENT': None}), cbc+'TaxAmount__currencyID': taxtotalamount.get({'BOTSID': ram+'TaxTotalAmount', ram+'TaxTotalAmount__currencyID': None}) or invoicecurrencycode})

    if not taxtotal:
        taxtotal = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxTotal'})

    for applicabletradetax in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'}):

        taxsubtotal = taxtotal.putloop({'BOTSID': cac+'TaxTotal'}, {'BOTSID': cac+'TaxSubtotal'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CategoryCode
        # +/Invoice /TaxTotal /TaxSubtotal /TaxCategory /ID
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /BasisAmount
        # +/Invoice /TaxTotal /TaxSubtotal /TaxableAmount
        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /BasisAmount /BasisAmount__currencyID
        # +/Invoice /TaxTotal /TaxSubtotal /TaxableAmount /TaxableAmount__currencyID
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxableAmount', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': None}), cbc+'TaxableAmount__currencyID': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'BasisAmount', ram+'BasisAmount__currencyID': None}) or invoicecurrencycode})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CalculatedAmount
        # +/Invoice /TaxTotal /TaxSubtotal /TaxAmount
        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CalculatedAmount /CalculatedAmount__currencyID
        # +/Invoice /TaxTotal /TaxSubtotal /TaxAmount /TaxAmount__currencyID
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxAmount', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CalculatedAmount', 'BOTSCONTENT': None}), cbc+'TaxAmount__currencyID': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CalculatedAmount', ram+'CalculatedAmount__currencyID': None}) or invoicecurrencycode})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /ExemptionReason
        # +/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxExemptionReason
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'TaxExemptionReason', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'ExemptionReason', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CategoryCode
        # +/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxScheme /TaxTypeCode
        # taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'TaxTypeCode', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /ExemptionReasonCode
        # +/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxExemptionReasonCode
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'TaxExemptionReasonCode', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'ExemptionReasonCode', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /RateApplicablePercent
        # +/Invoice /TaxTotal /TaxSubtotal /TaxCategory /Percent
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /TypeCode
        # Fixed: 'VAT'
        # +/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxScheme /ID
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': None}) or 'VAT'})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /TaxPointDate /DateString
    # +/Invoice /TaxPointDate
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'TaxPointDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'TaxPointDate'}, {'BOTSID': udt+'DateString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /DueDateTypeCode
    # +/Invoice /InvoicePeriod /DescriptionCode
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'DescriptionCode', 'BOTSCONTENT': cii2475_to_ubl2005(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'DueDateTypeCode', 'BOTSCONTENT': None}))})

    for billingsperioddescription in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'Description'}):

        invoiceperioddescription = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'Description'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /BillingSpecifiedPeriod /Description
        # +/Invoice /InvoicePeriod /Description
        invoiceperioddescription.put({'BOTSID': cbc+'Description', 'BOTSCONTENT': billingsperioddescription.get({'BOTSID': ram+'Description', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /BillingSpecifiedPeriod /EndDateTime /DateTimeString
    # +/Invoice /InvoicePeriod /EndDate
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'EndDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'EndDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /BillingSpecifiedPeriod /StartDateTime /DateTimeString
    # +/Invoice /InvoicePeriod /StartDate
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'StartDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'StartDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceCurrencyCode
    # +/Invoice /DocumentCurrencyCode
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'DocumentCurrencyCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceCurrencyCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceReferencedDocument /FormattedIssueDateTime /DateTimeString
    # +/Invoice /BillingReference /InvoiceDocumentReference /IssueDate
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'BillingReference'}, {'BOTSID': cac+'InvoiceDocumentReference'}, {'BOTSID': cbc+'IssueDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceReferencedDocument'}, {'BOTSID': ram+'FormattedIssueDateTime'}, {'BOTSID': qdt+'DateTimeString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceReferencedDocument /IssuerAssignedID
    # +/Invoice /BillingReference /InvoiceDocumentReference /ID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'BillingReference'}, {'BOTSID': cac+'InvoiceDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    for payeetradepartyglobalid in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'GlobalID'}):

        payeepartyidentification = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyIdentification'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /GlobalID
        # +/Invoice /PayeeParty /PartyIdentification /ID
        payeepartyidentification.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': payeetradepartyglobalid.get({'BOTSID': ram+'GlobalID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /GlobalID /GlobalID__schemeID
        # +/Invoice /PayeeParty /PartyIdentification /ID /ID__schemeID
        payeepartyidentification.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID':payeetradepartyglobalid.get({'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': None})})

    for payeetradepartyid in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'ID'}):

        payeepartyidentification = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyIdentification'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /ID
        # +/Invoice /PayeeParty /PartyIdentification /ID
        payeepartyidentification.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': payeetradepartyid.get({'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /Name
    # +/Invoice /PayeeParty /PartyName /Name
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /SpecifiedLegalOrganization /ID
    # +/Invoice /PayeeParty /PartyLegalEntity /CompanyID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    # +/Invoice /PayeeParty /PartyLegalEntity /CompanyID /CompanyID__schemeID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ReceivableSpecifiedTradeAccountingAccount /ID
    # +/Invoice /AccountingCost
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'AccountingCost', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ReceivableSpecifiedTradeAccountingAccount'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    for specifiedtradeallowancecharge in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}):

        allowancecharge = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AllowanceCharge'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount
        # +/Invoice /AllowanceCharge /Amount
        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount /ActualAmount__currencyID
        # +/Invoice /AllowanceCharge /Amount /Amount__currencyID
        allowancecharge.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': specifiedtradeallowancecharge.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': None}), cbc+'Amount__currencyID': specifiedtradeallowancecharge.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', ram+'ActualAmount__currencyID': None}) or invoicecurrencycode})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount
        # +/Invoice /AllowanceCharge /BaseAmount
        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount /BasisAmount__currencyID
        # +/Invoice /AllowanceCharge /BaseAmount /BaseAmount__currencyID
        allowancecharge.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': specifiedtradeallowancecharge.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': None}), cbc+'BaseAmount__currencyID': specifiedtradeallowancecharge.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', ram+'BasisAmount__currencyID': None}) or invoicecurrencycode})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CalculationPercent
        # +/Invoice /AllowanceCharge /MultiplierFactorNumeric
        allowancecharge.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'MultiplierFactorNumeric', 'BOTSCONTENT': specifiedtradeallowancecharge.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CalculationPercent', 'BOTSCONTENT': None})})

        for categorytradetax in specifiedtradeallowancecharge.getloop({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CategoryTradeTax'}):

            taxcategory = allowancecharge.putloop({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cac+'TaxCategory'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /CategoryCode
            # +/Invoice /AllowanceCharge /TaxCategory /ID
            taxcategory.put({'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': categorytradetax.get({'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /RateApplicablePercent
            # +/Invoice /AllowanceCharge /TaxCategory /Percent
            taxcategory.put({'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': categorytradetax.get({'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /TypeCode
            # +/Invoice /AllowanceCharge /TaxCategory /TaxScheme /ID
            taxcategory.put({'BOTSID': cac+'TaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': categorytradetax.get({'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ChargeIndicator /Indicator
        # +/Invoice /AllowanceCharge /ChargeIndicator
        allowancecharge.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'ChargeIndicator', 'BOTSCONTENT': specifiedtradeallowancecharge.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ChargeIndicator'}, {'BOTSID': udt+'Indicator', 'BOTSCONTENT': None})})

        allowancechargereason = allowancecharge.putloop({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReason'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /Reason
        # +/Invoice /AllowanceCharge /AllowanceChargeReason
        allowancechargereason.put({'BOTSID': cbc+'AllowanceChargeReason', 'BOTSCONTENT': specifiedtradeallowancecharge.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'Reason', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ReasonCode
        # +/Invoice /AllowanceCharge /AllowanceChargeReasonCode
        allowancecharge.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReasonCode', 'BOTSCONTENT': specifiedtradeallowancecharge.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ReasonCode', 'BOTSCONTENT': None})})

    for specifiedtradepaymentterms in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradePaymentTerms'}):

        paymentterms = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PaymentTerms'})

        for description3 in specifiedtradepaymentterms.getloop({'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'Description'}):

            note2 = paymentterms.putloop({'BOTSID': cac+'PaymentTerms'}, {'BOTSID': cbc+'Note'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /Description
            # +/Invoice /PaymentTerms /Note
            note2.put({'BOTSID': cbc+'Note', 'BOTSCONTENT': description3.get({'BOTSID': ram+'Description', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /DueDateDateTime /DateTimeString
    duedate = transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'DueDateDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))
    if ubltype == 'Invoice':
        # + /Invoice /DueDate
        out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'DueDate', 'BOTSCONTENT': duedate})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /AllowanceTotalAmount
    # +/Invoice /LegalMonetaryTotal /AllowanceTotalAmount
    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /AllowanceTotalAmount /AllowanceTotalAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /AllowanceTotalAmount /AllowanceTotalAmount__currencyID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'AllowanceTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'AllowanceTotalAmount', 'BOTSCONTENT': None}), cbc+'AllowanceTotalAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'AllowanceTotalAmount', ram+'AllowanceTotalAmount__currencyID': None}) or invoicecurrencycode})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /ChargeTotalAmount
    # +/Invoice /LegalMonetaryTotal /ChargeTotalAmount
    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /ChargeTotalAmount /ChargeTotalAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /ChargeTotalAmount /ChargeTotalAmount__currencyID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'ChargeTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'ChargeTotalAmount', 'BOTSCONTENT': None}), cbc+'ChargeTotalAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'ChargeTotalAmount', ram+'ChargeTotalAmount__currencyID': None}) or invoicecurrencycode})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /DuePayableAmount
    # +/Invoice /LegalMonetaryTotal /PayableAmount
    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /DuePayableAmount /DuePayableAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /PayableAmount /PayableAmount__currencyID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'DuePayableAmount', 'BOTSCONTENT': None}), cbc+'PayableAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'DuePayableAmount', ram+'DuePayableAmount__currencyID': None}) or invoicecurrencycode})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /GrandTotalAmount
    # +/Invoice /LegalMonetaryTotal /TaxInclusiveAmount
    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /GrandTotalAmount /GrandTotalAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /TaxInclusiveAmount /TaxInclusiveAmount__currencyID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxInclusiveAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'GrandTotalAmount', 'BOTSCONTENT': None}), cbc+'TaxInclusiveAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'GrandTotalAmount', ram+'GrandTotalAmount__currencyID': None}) or invoicecurrencycode})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /LineTotalAmount
    # +/Invoice /LegalMonetaryTotal /LineExtensionAmount
    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /LineTotalAmount /LineTotalAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /LineExtensionAmount /LineExtensionAmount__currencyID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'LineExtensionAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', 'BOTSCONTENT': None}), cbc+'LineExtensionAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', ram+'LineTotalAmount__currencyID': None}) or invoicecurrencycode})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /RoundingAmount
    # +/Invoice /LegalMonetaryTotal /PayableRoundingAmount
    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /RoundingAmount /RoundingAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /PayableRoundingAmount /PayableRoundingAmount__currencyID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableRoundingAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'RoundingAmount', 'BOTSCONTENT': None}), cbc+'PayableRoundingAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'RoundingAmount', ram+'RoundingAmount__currencyID': None}) or invoicecurrencycode})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxBasisTotalAmount
    # +/Invoice /LegalMonetaryTotal /TaxExclusiveAmount
    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxBasisTotalAmount /TaxBasisTotalAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /TaxExclusiveAmount /TaxExclusiveAmount__currencyID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxExclusiveAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxBasisTotalAmount', 'BOTSCONTENT': None}), cbc+'TaxExclusiveAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxBasisTotalAmount', ram+'TaxBasisTotalAmount__currencyID': None}) or invoicecurrencycode})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TotalPrepaidAmount
    # +/Invoice /LegalMonetaryTotal /PrepaidAmount
    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TotalPrepaidAmount /TotalPrepaidAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /PrepaidAmount /PrepaidAmount__currencyID
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PrepaidAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TotalPrepaidAmount', 'BOTSCONTENT': None}), cbc+'PrepaidAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TotalPrepaidAmount', ram+'TotalPrepaidAmount__currencyID': None}) or invoicecurrencycode})

    for specifiedtradesettlementpaymentmeans in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}):

        paymentmeans = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PaymentMeans'})

        if ubltype == 'CreditNote' and duedate:
            # + /Invoice /PaymentMeans /PaymentDueDate
            paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentDueDate', 'BOTSCONTENT': duedate})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayerPartyDebtorFinancialAccount /IBANID
        # +/Invoice /PaymentMeans /PaymentMandate /PayerFinancialAccount /ID
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PaymentMandate'}, {'BOTSID': cac+'PayerFinancialAccount'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayerPartyDebtorFinancialAccount'}, {'BOTSID': ram+'IBANID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PaymentReference
        # +/Invoice /PaymentMeans /PaymentID
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PaymentReference', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /DirectDebitMandateID
        # +/Invoice /PaymentMeans /PaymentMandate /ID
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PaymentMandate'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'DirectDebitMandateID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /ApplicableTradeSettlementFinancialCard /CardholderName
        # +/Invoice /PaymentMeans /CardAccount /HolderName
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'CardAccount'}, {'BOTSID': cbc+'HolderName', 'BOTSCONTENT': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'ApplicableTradeSettlementFinancialCard'}, {'BOTSID': ram+'CardholderName', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /ApplicableTradeSettlementFinancialCard /ID
        # +/Invoice /PaymentMeans /CardAccount /PrimaryAccountNumberID
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'CardAccount'}, {'BOTSID': cbc+'PrimaryAccountNumberID', 'BOTSCONTENT': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'ApplicableTradeSettlementFinancialCard'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        if paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'CardAccount'}, {'BOTSID': cbc+'PrimaryAccountNumberID', 'BOTSCONTENT': None}):
            # +/Invoice /PaymentMeans /CardAccount /NetworkID
            # -/Invoice /PaymentMeans /CardAccount /PrimaryAccountNumberID (First digit)
            paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'CardAccount'}, {'BOTSID': cbc+'NetworkID', 'BOTSCONTENT': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'CardAccount'}, {'BOTSID': cbc+'PrimaryAccountNumberID', 'BOTSCONTENT': None})[0]})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode
        # +/Invoice /PaymentMeans /PaymentMeansCode
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', 'BOTSCONTENT': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode /TypeCode__listAgencyID
        # +/Invoice /PaymentMeans /PaymentMeansCode /PaymentMeansCode__listAgencyID
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', cbc+'PaymentMeansCode__listAgencyID': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', ram+'TypeCode__listAgencyID': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode /TypeCode__listID
        # +/Invoice /PaymentMeans /PaymentMeansCode /PaymentMeansCode__listID
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', cbc+'PaymentMeansCode__listID': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', ram+'TypeCode__listID': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode /TypeCode__listURI
        # +/Invoice /PaymentMeans /PaymentMeansCode /PaymentMeansCode__listURI
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', cbc+'PaymentMeansCode__listURI': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', ram+'TypeCode__listURI': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode /TypeCode__listVersionID
        # +/Invoice /PaymentMeans /PaymentMeansCode /PaymentMeansCode__listVersionID
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', cbc+'PaymentMeansCode__listVersionID': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', ram+'TypeCode__listVersionID': None})})

        name = ''
        for information in specifiedtradesettlementpaymentmeans.getloop({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'Information'}):
            name += information.get({'BOTSID': ram+'Information', 'BOTSCONTENT': None})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /Information
        # +/Invoice /PaymentMeans /PaymentMeansCode /PaymentMeansCode__name
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', cbc+'PaymentMeansCode__name': name or None})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayeePartyCreditorFinancialAccount /AccountName
        # +/Invoice /PaymentMeans /PayeeFinancialAccount /Name
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PayeeFinancialAccount'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayeePartyCreditorFinancialAccount'}, {'BOTSID': ram+'AccountName', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayeePartyCreditorFinancialAccount /IBANID
        ibanid = specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayeePartyCreditorFinancialAccount'}, {'BOTSID': ram+'IBANID', 'BOTSCONTENT': None})

        if not ibanid:
            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayeePartyCreditorFinancialAccount /ProprietaryID
            ibanid = specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayeePartyCreditorFinancialAccount'}, {'BOTSID': ram+'ProprietaryID', 'BOTSCONTENT': None})

        # +/Invoice /PaymentMeans /PayeeFinancialAccount /ID
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PayeeFinancialAccount'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': ibanid})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayeeSpecifiedCreditorFinancialInstitution /BICID
        # +/Invoice /PaymentMeans /PayeeFinancialAccount /FinancialInstitutionBranch /ID
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PayeeFinancialAccount'}, {'BOTSID': cac+'FinancialInstitutionBranch'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayeeSpecifiedCreditorFinancialInstitution'}, {'BOTSID': ram+'BICID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /TaxCurrencyCode
    # +/Invoice /TaxCurrencyCode
    out.put({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'TaxCurrencyCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'TaxCurrencyCode', 'BOTSCONTENT': None})})

    for includedsupplychaintradelineitem in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}):

        invoiceline = out.putloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+ubltype+'Line'})

        item = invoiceline.putloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Item'})

        for includednote2 in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'AssociatedDocumentLineDocument'}, {'BOTSID': ram+'IncludedNote'}):

            for content2 in includednote2.getloop({'BOTSID': ram+'IncludedNote'}, {'BOTSID': ram+'Content'}):

                note3 = invoiceline.putloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+'Note'})

                # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /AssociatedDocumentLineDocument /IncludedNote /Content
                # +/Invoice /InvoiceLine /Note
                note3.put({'BOTSID': cbc+'Note', 'BOTSCONTENT': content2.get({'BOTSID': ram+'Content', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /AssociatedDocumentLineDocument /LineID
        # +/Invoice /InvoiceLine /ID
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'AssociatedDocumentLineDocument'}, {'BOTSID': ram+'LineID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /BuyerOrderReferencedDocument /LineID
        # +/Invoice /InvoiceLine /OrderLineReference /LineID
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'OrderLineReference'}, {'BOTSID': cbc+'LineID', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'BuyerOrderReferencedDocument'}, {'BOTSID': ram+'LineID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /BasisQuantity
        # +/Invoice /InvoiceLine /Price /BaseQuantity
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /BasisQuantity /BasisQuantity__unitCode
        # +/Invoice /InvoiceLine /Price /BaseQuantity /BaseQuantity__unitCode
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', cbc+'BaseQuantity__unitCode': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', ram+'BasisQuantity__unitCode': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /ChargeAmount
        # +/Invoice /InvoiceLine /Price /PriceAmount
        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /ChargeAmount /ChargeAmount__currencyID
        # +/Invoice /InvoiceLine /Price /PriceAmount /PriceAmount__currencyID
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'PriceAmount', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', 'BOTSCONTENT': None}), cbc+'PriceAmount__currencyID': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', ram+'ChargeAmount__currencyID': None}) or invoicecurrencycode})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /BasisQuantity
        # +/Invoice /InvoiceLine /Price /BaseQuantity
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /BasisQuantity /BasisQuantity__unitCode
        # +/Invoice /InvoiceLine /Price /BaseQuantity /BaseQuantity__unitCode
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', cbc+'BaseQuantity__unitCode': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', ram+'BasisQuantity__unitCode': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /ChargeAmount
        chargeamount = includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', 'BOTSCONTENT': None})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /ChargeAmount /ChargeAmount__currencyID
        chargeamount__currencyid = includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', ram+'ChargeAmount__currencyID': None})

        allowancecharge2 = None

        for appliedtradeallowancecharge in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'AppliedTradeAllowanceCharge'}):

            allowancecharge2 = invoiceline.putloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cac+'AllowanceCharge'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ActualAmount
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /Amount
            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ActualAmount /ActualAmount__currencyID
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /Amount /Amount__currencyID
            allowancecharge2.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': appliedtradeallowancecharge.get({'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': None}), cbc+'Amount__currencyID': appliedtradeallowancecharge.get({'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', ram+'ActualAmount__currencyID': None}) or invoicecurrencycode})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ChargeIndicator /Indicator
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /ChargeIndicator
            allowancecharge2.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'ChargeIndicator', 'BOTSCONTENT': appliedtradeallowancecharge.get({'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ChargeIndicator'}, {'BOTSID': udt+'Indicator', 'BOTSCONTENT': None}) or 'false'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /ChargeAmount
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /BaseAmount
            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /ChargeAmount /ChargeAmount__currencyID
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /BaseAmount /BaseAmount__currencyID
            allowancecharge2.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': chargeamount, cbc+'BaseAmount__currencyID': chargeamount__currencyid or invoicecurrencycode})

        if not allowancecharge2 and chargeamount:
            allowancecharge2 = invoiceline.putloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cac+'AllowanceCharge'})

            # +/Invoice /InvoiceLine /Price /AllowanceCharge /Amount
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /Amount /Amount__currencyID
            allowancecharge2.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': '0', cbc+'Amount__currencyID': invoicecurrencycode})

            # +/Invoice /InvoiceLine /Price /AllowanceCharge /ChargeIndicator (false)
            allowancecharge2.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'ChargeIndicator', 'BOTSCONTENT': 'false'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /ChargeAmount
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /BaseAmount
            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /ChargeAmount /ChargeAmount__currencyID
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /BaseAmount /BaseAmount__currencyID
            allowancecharge2.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': chargeamount, cbc+'BaseAmount__currencyID': chargeamount__currencyid or invoicecurrencycode})

        # invoiceline_delivery = invoiceline.putloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Delivery'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeDelivery /ActualDeliverySupplyChainEvent /OccurrenceDateTime /DateTimeString
        # +/Invoice /InvoiceLine /Delivery /ActualDeliveryDate
        # invoiceline_delivery.put({'BOTSID': cac+'Delivery'}, {'BOTSID': cbc+'ActualDeliveryDate', 'BOTSCONTENT': transformdate(includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeDelivery'}, {'BOTSID': ram+'ActualDeliverySupplyChainEvent'}, {'BOTSID': ram+'OccurrenceDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

        qtytag = 'CreditedQuantity' if ubltype == 'CreditNote' else 'InvoicedQuantity'
        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeDelivery /BilledQuantity
        # +/Invoice /InvoiceLine /InvoicedQuantity
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+qtytag, 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeDelivery'}, {'BOTSID': ram+'BilledQuantity', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeDelivery /BilledQuantity /BilledQuantity__unitCode
        # +/Invoice /InvoiceLine /InvoicedQuantity /InvoicedQuantity__unitCode
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+qtytag, cbc+qtytag+'__unitCode': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeDelivery'}, {'BOTSID': ram+'BilledQuantity', ram+'BilledQuantity__unitCode': None})})

        for additionalreferenceddocument2 in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'AdditionalReferencedDocument'}):

            documentreference = invoiceline.putloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'DocumentReference'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /AdditionalReferencedDocument /IssuerAssignedID
            # +/Invoice /InvoiceLine /DocumentReference /ID
            documentreference.put({'BOTSID': cac+'DocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': additionalreferenceddocument2.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /AdditionalReferencedDocument /ReferenceTypeCode
            # +/Invoice /InvoiceLine /DocumentReference /ID /ID__schemeID
            documentreference.put({'BOTSID': cac+'DocumentReference'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': additionalreferenceddocument2.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'ReferenceTypeCode', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /AdditionalReferencedDocument /TypeCode
            # +/Invoice /InvoiceLine /DocumentReference /DocumentTypeCode
            documentreference.put({'BOTSID': cac+'DocumentReference'}, {'BOTSID': cbc+'DocumentTypeCode', 'BOTSCONTENT': additionalreferenceddocument2.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': None})})

        for applicabletradetax2 in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'}):

            classifiedtaxcategory = item.putloop({'BOTSID': cac+'Item'}, {'BOTSID': cac+'ClassifiedTaxCategory'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ApplicableTradeTax /CategoryCode
            # +/Invoice /InvoiceLine /Item /ClassifiedTaxCategory /ID
            classifiedtaxcategory.put({'BOTSID': cac+'ClassifiedTaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': applicabletradetax2.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ApplicableTradeTax /RateApplicablePercent
            # +/Invoice /InvoiceLine /Item /ClassifiedTaxCategory /Percent
            classifiedtaxcategory.put({'BOTSID': cac+'ClassifiedTaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': applicabletradetax2.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ApplicableTradeTax /TypeCode
            # +/Invoice /InvoiceLine /Item /ClassifiedTaxCategory /TaxScheme /ID
            classifiedtaxcategory.put({'BOTSID': cac+'ClassifiedTaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': applicabletradetax2.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /BillingSpecifiedPeriod /EndDateTime /DateTimeString
        # +/Invoice /InvoiceLine /InvoicePeriod /EndDate
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'EndDate', 'BOTSCONTENT': transformdate(includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'EndDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /BillingSpecifiedPeriod /StartDateTime /DateTimeString
        # +/Invoice /InvoiceLine /InvoicePeriod /StartDate
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'StartDate', 'BOTSCONTENT': transformdate(includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'StartDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

        for receivablespecifiedtradeaccountingaccount2 in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'ReceivableSpecifiedTradeAccountingAccount'}):

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ReceivableSpecifiedTradeAccountingAccount /ID
            # +/Invoice /InvoiceLine /AccountingCost
            invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+'AccountingCost', 'BOTSCONTENT': receivablespecifiedtradeaccountingaccount2.get({'BOTSID': ram+'ReceivableSpecifiedTradeAccountingAccount'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        for specifiedtradeallowancecharge2 in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}):

            allowancecharge3 = invoiceline.putloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'AllowanceCharge'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount
            # +/Invoice /InvoiceLine /AllowanceCharge /Amount
            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount /ActualAmount__currencyID
            # +/Invoice /InvoiceLine /AllowanceCharge /Amount /Amount__currencyID
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': None}), cbc+'Amount__currencyID': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', ram+'ActualAmount__currencyID': None}) or invoicecurrencycode})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount
            # +/Invoice /InvoiceLine /AllowanceCharge /BaseAmount
            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount /BasisAmount__currencyID
            # +/Invoice /InvoiceLine /AllowanceCharge /BaseAmount /BaseAmount__currencyID
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': None}), cbc+'BaseAmount__currencyID': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', ram+'BasisAmount__currencyID': None}) or invoicecurrencycode})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /CalculationPercent
            # +/Invoice /InvoiceLine /AllowanceCharge /MultiplierFactorNumeric
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'MultiplierFactorNumeric', 'BOTSCONTENT': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CalculationPercent', 'BOTSCONTENT': None})})

            for categorytradetax2 in specifiedtradeallowancecharge2.getloop({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CategoryTradeTax'}):

                taxcategory2 = allowancecharge3.putloop({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cac+'TaxCategory'})

                # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /CategoryCode
                # +/Invoice /InvoiceLine /AllowanceCharge /TaxCategory /ID
                taxcategory2.put({'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': categorytradetax2.get({'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': None})})

                # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /RateApplicablePercent
                # +/Invoice /InvoiceLine /AllowanceCharge /TaxCategory /Percent
                taxcategory2.put({'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': categorytradetax2.get({'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ChargeIndicator /Indicator
            # +/Invoice /InvoiceLine /AllowanceCharge /ChargeIndicator
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'ChargeIndicator', 'BOTSCONTENT': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ChargeIndicator'}, {'BOTSID': udt+'Indicator', 'BOTSCONTENT': None}) or 'false'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /Reason
            # +/Invoice /InvoiceLine /AllowanceCharge /AllowanceChargeReason
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReason', 'BOTSCONTENT': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'Reason', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ReasonCode
            # +/Invoice /InvoiceLine /AllowanceCharge /AllowanceChargeReasonCode
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReasonCode', 'BOTSCONTENT': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ReasonCode', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeSettlementLineMonetarySummation /LineTotalAmount
        # +/Invoice /InvoiceLine /LineExtensionAmount
        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeSettlementLineMonetarySummation /LineTotalAmount /LineTotalAmount__currencyID
        # +/Invoice /InvoiceLine /LineExtensionAmount /LineExtensionAmount__currencyID
        invoiceline.put({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+'LineExtensionAmount', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementLineMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', 'BOTSCONTENT': None}), cbc+'LineExtensionAmount__currencyID': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementLineMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', ram+'LineTotalAmount__currencyID': None}) or invoicecurrencycode})

        for applicableproductcharacteristic in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'ApplicableProductCharacteristic'}):
            additionalitemproperty = item.putloop({'BOTSID': cac+'Item'}, {'BOTSID': cac+'AdditionalItemProperty'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /ApplicableProductCharacteristic /Description
            # +/Invoice /InvoiceLine /Item /AdditionalItemProperty /Name
            additionalitemproperty.put({'BOTSID': cac+'AdditionalItemProperty'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': applicableproductcharacteristic.get({'BOTSID': ram+'ApplicableProductCharacteristic'}, {'BOTSID': ram+'Description', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /ApplicableProductCharacteristic /Value
            # +/Invoice /InvoiceLine /Item /AdditionalItemProperty /Value
            additionalitemproperty.put({'BOTSID': cac+'AdditionalItemProperty'}, {'BOTSID': cbc+'Value', 'BOTSCONTENT': applicableproductcharacteristic.get({'BOTSID': ram+'ApplicableProductCharacteristic'}, {'BOTSID': ram+'Value', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /BuyerAssignedID
        # +/Invoice /InvoiceLine /Item /BuyersItemIdentification /ID
        item.put({'BOTSID': cac+'Item'}, {'BOTSID': cac+'BuyersItemIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'BuyerAssignedID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /Description
        # +/Invoice /InvoiceLine /Item /Description
        item.put({'BOTSID': cac+'Item'}, {'BOTSID': cbc+'Description', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'Description', 'BOTSCONTENT': None})})

        for designatedproductclassification in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'DesignatedProductClassification'}):

            commodityclassification = item.putloop({'BOTSID': cac+'Item'}, {'BOTSID': cac+'CommodityClassification'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /DesignatedProductClassification /ClassCode
            # +/Invoice /InvoiceLine /Item /CommodityClassification /ItemClassificationCode
            commodityclassification.put({'BOTSID': cac+'CommodityClassification'}, {'BOTSID': cbc+'ItemClassificationCode', 'BOTSCONTENT': designatedproductclassification.get({'BOTSID': ram+'DesignatedProductClassification'}, {'BOTSID': ram+'ClassCode', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /DesignatedProductClassification /ClassCode /ClassCode__listID
            # +/Invoice /InvoiceLine /Item /CommodityClassification /ItemClassificationCode /ItemClassificationCode__listID
            commodityclassification.put({'BOTSID': cac+'CommodityClassification'}, {'BOTSID': cbc+'ItemClassificationCode', cbc+'ItemClassificationCode__listID': designatedproductclassification.get({'BOTSID': ram+'DesignatedProductClassification'}, {'BOTSID': ram+'ClassCode', ram+'ClassCode__listID': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /DesignatedProductClassification /ClassCode /ClassCode__listVersionID
            # +/Invoice /InvoiceLine /Item /CommodityClassification /ItemClassificationCode /ItemClassificationCode__listVersionID
            commodityclassification.put({'BOTSID': cac+'CommodityClassification'}, {'BOTSID': cbc+'ItemClassificationCode', cbc+'ItemClassificationCode__listVersionID': designatedproductclassification.get({'BOTSID': ram+'DesignatedProductClassification'}, {'BOTSID': ram+'ClassCode', ram+'ClassCode__listVersionID': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /GlobalID
        # +/Invoice /InvoiceLine /Item /StandardItemIdentification /ID
        item.put({'BOTSID': cac+'Item'}, {'BOTSID': cac+'StandardItemIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'GlobalID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /GlobalID /GlobalID__schemeID
        # +/Invoice /InvoiceLine /Item /StandardItemIdentification /ID /ID__schemeID
        item.put({'BOTSID': cac+'Item'}, {'BOTSID': cac+'StandardItemIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /Name
        # +/Invoice /InvoiceLine /Item /Name
        item.put({'BOTSID': cac+'Item'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /OriginTradeCountry /ID
        # +/Invoice /InvoiceLine /Item /OriginCountry /IdentificationCode
        item.put({'BOTSID': cac+'Item'}, {'BOTSID': cac+'OriginCountry'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'OriginTradeCountry'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /SellerAssignedID
        # +/Invoice /InvoiceLine /Item /SellersItemIdentification /ID
        item.put({'BOTSID': cac+'Item'}, {'BOTSID': cac+'SellersItemIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'SellerAssignedID', 'BOTSCONTENT': None})})
