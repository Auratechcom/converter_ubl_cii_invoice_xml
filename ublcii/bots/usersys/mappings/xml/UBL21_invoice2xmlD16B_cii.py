# -*- coding: utf-8 -*-
"""
bots-mapping-script
Message: xml/UBL21_INVOICE > xml/D16B_CII
Author: Ludovic Watteaux
"""
from __future__ import unicode_literals, division

from string import ascii_uppercase
from bots import transform
from bots.grammar import grammarread


CURRENCY_CODE = 'EUR'


def get_grammar(msg):
    args = [msg.ta_info['editype'], msg.ta_info['messagetype']]
    if grammarread.__code__.co_argcount > 2:
        args.append('grammars')
    return grammarread(*args)


UBL2005_TO_CII2475 = {
    '3': '5',
    '35': '29',
    '432': '72',
}


def ubl2005_to_cii2475(code):
    return UBL2005_TO_CII2475.get(code, code)


def isiban(iban):
    try:
        iban = iban.strip().replace(' ', '').replace('-', '').upper()
        key = ''
        for char in '%s%s' % (iban[4:], iban[:4]):
            idx = ascii_uppercase.find(char)
            if idx > -1:
                key += str(10 + idx)
            else:
                key += char
        return int(key) % 97 == 1
    except:
        return False


def transformdate(datestr):
    return transform.datemask(datestr, 'CCYY-MM-DD', 'CCYYMMDD')


def setcurrency(currency):
    if currency and currency != CURRENCY_CODE:
        return currency
    return None


def main(inn, out):

    # IN Message: xml/UBL21_INVOICE
    xmlns = inn.ta_info['xmlns']
    cbc = inn.ta_info['cbc']
    cac = inn.ta_info['cac']
    ext = inn.ta_info['ext']
    # Ubl type: Invoice or CreditNote
    ubltype = inn.ta_info['ubltype']

    # OUT Message: xml/D16B_CII
    out_syntax = get_grammar(out).syntax
    rsm = out_syntax['rsm']
    qdt = out_syntax['qdt']
    udt = out_syntax['udt']
    ram = out_syntax['ram']
    dtf = out_syntax['datetime_format']

    out.ta_info['reference'] = inn.ta_info['reference']

    out.put({'BOTSID': rsm+'CrossIndustryInvoice', rsm+'CrossIndustryInvoice__xmlns:xsi': out_syntax['xsi'].strip('{}')})

    # -/Invoice /ID
    # +/CrossIndustryInvoice /ExchangedDocument /ID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    for note in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'Note'}):

        includednote = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'IncludedNote'})

        # -/Invoice /Note
        notecontent = note.get({'BOTSID': cbc+'Note', 'BOTSCONTENT': None})
        if notecontent and notecontent.lstrip(' ').startswith('#'):
            terug = notecontent.split('#')
            if len(terug) > 2:
                # +/CrossIndustryInvoice /ExchangedDocument /IncludedNote /SubjectCode
                includednote.put({'BOTSID': ram+'IncludedNote'}, {'BOTSID': ram+'SubjectCode', 'BOTSCONTENT': terug[1]})
                notecontent = '#'.join(terug[2:])

        # -/Invoice /Note
        # +/CrossIndustryInvoice /ExchangedDocument /IncludedNote /Content
        includednote.put({'BOTSID': ram+'IncludedNote'}, {'BOTSID': ram+'Content', 'BOTSCONTENT': notecontent})

    # -/Invoice /IssueDate
    # +/CrossIndustryInvoice /ExchangedDocument /IssueDateTime /DateTimeString
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'IssueDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': dtf, 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'IssueDate', 'BOTSCONTENT': None}))})

    # -/Invoice /InvoiceTypeCode
    # +/CrossIndustryInvoice /ExchangedDocument /TypeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+ubltype+'TypeCode', 'BOTSCONTENT': None})})

    # +/CrossIndustryInvoice /ExchangedDocumentContext
    exchangeddocumentcontext = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocumentContext'})

    # +/CrossIndustryInvoice /ExchangedDocumentContext /TestIndicator /Indicator
    # exchangeddocumentcontext.put({'BOTSID': rsm+'ExchangedDocumentContext'}, {'BOTSID': ram+'TestIndicator'}, {'BOTSID': udt+'Indicator', 'BOTSCONTENT': 'False'})

    # -/Invoice /ProfileID
    # or
    # -/Invoice /UBLExtensions /UBLExtension /ExtensionContent /CategoryCode
    # +/CrossIndustryInvoice /ExchangedDocumentContext /BusinessProcessSpecifiedDocumentContextParameter /ID
    exchangeddocumentcontext.put({'BOTSID': rsm+'ExchangedDocumentContext'}, {'BOTSID': ram+'BusinessProcessSpecifiedDocumentContextParameter'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'ProfileID', 'BOTSCONTENT': None}) or inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': ext+'UBLExtensions'}, {'BOTSID': ext+'UBLExtension'}, {'BOTSID': ext+'ExtensionContent'}, {'BOTSID': xmlns+'CategoryCode', 'BOTSCONTENT': None})})

    # -/Invoice /CustomizationID
    # +/CrossIndustryInvoice /ExchangedDocumentContext /GuidelineSpecifiedDocumentContextParameter /ID
    exchangeddocumentcontext.put({'BOTSID': rsm+'ExchangedDocumentContext'}, {'BOTSID': ram+'GuidelineSpecifiedDocumentContextParameter'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'CustomizationID', 'BOTSCONTENT': None})})

    # -/Invoice /DocumentCurrencyCode
    # invoicecurrencycode
    globals()['CURRENCY_CODE'] = inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'DocumentCurrencyCode', 'BOTSCONTENT': None}) or CURRENCY_CODE

    for originatordocumentreference in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'OriginatorDocumentReference'}):

        # -/Invoice /OriginatorDocumentReference /ID
        originatordocumentreferenceid = originatordocumentreference.get({'BOTSID': cac+'OriginatorDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})

        if originatordocumentreferenceid:

            additionalreferenceddocument = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'AdditionalReferencedDocument'})

            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /IssuerAssignedID
            # -/Invoice /OriginatorDocumentReference /ID
            additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': originatordocumentreferenceid})

            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /TypeCode
            # Fixed: '50'
            additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': '50'})

    projectreferenceid = None

    for additionaldocumentreference in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AdditionalDocumentReference'}):

        documenttypecode = additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'DocumentTypeCode', 'BOTSCONTENT': None})
        if documenttypecode == '50':
            # - /Invoice /AdditionalDocumentReference /ID
            projectreferenceid = additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})
            continue

        additionalreferenceddocument = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'AdditionalReferencedDocument'})

        """
        # This cause CII error [CII-DT-022] - AttachmentBinaryObject should not be present
        # -/Invoice /AdditionalDocumentReference /Attachment /EmbeddedDocumentBinaryObject
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /AttachmentBinaryObject
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'AttachmentBinaryObject', 'BOTSCONTENT': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cbc+'EmbeddedDocumentBinaryObject', 'BOTSCONTENT': None})})

        # -/Invoice /AdditionalDocumentReference /Attachment /EmbeddedDocumentBinaryObject /EmbeddedDocumentBinaryObject__filename
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /AttachmentBinaryObject /AttachmentBinaryObject__filename
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'AttachmentBinaryObject', ram+'AttachmentBinaryObject__filename': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cbc+'EmbeddedDocumentBinaryObject', cbc+'EmbeddedDocumentBinaryObject__filename': None})})

        # -/Invoice /AdditionalDocumentReference /Attachment /EmbeddedDocumentBinaryObject /EmbeddedDocumentBinaryObject__mimeCode
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /AttachmentBinaryObject /AttachmentBinaryObject__mimeCode
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'AttachmentBinaryObject', ram+'AttachmentBinaryObject__mimeCode': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cbc+'EmbeddedDocumentBinaryObject', cbc+'EmbeddedDocumentBinaryObject__mimeCode': None})})
        """

        # -/Invoice /AdditionalDocumentReference /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /IssuerAssignedID
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /AdditionalDocumentReference /ID /ID__schemeID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /ReferenceTypeCode
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'ReferenceTypeCode', 'BOTSCONTENT': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})})

        # ! Warning old validation caused [CII-DT-021] - Name should not be present
        additionaldocumentdescription = None
        for documentdescription in additionaldocumentreference.getloop({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'DocumentDescription'}):

            name = additionalreferenceddocument.putloop({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'Name'})

            # -/Invoice /AdditionalDocumentReference /DocumentDescription
            additionaldocumentdescription = documentdescription.get({'BOTSID': cbc+'DocumentDescription', 'BOTSCONTENT': None})
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /Name
            name.put({'BOTSID': ram+'Name', 'BOTSCONTENT': additionaldocumentdescription})

        # -/Invoice /AdditionalDocumentReference /Attachment /ExternalReference /URI
        externalreferenceuri = additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cac+'ExternalReference'}, {'BOTSID': cbc+'URI', 'BOTSCONTENT': None})
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /URIID
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': externalreferenceuri})

        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /TypeCode
        if additionaldocumentdescription or externalreferenceuri:
            # Fixed: '916'
            additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': '916'})
        else:
            # -/Invoice /AdditionalDocumentReference /DocumentTypeCode
            additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'DocumentTypeCode', 'BOTSCONTENT': None})})

    # -/Invoice /OrderReference /ID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerOrderReferencedDocument /IssuerAssignedID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerOrderReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'OrderReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    # -/Invoice /BuyerReference
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerReference
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerReference', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'BuyerReference', 'BOTSCONTENT': None})})


    # -/Invoice /AccountingCustomerParty /Party /Contact /Name
    customercontactname = inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})

    if customercontactname:
        if '(' in customercontactname:
            customercontactdpt = customercontactname[customercontactname.index('(')+1:customercontactname.index(')')]
            customercontactname = customercontactname[:customercontactname.index('(')]
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /DepartmentName
            out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'DepartmentName', 'BOTSCONTENT': customercontactdpt})

        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /PersonName
        out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'PersonName', 'BOTSCONTENT': customercontactname})

    # -/Invoice /AccountingCustomerParty /Party /Contact /ElectronicMail
    customercontactemail = inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'ElectronicMail', 'BOTSCONTENT': None})

    if customercontactemail:
        # -/Invoice /AccountingCustomerParty /Party /Contact /ElectronicMail
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /EmailURIUniversalCommunication /URIID
        out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'EmailURIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': customercontactemail})

    # -/Invoice /AccountingCustomerParty /Party /Contact /Telefax
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /FaxUniversalCommunication /CompleteNumber
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'FaxUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Telefax', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /Contact /Telephone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /TelephoneUniversalCommunication /CompleteNumber
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'TelephoneUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Telephone', 'BOTSCONTENT': None})})

    for partylegalentity in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}):

        customerlegalform = partylegalentity.get({'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyLegalForm', 'BOTSCONTENT': None})
        if customerlegalform:
            description = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'Description'})

            # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyLegalForm
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /Description
            description.put({'BOTSID': ram+'Description', 'BOTSCONTENT': customerlegalform})


    for customerpartyidentification in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'}):

        # -/Invoice /AccountingCustomerParty /Party /PartyIdentification /ID
        customerpartyid = customerpartyidentification.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})

        # -/Invoice /AccountingCustomerParty /Party /PartyIdentification /ID /ID__schemeID
        customerpartyschemeid = customerpartyidentification.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})

        if not customerpartyid:
            continue
        if not customerpartyschemeid:
            buyertradepartyid = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'ID'})

            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /ID
            buyertradepartyid.put({'BOTSID': ram+'ID', 'BOTSCONTENT': customerpartyid})
            continue

        buyertradepartyglobalid = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'GlobalID'})

        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /GlobalID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /GlobalID /GlobalID__schemeID
        buyertradepartyglobalid.put({'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': customerpartyschemeid, 'BOTSCONTENT': customerpartyid})


    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /Name
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'RegistrationName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CityName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountryID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /Country /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountryName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /CountrySubentity
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountrySubDivisionName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineOne
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineThree
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineTwo
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /PostcodeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /ID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyID /CompanyID__schemeID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CityName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /Country /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /CountrySubentity
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountrySubDivisionName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineOne
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineThree
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineTwo
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /PostcodeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyName /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /EndpointID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /URIUniversalCommunication /URIID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /EndpointID /EndpointID__schemeID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /URIUniversalCommunication /URIID /URIID__schemeID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', ram+'URIID__schemeID': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', cbc+'EndpointID__schemeID': None})})

    for contractdocumentreference in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'ContractDocumentReference'}):

        # -/Invoice /ContractDocumentReference /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /ContractReferencedDocument /IssuerAssignedID
        out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'ContractReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': contractdocumentreference.get({'BOTSID': cac+'ContractDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /ContractDocumentReference /DocumentTypeCode
        documenttypecode = contractdocumentreference.get({'BOTSID': cac+'ContractDocumentReference'}, {'BOTSID': cbc+'DocumentTypeCode', 'BOTSCONTENT': None})

        referencetypecode = None

        if documenttypecode == 'Contrat':
            referencetypecode = 'CT'
        elif documenttypecode in ['Bon de commande', 'Marché Public']:
            referencetypecode = 'BC'

        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /ContractReferencedDocument /ReferenceTypeCode
        out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'ContractReferencedDocument'}, {'BOTSID': ram+'ReferenceTypeCode', 'BOTSCONTENT': referencetypecode})

    # -/Invoice /OrderReference /SalesOrderID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerOrderReferencedDocument /IssuerAssignedID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerOrderReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'OrderReference'}, {'BOTSID': cbc+'SalesOrderID', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PartyName /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /Name
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CityName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CountryID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /CountrySubentity
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CountrySubDivisionName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineOne
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineThree
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineTwo
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /PostcodeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    for partytaxscheme in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PartyTaxScheme'}):

        specifiedtaxregistration = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'})

        # -/Invoice /TaxRepresentativeParty /PartyTaxScheme /CompanyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /SpecifiedTaxRegistration /ID
        specifiedtaxregistration.put({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': partytaxscheme.get({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /SpecifiedTaxRegistration /ID /ID__schemeID
        # Fixed: 'VA'
        specifiedtaxregistration.put({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': 'VA'})

    # -/Invoice /AccountingSupplierParty /Party /Contact /ElectronicMail
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /EmailURIUniversalCommunication /URIID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'EmailURIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'ElectronicMail', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /Contact /Telefax
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /FaxUniversalCommunication /CompleteNumber
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'FaxUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Telefax', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /Contact /Name
    suppliercontactname = inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})

    if suppliercontactname:
        if '(' in suppliercontactname:
            suppliercontactdpt = suppliercontactname[suppliercontactname.index('(')+1:suppliercontactname.index(')')]
            suppliercontactname = suppliercontactname[:suppliercontactname.index('(')]

            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /DepartmentName
            out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'DepartmentName', 'BOTSCONTENT': suppliercontactdpt})

        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /PersonName
        out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'PersonName', 'BOTSCONTENT': suppliercontactname})

    # -/Invoice /AccountingSupplierParty /Party /Contact /Telephone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /TelephoneUniversalCommunication /CompleteNumber
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'TelephoneUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'Contact'}, {'BOTSID': cbc+'Telephone', 'BOTSCONTENT': None})})

    for partylegalentity2 in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}):

        supplierlegalform = partylegalentity2.get({'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyLegalForm', 'BOTSCONTENT': None})
        if supplierlegalform:
            description2 = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'Description'})

            # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyLegalForm
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /Description
            description2.put({'BOTSID': ram+'Description', 'BOTSCONTENT': supplierlegalform})

    # -/Invoice /AccountingSupplierParty /Party /EndpointID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /URIUniversalCommunication /URIID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /EndpointID /EndpointID__schemeID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /URIUniversalCommunication /URIID /URIID__schemeID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', ram+'URIID__schemeID': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', cbc+'EndpointID__schemeID': None})})


    for supplierpartyidentification in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'}):

        # -/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID
        supplierpartyid = supplierpartyidentification.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})

        # -/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID /ID__schemeID
        supplierpartyschemeid = supplierpartyidentification.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})

        if not supplierpartyid:
            continue
        if not supplierpartyschemeid:
            sellertradepartyid = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'ID'})

            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /ID
            sellertradepartyid.put({'BOTSID': ram+'ID', 'BOTSCONTENT': supplierpartyid})
            continue

        if supplierpartyschemeid == 'SEPA':
            continue

        sellertradepartyglobalid = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'GlobalID'})

        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /GlobalID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /GlobalID /GlobalID__schemeID
        sellertradepartyglobalid.put({'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': supplierpartyschemeid, 'BOTSCONTENT': supplierpartyid})


    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /Name
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'RegistrationName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CityName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountryID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /Country /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountryName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /CountrySubentity
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountrySubDivisionName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineOne
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineThree
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineTwo
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /PostcodeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /ID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyID /CompanyID__schemeID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CityName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /Country /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /CountrySubentity
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountrySubDivisionName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineOne
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineThree
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineTwo
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /PostcodeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyName /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    for supplierpartytaxscheme in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyTaxScheme'}):

        sellertaxregistration = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'})

        # -/Invoice /AccountingSupplierParty /Party /PartyTaxScheme /CompanyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedTaxRegistration /ID
        sellertaxregistration.put({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': supplierpartytaxscheme.get({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedTaxRegistration /ID /ID__schemeID
        # Fixed 'VA'
        sellertaxregistration.put({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': 'VA'})

    for customertaxscheme in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyTaxScheme'}):

        buyertaxregistration = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'})

        # -/Invoice /AccountingCustomerParty /Party /PartyTaxScheme /CompanyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedTaxRegistration /ID
        buyertaxregistration.put({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': customertaxscheme.get({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedTaxRegistration /ID /ID__schemeID
        # Fixed:'VA'
        buyertaxregistration.put({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': 'VA'})

    if ubltype == 'Invoice':
        # - /Invoice /ProjectReference /ID
        projectreferenceid = inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'ProjectReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})

    if projectreferenceid:
        # + /CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SpecifiedProcuringProject /ID
        # - /Invoice /ProjectReference /ID
        # - /CreditNote /AdditionalDocumentReference /ID
        out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SpecifiedProcuringProject'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': projectreferenceid})

        # + /CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SpecifiedProcuringProject /Name
        # - Fixed: 'Project reference'
        out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SpecifiedProcuringProject'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': 'Project reference'})


    applicableheadertradedelivery = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'})

    # -/Invoice /Delivery /ActualDeliveryDate
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ActualDeliverySupplyChainEvent /OccurrenceDateTime /DateTimeString
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ActualDeliverySupplyChainEvent'}, {'BOTSID': ram+'OccurrenceDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': dtf, 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cbc+'ActualDeliveryDate', 'BOTSCONTENT': None}))})

    # -/Invoice /DespatchDocumentReference /ID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /DespatchAdviceReferencedDocument /IssuerAssignedID
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'DespatchAdviceReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'DespatchDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    # -/Invoice /ReceiptDocumentReference /ID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ReceivingAdviceReferencedDocument /IssuerAssignedID
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ReceivingAdviceReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'ReceiptDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    for delivery in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}):

        for deliverydescription in delivery.getloop({'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'Description'}):

            shiptotradepartydescription = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'Description'})

            # -/Invoice /Delivery /DeliveryLocation /Description
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /Description
            shiptotradepartydescription.put({'BOTSID': ram+'Description', 'BOTSCONTENT': deliverydescription.get({'BOTSID': cbc+'Description', 'BOTSCONTENT': None})})

        # -/Invoice /Delivery /DeliveryLocation /ID
        deliverylocid = delivery.get({'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})

        # -/Invoice /Delivery /DeliveryLocation /ID /ID__schemeID
        deliveryschemeid = delivery.get({'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})

        if deliverylocid and deliveryschemeid:
            shiptotradepartyglobalid = applicableheadertradedelivery.putloop({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'GlobalID'})

            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /GlobalID
            shiptotradepartyglobalid.put({'BOTSID': ram+'GlobalID', 'BOTSCONTENT': deliverylocid})

            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /GlobalID /GlobalID__schemeID
            shiptotradepartyglobalid.put({'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': deliveryschemeid})

        elif deliverylocid:
            shiptotradepartyid = applicableheadertradedelivery.putloop({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'ID'})

            # -/Invoice /Delivery /DeliveryLocation /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /ID
            shiptotradepartyid.put({'BOTSID': ram+'ID', 'BOTSCONTENT': deliverylocid})

        # -/Invoice /Delivery /DeliveryLocation /Address /CountrySubentity
        countrysubentity = delivery.get({'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})

        if countrysubentity:
            countrysubdivisionname4 = applicableheadertradedelivery.putloop({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName'})

            # -/Invoice /Delivery /DeliveryLocation /Address /CountrySubentity
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CountrySubDivisionName
            countrysubdivisionname4.put({'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': countrysubentity})

    # -/Invoice /Delivery /DeliveryParty /PartyName /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /Name
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CityName
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CountryID
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineOne
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineThree
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineTwo
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /PostcodeCode
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    # -/Invoice /TaxCurrencyCode
    taxcurrencycode = setcurrency(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'TaxCurrencyCode', 'BOTSCONTENT': None}))
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /TaxCurrencyCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'TaxCurrencyCode', 'BOTSCONTENT': taxcurrencycode})

    for taxtotal in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'TaxTotal'}):

        # BT-110
        # Validation to pass EN16931-CII-validation.xslt#182
        # taxamount_currencyid = taxcurrencycode or CURRENCY_CODE

        # -/Invoice /TaxTotal /TaxAmount
        taxamount = taxtotal.get({'BOTSID': cac+'TaxTotal'}, {'BOTSID': cbc+'TaxAmount', 'BOTSCONTENT': None})

        if taxamount:

            taxtotalamount = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxTotalAmount'})

            # -/Invoice /TaxTotal /TaxAmount
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxTotalAmount
            taxtotalamount.put({'BOTSID': ram+'TaxTotalAmount', 'BOTSCONTENT': taxamount})

            # -/Invoice /TaxTotal /TaxAmount /TaxAmount__currencyID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxTotalAmount /TaxTotalAmount__currencyID
            # BT-110: Keep currencyID here
            taxtotalamount.put({'BOTSID': ram+'TaxTotalAmount', ram+'TaxTotalAmount__currencyID': taxtotal.get({'BOTSID': cac+'TaxTotal'}, {'BOTSID': cbc+'TaxAmount', cbc+'TaxAmount__currencyID': None})})

        for taxsubtotal in taxtotal.getloop({'BOTSID': cac+'TaxTotal'}, {'BOTSID': cac+'TaxSubtotal'}):
            
            applicabletradetax = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxableAmount
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /BasisAmount
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxableAmount', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxableAmount /TaxableAmount__currencyID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /BasisAmount /BasisAmount__currencyID
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'BasisAmount', ram+'BasisAmount__currencyID': setcurrency(taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxableAmount', cbc+'TaxableAmount__currencyID': None}))})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxAmount
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CalculatedAmount
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CalculatedAmount', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxAmount', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxAmount /TaxAmount__currencyID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CalculatedAmount /CalculatedAmount__currencyID
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CalculatedAmount', ram+'CalculatedAmount__currencyID': setcurrency(taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxAmount', cbc+'TaxAmount__currencyID': None}))})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxScheme /TaxTypeCode
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CategoryCode
            # applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'TaxTypeCode', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxExemptionReason
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /ExemptionReason
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'ExemptionReason', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'TaxExemptionReason', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxExemptionReasonCode
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /ExemptionReasonCode
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'ExemptionReasonCode', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'TaxExemptionReasonCode', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxCategory /Percent
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /RateApplicablePercent
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxScheme /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /TypeCode
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None}) or 'VAT'})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxCategory /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CategoryCode
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

            # -/Invoice /TaxPointDate
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /TaxPointDate /DateString
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'TaxPointDate'}, {'BOTSID': udt+'DateString', udt+'DateString__format': dtf, 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'TaxPointDate', 'BOTSCONTENT': None}))})

            # -/Invoice /InvoicePeriod /DescriptionCode
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /DueDateTypeCode
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'DueDateTypeCode', 'BOTSCONTENT': ubl2005_to_cii2475(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'DescriptionCode', 'BOTSCONTENT': None}))})

    for invoiceperioddescription in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'Description'}):

        billingsperioddescription = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'Description'})

        # -/Invoice /InvoicePeriod /Description
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /BillingSpecifiedPeriod /Description
        billingsperioddescription.put({'BOTSID': ram+'Description', 'BOTSCONTENT': invoiceperioddescription.get({'BOTSID': cbc+'Description', 'BOTSCONTENT': None})})

    # -/Invoice /InvoicePeriod /EndDate
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /BillingSpecifiedPeriod /EndDateTime /DateTimeString
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'EndDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': dtf, 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'EndDate', 'BOTSCONTENT': None}))})

    # -/Invoice /InvoicePeriod /StartDate
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /BillingSpecifiedPeriod /StartDateTime /DateTimeString
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'StartDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': dtf, 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'StartDate', 'BOTSCONTENT': None}))})

    # -/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID
    # with: 'ID__SchemeID': 'SEPA''
    creditorreferenceid = inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': 'SEPA', 'BOTSCONTENT': None})
    if not creditorreferenceid:
        # -/Invoice /PayeeParty /PartyIdentification /ID
        creditorreferenceid = inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': 'SEPA', 'BOTSCONTENT': None})

    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /CreditorReferenceID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'CreditorReferenceID', 'BOTSCONTENT': creditorreferenceid})

    # -/Invoice /DocumentCurrencyCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceCurrencyCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceCurrencyCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'DocumentCurrencyCode', 'BOTSCONTENT': None})})

    # -/Invoice /BillingReference /InvoiceDocumentReference /IssueDate
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceReferencedDocument /FormattedIssueDateTime /DateTimeString
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceReferencedDocument'}, {'BOTSID': ram+'FormattedIssueDateTime'}, {'BOTSID': qdt+'DateTimeString', qdt+'DateTimeString__format': dtf, 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'BillingReference'}, {'BOTSID': cac+'InvoiceDocumentReference'}, {'BOTSID': cbc+'IssueDate', 'BOTSCONTENT': None}))})

    # -/Invoice /BillingReference /InvoiceDocumentReference /ID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceReferencedDocument /IssuerAssignedID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'BillingReference'}, {'BOTSID': cac+'InvoiceDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    for payeepartyidentification in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyIdentification'}):

        # -/Invoice /PayeeParty /PartyIdentification /ID
        payeepartyid = payeepartyidentification.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})

        # -/Invoice /PayeeParty /PartyIdentification /ID /ID__schemeID
        payeepartyschemeid = payeepartyidentification.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})

        if not payeepartyid:
            continue

        if not payeepartyschemeid:

            payeetradepartyid = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'ID'})

            # -/Invoice /PayeeParty /PartyIdentification /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /ID
            payeetradepartyid.put({'BOTSID': ram+'ID', 'BOTSCONTENT': payeepartyid})
            continue

        if payeepartyschemeid == 'SEPA':
            continue

        payeetradepartyglobalid = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'GlobalID'})

        # -/Invoice /PayeeParty /PartyIdentification /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /GlobalID
        payeetradepartyglobalid.put({'BOTSID': ram+'GlobalID', 'BOTSCONTENT': payeepartyid})

        # -/Invoice /PayeeParty /PartyIdentification /ID /ID__schemeID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /GlobalID /GlobalID__schemeID
        payeetradepartyglobalid.put({'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': payeepartyschemeid})


    # -/Invoice /PayeeParty /PartyName /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /Name
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /PayeeParty /PartyLegalEntity /CompanyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /SpecifiedLegalOrganization /ID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

    # -/Invoice /PayeeParty /PartyLegalEntity /CompanyID /CompanyID__schemeID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': None})})

    # -/Invoice /AccountingCost
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ReceivableSpecifiedTradeAccountingAccount /ID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ReceivableSpecifiedTradeAccountingAccount'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'AccountingCost', 'BOTSCONTENT': None})})

    for allowancecharge in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'AllowanceCharge'}):

        specifiedtradeallowancecharge = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeAllowanceCharge'})

        # -/Invoice /AllowanceCharge /Amount
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /Amount /Amount__currencyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount /ActualAmount__currencyID
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', ram+'ActualAmount__currencyID': setcurrency(allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', cbc+'Amount__currencyID': None}))})

        # -/Invoice /AllowanceCharge /BaseAmount
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /BaseAmount /BaseAmount__currencyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount /BasisAmount__currencyID
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', ram+'BasisAmount__currencyID': setcurrency(allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', cbc+'BaseAmount__currencyID': None}))})

        # -/Invoice /AllowanceCharge /MultiplierFactorNumeric
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CalculationPercent
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CalculationPercent', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'MultiplierFactorNumeric', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /TaxCategory /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /CategoryCode
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /TaxCategory /Percent
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /RateApplicablePercent
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /TaxCategory /TaxScheme /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /TypeCode
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /ChargeIndicator
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ChargeIndicator /Indicator
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ChargeIndicator'}, {'BOTSID': udt+'Indicator', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'ChargeIndicator', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /AllowanceChargeReason
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /Reason
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'Reason', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReason', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /AllowanceChargeReasonCode
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ReasonCode
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ReasonCode', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReasonCode', 'BOTSCONTENT': None})})

    paymenttermsnote = None
    for paymentterms in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PaymentTerms'}):

        specifiedtradepaymentterms = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradePaymentTerms'})

        # -/Invoice /PaymentMeans /PaymentMandate /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /DirectDebitMandateID
        specifiedtradepaymentterms.put({'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'DirectDebitMandateID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PaymentMandate'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        for note2 in paymentterms.getloop({'BOTSID': cac+'PaymentTerms'}, {'BOTSID': cbc+'Note'}):

            description3 = specifiedtradepaymentterms.putloop({'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'Description'})

            # -/Invoice /PaymentTerms /Note
            paymenttermsnote = note2.get({'BOTSID': cbc+'Note', 'BOTSCONTENT': None})
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /Description
            description3.put({'BOTSID': ram+'Description', 'BOTSCONTENT': paymenttermsnote})

    duedate = None
    if ubltype == 'Invoice':
        # - /Invoice /DueDate
        duedate = transformdate(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cbc+'DueDate', 'BOTSCONTENT': None}))
    elif ubltype == 'CreditNote':
        # - /CreditNote /PaymentMeans /PaymentDueDate
        duedate = transformdate(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentDueDate', 'BOTSCONTENT': None}))

    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /DueDateDateTime /DateTimeString
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'DueDateDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': dtf, 'BOTSCONTENT': duedate})

    if ubltype == 'CreditNote' and not duedate and not paymenttermsnote:

        description = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'Description'})

        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /Description
        # Fixed: 'Avoir'
        description.put({'BOTSID': ram+'Description', 'BOTSCONTENT': 'Avoir'})

    # -/Invoice /LegalMonetaryTotal /AllowanceTotalAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /AllowanceTotalAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'AllowanceTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'AllowanceTotalAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /AllowanceTotalAmount /AllowanceTotalAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /AllowanceTotalAmount /AllowanceTotalAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'AllowanceTotalAmount', ram+'AllowanceTotalAmount__currencyID': setcurrency(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'AllowanceTotalAmount', cbc+'AllowanceTotalAmount__currencyID': None}))})

    # -/Invoice /LegalMonetaryTotal /ChargeTotalAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /ChargeTotalAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'ChargeTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'ChargeTotalAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /ChargeTotalAmount /ChargeTotalAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /ChargeTotalAmount /ChargeTotalAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'ChargeTotalAmount', ram+'ChargeTotalAmount__currencyID': setcurrency(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'ChargeTotalAmount', cbc+'ChargeTotalAmount__currencyID': None}))})

    # -/Invoice /LegalMonetaryTotal /PayableAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /DuePayableAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'DuePayableAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /PayableAmount /PayableAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /DuePayableAmount /DuePayableAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'DuePayableAmount', ram+'DuePayableAmount__currencyID': setcurrency(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableAmount', cbc+'PayableAmount__currencyID': None}))})

    # -/Invoice /LegalMonetaryTotal /TaxInclusiveAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /GrandTotalAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'GrandTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxInclusiveAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /TaxInclusiveAmount /TaxInclusiveAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /GrandTotalAmount /GrandTotalAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'GrandTotalAmount', ram+'GrandTotalAmount__currencyID': setcurrency(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxInclusiveAmount', cbc+'TaxInclusiveAmount__currencyID': None}))})

    # -/Invoice /LegalMonetaryTotal /LineExtensionAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /LineTotalAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'LineExtensionAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /LineExtensionAmount /LineExtensionAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /LineTotalAmount /LineTotalAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', ram+'LineTotalAmount__currencyID': setcurrency(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'LineExtensionAmount', cbc+'LineExtensionAmount__currencyID': None}))})

    # -/Invoice /LegalMonetaryTotal /PayableRoundingAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /RoundingAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'RoundingAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableRoundingAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /PayableRoundingAmount /PayableRoundingAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /RoundingAmount /RoundingAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'RoundingAmount', ram+'RoundingAmount__currencyID': setcurrency(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableRoundingAmount', cbc+'PayableRoundingAmount__currencyID': None}))})

    # -/Invoice /LegalMonetaryTotal /TaxExclusiveAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxBasisTotalAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxBasisTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxExclusiveAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /TaxExclusiveAmount /TaxExclusiveAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxBasisTotalAmount /TaxBasisTotalAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxBasisTotalAmount', ram+'TaxBasisTotalAmount__currencyID': setcurrency(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxExclusiveAmount', cbc+'TaxExclusiveAmount__currencyID': None}))})

    # -/Invoice /LegalMonetaryTotal /PrepaidAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TotalPrepaidAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TotalPrepaidAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PrepaidAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /PrepaidAmount /PrepaidAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TotalPrepaidAmount /TotalPrepaidAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TotalPrepaidAmount', ram+'TotalPrepaidAmount__currencyID': setcurrency(inn.get({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PrepaidAmount', cbc+'PrepaidAmount__currencyID': None}))})

    paymentids = []
    for paymentmeans in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+'PaymentMeans'}):
        for paymentid in paymentmeans.getloop({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentID'}):
            paymentid = paymentid.get({'BOTSID': cbc+'PaymentID', 'BOTSCONTENT': None})
            if not paymentid in paymentids:
                paymentids.append(paymentid)

                paymentreference = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PaymentReference'})

                # -/Invoice /PaymentMeans /PaymentID
                # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PaymentReference
                paymentreference.put({'BOTSID': ram+'PaymentReference', 'BOTSCONTENT': paymentid})

        specifiedtradesettlementpaymentmeans = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'})

        # -/Invoice /PaymentMeans /CardAccount /HolderName
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /ApplicableTradeSettlementFinancialCard /CardholderName
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'ApplicableTradeSettlementFinancialCard'}, {'BOTSID': ram+'CardholderName', 'BOTSCONTENT': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'CardAccount'}, {'BOTSID': cbc+'HolderName', 'BOTSCONTENT': None})})

        # -/Invoice /PaymentMeans /CardAccount /PrimaryAccountNumberID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /ApplicableTradeSettlementFinancialCard /ID
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'ApplicableTradeSettlementFinancialCard'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'CardAccount'}, {'BOTSID': cbc+'PrimaryAccountNumberID', 'BOTSCONTENT': None})})

        # -/Invoice /PaymentMeans /PaymentMeansCode /PaymentMeansCode__name
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /Information
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'Information', 'BOTSCONTENT': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', cbc+'PaymentMeansCode__name': None})})

        # -/Invoice /PaymentMeans /PayeeFinancialAccount /Name
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayeePartyCreditorFinancialAccount /AccountName
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayeePartyCreditorFinancialAccount'}, {'BOTSID': ram+'AccountName', 'BOTSCONTENT': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PayeeFinancialAccount'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

        # -/Invoice /PaymentMeans /PayeeFinancialAccount /ID
        payeefinancialaccountid = paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PayeeFinancialAccount'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})

        if payeefinancialaccountid and isiban(payeefinancialaccountid):
            # -/Invoice /PaymentMeans /PayeeFinancialAccount /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayeePartyCreditorFinancialAccount /IBANID
            specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayeePartyCreditorFinancialAccount'}, {'BOTSID': ram+'IBANID', 'BOTSCONTENT': payeefinancialaccountid})

        elif payeefinancialaccountid:
            # -/Invoice /PaymentMeans /PayeeFinancialAccount /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayeePartyCreditorFinancialAccount /ProprietaryID
            specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayeePartyCreditorFinancialAccount'}, {'BOTSID': ram+'ProprietaryID', 'BOTSCONTENT': payeefinancialaccountid})

        # -/Invoice /PaymentMeans /PayeeFinancialAccount /FinancialInstitutionBranch /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayeeSpecifiedCreditorFinancialInstitution /BICID
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayeeSpecifiedCreditorFinancialInstitution'}, {'BOTSID': ram+'BICID', 'BOTSCONTENT': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PayeeFinancialAccount'}, {'BOTSID': cac+'FinancialInstitutionBranch'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /PaymentMeans /PaymentMandate /PayerFinancialAccount /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayerPartyDebtorFinancialAccount /IBANID
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayerPartyDebtorFinancialAccount'}, {'BOTSID': ram+'IBANID', 'BOTSCONTENT': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PaymentMandate'}, {'BOTSID': cac+'PayerFinancialAccount'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /PaymentMeans /PaymentMeansCode
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', 'BOTSCONTENT': None})})

        # -/Invoice /PaymentMeans /PaymentMeansCode /PaymentMeansCode__listAgencyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode /TypeCode__listAgencyID
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', ram+'TypeCode__listAgencyID': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', cbc+'PaymentMeansCode__listAgencyID': None})})

        # -/Invoice /PaymentMeans /PaymentMeansCode /PaymentMeansCode__listID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode /TypeCode__listID
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', ram+'TypeCode__listID': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', cbc+'PaymentMeansCode__listID': None})})

        # -/Invoice /PaymentMeans /PaymentMeansCode /PaymentMeansCode__listURI
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode /TypeCode__listURI
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', ram+'TypeCode__listURI': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', cbc+'PaymentMeansCode__listURI': None})})

        # -/Invoice /PaymentMeans /PaymentMeansCode /PaymentMeansCode__listVersionID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode /TypeCode__listVersionID
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', ram+'TypeCode__listVersionID': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', cbc+'PaymentMeansCode__listVersionID': None})})

    for invoiceline in inn.getloop({'BOTSID': xmlns+ubltype}, {'BOTSID': cac+ubltype+'Line'}):

        includedsupplychaintradelineitem = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'IncludedSupplyChainTradeLineItem'})

        # -/Invoice /InvoiceLine /LineExtensionAmount
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeSettlementLineMonetarySummation /LineTotalAmount
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementLineMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+'LineExtensionAmount', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /LineExtensionAmount /LineExtensionAmount__currencyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeSettlementLineMonetarySummation /LineTotalAmount /LineTotalAmount__currencyID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementLineMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', ram+'LineTotalAmount__currencyID': setcurrency(invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+'LineExtensionAmount', cbc+'LineExtensionAmount__currencyID': None}))})

        for note3 in invoiceline.getloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+'Note'}):

            includednote2 = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'AssociatedDocumentLineDocument'}, {'BOTSID': ram+'IncludedNote'})

            # -/Invoice /InvoiceLine /Note
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /AssociatedDocumentLineDocument /IncludedNote /Content
            includednote2.put({'BOTSID': ram+'IncludedNote'}, {'BOTSID': ram+'Content', 'BOTSCONTENT': note3.get({'BOTSID': cbc+'Note', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /AssociatedDocumentLineDocument /LineID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'AssociatedDocumentLineDocument'}, {'BOTSID': ram+'LineID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /OrderLineReference /LineID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /BuyerOrderReferencedDocument /LineID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'BuyerOrderReferencedDocument'}, {'BOTSID': ram+'LineID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'OrderLineReference'}, {'BOTSID': cbc+'LineID', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Price /BaseQuantity
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /BasisQuantity
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Price /BaseQuantity /BaseQuantity__unitCode
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /BasisQuantity /BasisQuantity__unitCode
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', ram+'BasisQuantity__unitCode': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', cbc+'BaseQuantity__unitCode': None})})

        # -/Invoice /InvoiceLine /Price /PriceAmount
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /ChargeAmount
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'PriceAmount', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Price /PriceAmount /PriceAmount__currencyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /ChargeAmount /ChargeAmount__currencyID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', ram+'ChargeAmount__currencyID': setcurrency(invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'PriceAmount', cbc+'PriceAmount__currencyID': None}))})

        # -/Invoice /InvoiceLine /Delivery /ActualDeliveryDate
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeDelivery /ActualDeliverySupplyChainEvent /OccurrenceDateTime /DateTimeString
        # includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeDelivery'}, {'BOTSID': ram+'ActualDeliverySupplyChainEvent'}, {'BOTSID': ram+'OccurrenceDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': transformdate(invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cbc+'ActualDeliveryDate', 'BOTSCONTENT': None}))})

        qtytag = 'CreditedQuantity' if ubltype == 'CreditNote' else 'InvoicedQuantity'
        # -/Invoice /InvoiceLine /InvoicedQuantity
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeDelivery /BilledQuantity
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeDelivery'}, {'BOTSID': ram+'BilledQuantity', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+qtytag, 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /InvoicedQuantity /InvoicedQuantity__unitCode
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeDelivery /BilledQuantity /BilledQuantity__unitCode
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeDelivery'}, {'BOTSID': ram+'BilledQuantity', ram+'BilledQuantity__unitCode': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+qtytag, cbc+qtytag+'__unitCode': None})})

        for documentreference in invoiceline.getloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'DocumentReference'}):

            additionalreferenceddocument2 = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'AdditionalReferencedDocument'})

            # -/Invoice /InvoiceLine /DocumentReference /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /AdditionalReferencedDocument /IssuerAssignedID
            additionalreferenceddocument2.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': documentreference.get({'BOTSID': cac+'DocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /DocumentReference /ID /ID__schemeID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /AdditionalReferencedDocument /ReferenceTypeCode
            additionalreferenceddocument2.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'ReferenceTypeCode', 'BOTSCONTENT': documentreference.get({'BOTSID': cac+'DocumentReference'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})})

            # -/Invoice /InvoiceLine /DocumentReference /DocumentTypeCode
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /AdditionalReferencedDocument /TypeCode
            additionalreferenceddocument2.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': documentreference.get({'BOTSID': cac+'DocumentReference'}, {'BOTSID': cbc+'DocumentTypeCode', 'BOTSCONTENT': None})})

        for classifiedtaxcategory in invoiceline.getloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'ClassifiedTaxCategory'}):

            applicabletradetax2 = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'})

            # -/Invoice /InvoiceLine /Item /ClassifiedTaxCategory /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ApplicableTradeTax /CategoryCode
            applicabletradetax2.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': classifiedtaxcategory.get({'BOTSID': cac+'ClassifiedTaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /Item /ClassifiedTaxCategory /Percent
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ApplicableTradeTax /RateApplicablePercent
            applicabletradetax2.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': classifiedtaxcategory.get({'BOTSID': cac+'ClassifiedTaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /Item /ClassifiedTaxCategory /TaxScheme /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ApplicableTradeTax /TypeCode
            applicabletradetax2.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': classifiedtaxcategory.get({'BOTSID': cac+'ClassifiedTaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /InvoicePeriod /EndDate
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /BillingSpecifiedPeriod /EndDateTime /DateTimeString
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'EndDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': dtf, 'BOTSCONTENT': transformdate(invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'EndDate', 'BOTSCONTENT': None}))})

        # -/Invoice /InvoiceLine /InvoicePeriod /StartDate
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /BillingSpecifiedPeriod /StartDateTime /DateTimeString
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'StartDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': dtf, 'BOTSCONTENT': transformdate(invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'StartDate', 'BOTSCONTENT': None}))})

        # -/Invoice /InvoiceLine /AccountingCost
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ReceivableSpecifiedTradeAccountingAccount /ID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'ReceivableSpecifiedTradeAccountingAccount'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cbc+'AccountingCost', 'BOTSCONTENT': None})})

        for allowancecharge in invoiceline.getloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'AllowanceCharge'}):

            specifiedtradeallowancecharge2 = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeAllowanceCharge'})

            # -/Invoice /InvoiceLine /AllowanceCharge /Amount
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /AllowanceCharge /Amount /Amount__currencyID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount /ActualAmount__currencyID
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', ram+'ActualAmount__currencyID': setcurrency(allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', cbc+'Amount__currencyID': None}))})

            # -/Invoice /InvoiceLine /AllowanceCharge /BaseAmount
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /AllowanceCharge /BaseAmount /BaseAmount__currencyID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount /BasisAmount__currencyID
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', ram+'BasisAmount__currencyID': setcurrency(allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', cbc+'BaseAmount__currencyID': None}))})

            # -/Invoice /InvoiceLine /AllowanceCharge /MultiplierFactorNumeric
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /CalculationPercent
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CalculationPercent', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'MultiplierFactorNumeric', 'BOTSCONTENT': None})})

            for taxcategory in allowancecharge.getloop({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cac+'TaxCategory'}):

                categorytradetax2 = specifiedtradeallowancecharge2.putloop({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CategoryTradeTax'})

                # -/Invoice /InvoiceLine /AllowanceCharge /TaxCategory /ID
                # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /CategoryCode
                categorytradetax2.put({'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': taxcategory.get({'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

                # -/Invoice /InvoiceLine /AllowanceCharge /TaxCategory /Percent
                # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /RateApplicablePercent
                categorytradetax2.put({'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': taxcategory.get({'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /AllowanceCharge /ChargeIndicator
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ChargeIndicator /Indicator
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ChargeIndicator'}, {'BOTSID': udt+'Indicator', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'ChargeIndicator', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /AllowanceCharge /AllowanceChargeReason
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /Reason
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'Reason', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReason', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /AllowanceCharge /AllowanceChargeReasonCode
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ReasonCode
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ReasonCode', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReasonCode', 'BOTSCONTENT': None})})

        if invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': None}):

            grosspriceproducttradeprice = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'})

            # -/Invoice /InvoiceLine /Price /AllowanceCharge /BaseAmount
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /ChargeAmount
            grosspriceproducttradeprice.put({'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /Price /AllowanceCharge /BaseAmount /BaseAmount__currencyID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /ChargeAmount /ChargeAmount__currencyID
            grosspriceproducttradeprice.put({'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', ram+'ChargeAmount__currencyID': setcurrency(invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', cbc+'BaseAmount__currencyID': None}))})

            # -/Invoice /InvoiceLine /Price /BaseQuantity
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /BasisQuantity
            grosspriceproducttradeprice.put({'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /Price /BaseQuantity /BaseQuantity__unitCode
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /BasisQuantity /BasisQuantity__unitCode
            grosspriceproducttradeprice.put({'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', ram+'BasisQuantity__unitCode': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', cbc+'BaseQuantity__unitCode': None})})

            for priceallowancecharge in invoiceline.getloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Price'}, {'BOTSID': cac+'AllowanceCharge'}):

                # -/Invoice /InvoiceLine /Price /AllowanceCharge /Amount
                allowancechargeamount = priceallowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': None})

                if allowancechargeamount and bool(float(allowancechargeamount)):

                    appliedtradeallowancecharge = grosspriceproducttradeprice.putloop({'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'AppliedTradeAllowanceCharge'})

                    # -/Invoice /InvoiceLine /Price /AllowanceCharge /Amount
                    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ActualAmount
                    appliedtradeallowancecharge.put({'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': allowancechargeamount})

                    # -/Invoice /InvoiceLine /Price /AllowanceCharge /Amount /Amount__currencyID
                    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ActualAmount /ActualAmount__currencyID
                    appliedtradeallowancecharge.put({'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', ram+'ActualAmount__currencyID': setcurrency(priceallowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', cbc+'Amount__currencyID': None}))})

                    # -/Invoice /InvoiceLine /Price /AllowanceCharge /ChargeIndicator
                    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ChargeIndicator /Indicator
                    appliedtradeallowancecharge.put({'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ChargeIndicator'}, {'BOTSID': udt+'Indicator', 'BOTSCONTENT': priceallowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'ChargeIndicator', 'BOTSCONTENT': None})})

        for additionalitemproperty in invoiceline.getloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'AdditionalItemProperty'}):

            applicableproductcharacteristic = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'ApplicableProductCharacteristic'})

            # -/Invoice /InvoiceLine /Item /AdditionalItemProperty /Name
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /ApplicableProductCharacteristic /Description
            applicableproductcharacteristic.put({'BOTSID': ram+'ApplicableProductCharacteristic'}, {'BOTSID': ram+'Description', 'BOTSCONTENT': additionalitemproperty.get({'BOTSID': cac+'AdditionalItemProperty'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /Item /AdditionalItemProperty /Value
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /ApplicableProductCharacteristic /Value
            applicableproductcharacteristic.put({'BOTSID': ram+'ApplicableProductCharacteristic'}, {'BOTSID': ram+'Value', 'BOTSCONTENT': additionalitemproperty.get({'BOTSID': cac+'AdditionalItemProperty'}, {'BOTSID': cbc+'Value', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Item /BuyersItemIdentification /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /BuyerAssignedID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'BuyerAssignedID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'BuyersItemIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        itemdescription = ''
        for description2 in invoiceline.getloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Item'}, {'BOTSID': cbc+'Description'}):

            itemdescription += description2.get({'BOTSID': cbc+'Description', 'BOTSCONTENT': None}) or ''

        # -/Invoice /InvoiceLine /Item /Description
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /Description
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'Description', 'BOTSCONTENT': itemdescription or None})

        for commodityclassification in invoiceline.getloop({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'CommodityClassification'}):

            designatedproductclassification = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'DesignatedProductClassification'})

            # -/Invoice /InvoiceLine /Item /CommodityClassification /ItemClassificationCode
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /DesignatedProductClassification /ClassCode
            designatedproductclassification.put({'BOTSID': ram+'DesignatedProductClassification'}, {'BOTSID': ram+'ClassCode', 'BOTSCONTENT': commodityclassification.get({'BOTSID': cac+'CommodityClassification'}, {'BOTSID': cbc+'ItemClassificationCode', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /Item /CommodityClassification /ItemClassificationCode /ItemClassificationCode__listID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /DesignatedProductClassification /ClassCode /ClassCode__listID
            designatedproductclassification.put({'BOTSID': ram+'DesignatedProductClassification'}, {'BOTSID': ram+'ClassCode', ram+'ClassCode__listID': commodityclassification.get({'BOTSID': cac+'CommodityClassification'}, {'BOTSID': cbc+'ItemClassificationCode', cbc+'ItemClassificationCode__listID': None})})

            # -/Invoice /InvoiceLine /Item /CommodityClassification /ItemClassificationCode /ItemClassificationCode__listVersionID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /DesignatedProductClassification /ClassCode /ClassCode__listVersionID
            designatedproductclassification.put({'BOTSID': ram+'DesignatedProductClassification'}, {'BOTSID': ram+'ClassCode', ram+'ClassCode__listVersionID': commodityclassification.get({'BOTSID': cac+'CommodityClassification'}, {'BOTSID': cbc+'ItemClassificationCode', cbc+'ItemClassificationCode__listVersionID': None})})

        # -/Invoice /InvoiceLine /Item /StandardItemIdentification /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /GlobalID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'GlobalID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'StandardItemIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Item /StandardItemIdentification /ID /ID__schemeID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /GlobalID /GlobalID__schemeID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'StandardItemIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})})

        # -/Invoice /InvoiceLine /Item /Name
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /Name
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Item'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Item /OriginCountry /IdentificationCode
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /OriginTradeCountry /ID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'OriginTradeCountry'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'OriginCountry'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Item /SellersItemIdentification /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /SellerAssignedID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'SellerAssignedID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+ubltype+'Line'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'SellersItemIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})
