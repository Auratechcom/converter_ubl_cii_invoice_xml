# -*- coding: utf-8 -*-
"""
bots-mapping-script
Message: xml/UBL21_INVOICE > xml/D16B_CII
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


def transformdate(datestr):

    return transform.datemask(datestr, 'CCYY-MM-DD', 'CCYYMMDD')


def main(inn, out):

    # IN Message: xml/UBL21_INVOICE
    inn_syntax = get_grammar(inn).syntax
    xmlns = inn_syntax['xmlns']
    cbc = inn_syntax['cbc']
    cac = inn_syntax['cac']

    # OUT Message: xml/D16B_CII
    out_syntax = get_grammar(out).syntax
    rsm = out_syntax['rsm']
    qdt = out_syntax['qdt']
    udt = out_syntax['udt']
    ram = out_syntax['ram']

    out.put({'BOTSID': rsm+'CrossIndustryInvoice', rsm+'CrossIndustryInvoice__xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'})

    # -/Invoice /ID
    # +/CrossIndustryInvoice /ExchangedDocument /ID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    exchangeddocumentcontext = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocumentContext'})

    # +/CrossIndustryInvoice /ExchangedDocumentContext /TestIndicator /IndicatorString
    # exchangeddocumentcontext.put({'BOTSID': rsm+'ExchangedDocumentContext'}, {'BOTSID': ram+'TestIndicator'}, {'BOTSID': udt+'IndicatorString', 'BOTSCONTENT': 'False'})

    # -/Invoice /ProfileID
    # +/CrossIndustryInvoice /ExchangedDocumentContext /GuidelineSpecifiedDocumentContextParameter /ID
    exchangeddocumentcontext.put({'BOTSID': rsm+'ExchangedDocumentContext'}, {'BOTSID': ram+'GuidelineSpecifiedDocumentContextParameter'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'ProfileID', 'BOTSCONTENT': None})})

    for note in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'Note'}):

        includednote = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'IncludedNote'})

        # -/Invoice /Note
        # +/CrossIndustryInvoice /ExchangedDocument /IncludedNote /Content
        includednote.put({'BOTSID': ram+'IncludedNote'}, {'BOTSID': ram+'Content', 'BOTSCONTENT': note.get({'BOTSID': cbc+'Note', 'BOTSCONTENT': None})})

    # -/Invoice /IssueDate
    # +/CrossIndustryInvoice /ExchangedDocument /IssueDateTime /DateTimeString
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'IssueDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': '102', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'IssueDate', 'BOTSCONTENT': None}))})

    # -/Invoice /InvoiceTypeCode
    # +/CrossIndustryInvoice /ExchangedDocument /TypeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'InvoiceTypeCode', 'BOTSCONTENT': None})})

    for additionaldocumentreference in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AdditionalDocumentReference'}):

        additionalreferenceddocument = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'AdditionalReferencedDocument'})

        # -/Invoice /AdditionalDocumentReference /Attachment /EmbeddedDocumentBinaryObject
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /AttachmentBinaryObject
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'AttachmentBinaryObject', 'BOTSCONTENT': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cbc+'EmbeddedDocumentBinaryObject', 'BOTSCONTENT': None})})

        # -/Invoice /AdditionalDocumentReference /Attachment /EmbeddedDocumentBinaryObject /EmbeddedDocumentBinaryObject__filename
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /AttachmentBinaryObject /AttachmentBinaryObject__filename
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'AttachmentBinaryObject', ram+'AttachmentBinaryObject__filename': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cbc+'EmbeddedDocumentBinaryObject', cbc+'EmbeddedDocumentBinaryObject__filename': None})})

        # -/Invoice /AdditionalDocumentReference /Attachment /EmbeddedDocumentBinaryObject /EmbeddedDocumentBinaryObject__mimeCode
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /AttachmentBinaryObject /AttachmentBinaryObject__mimeCode
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'AttachmentBinaryObject', ram+'AttachmentBinaryObject__mimeCode': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cbc+'EmbeddedDocumentBinaryObject', cbc+'EmbeddedDocumentBinaryObject__mimeCode': None})})

        # -/Invoice /AdditionalDocumentReference /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /IssuerAssignedID
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        for documentdescription in additionaldocumentreference.getloop({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'DocumentDescription'}):

            name = additionalreferenceddocument.putloop({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'Name'})

            # -/Invoice /AdditionalDocumentReference /DocumentDescription
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /Name
            name.put({'BOTSID': ram+'Name', 'BOTSCONTENT': documentdescription.get({'BOTSID': cbc+'DocumentDescription', 'BOTSCONTENT': None})})

        # -/Invoice /AdditionalDocumentReference /ID /ID__schemeID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /ReferenceTypeCode
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'ReferenceTypeCode', 'BOTSCONTENT': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})})

        # -/Invoice /AdditionalDocumentReference /Attachment /ExternalReference /URI
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /URIID
        additionalreferenceddocument.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': additionaldocumentreference.get({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cac+'ExternalReference'}, {'BOTSID': cbc+'URI', 'BOTSCONTENT': None})})

    # -/Invoice /OrderReference /ID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerOrderReferencedDocument /IssuerAssignedID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerOrderReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'OrderReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    # -/Invoice /BuyerReference
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerReference
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerReference', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'BuyerReference', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /AccountingContact /ElectronicMail
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /EmailURIUniversalCommunication /URIID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'EmailURIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'ElectronicMail', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /AccountingContact /Telefax
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /FaxUniversalCommunication /CompleteNumber
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'FaxUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Telefax', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /AccountingContact /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /PersonName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'PersonName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /AccountingContact /Telephone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /TelephoneUniversalCommunication /CompleteNumber
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'TelephoneUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Telephone', 'BOTSCONTENT': None})})

    for partylegalentity in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}):

        customerlegalform = partylegalentity.get({'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyLegalForm', 'BOTSCONTENT': None})
        if customerlegalform:
            description = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'Description'})

            # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyLegalForm
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /Description
            description.put({'BOTSID': ram+'Description', 'BOTSCONTENT': customerlegalform})

    for partyidentification in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'}):

        id = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'ID'})

        # -/Invoice /AccountingCustomerParty /Party /PartyIdentification /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /ID
        id.put({'BOTSID': ram+'ID', 'BOTSCONTENT': partyidentification.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /AccountingCustomerParty /Party /PartyIdentification /ID /ID__schemeID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /ID /ID__schemeID
        id.put({'BOTSID': ram+'ID', ram+'ID__schemeID': partyidentification.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyName /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /Name
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CityName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountryID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /Country /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountryName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /CountrySubentity
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountrySubDivisionName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineOne
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineThree
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineTwo
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PostalAddress /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /PostcodeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /ID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyID /CompanyID__schemeID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CityName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /Country /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /CountrySubentity
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountrySubDivisionName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineOne
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineThree
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineTwo
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /PostcodeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'RegistrationName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /EndpointID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /URIUniversalCommunication /URIID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingCustomerParty /Party /EndpointID /EndpointID__schemeID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /URIUniversalCommunication /URIID /URIID__schemeID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', ram+'URIID__schemeID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', cbc+'EndpointID__schemeID': None})})

    for contractdocumentreference in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'ContractDocumentReference'}):

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
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerOrderReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'OrderReference'}, {'BOTSID': cbc+'SalesOrderID', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CityName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CountryID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /CountrySubentity
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CountrySubDivisionName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineOne
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineThree
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineTwo
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PostalAddress /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /PostcodeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryParty /PartyName /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /TaxRepresentativeParty /PartyName /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    for partytaxscheme in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PartyTaxScheme'}):

        specifiedtaxregistration = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'})

        # -/Invoice /TaxRepresentativeParty /PartyTaxScheme /CompanyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /SpecifiedTaxRegistration /ID
        specifiedtaxregistration.put({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': 'VA', 'BOTSCONTENT': partytaxscheme.get({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /AccountingContact /ElectronicMail
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /EmailURIUniversalCommunication /URIID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'EmailURIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'ElectronicMail', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /AccountingContact /Telefax
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /FaxUniversalCommunication /CompleteNumber
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'FaxUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Telefax', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /AccountingContact /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /PersonName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'PersonName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /AccountingContact /Telephone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /TelephoneUniversalCommunication /CompleteNumber
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'TelephoneUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Telephone', 'BOTSCONTENT': None})})

    for partylegalentity2 in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}):

        supplierlegalform = partylegalentity2.get({'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyLegalForm', 'BOTSCONTENT': None})
        if supplierlegalform:
            description2 = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'Description'})

            # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyLegalForm
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /Description
            description2.put({'BOTSID': ram+'Description', 'BOTSCONTENT': supplierlegalform})

    # -/Invoice /AccountingSupplierParty /Party /EndpointID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /URIUniversalCommunication /URIID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /EndpointID /EndpointID__schemeID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /URIUniversalCommunication /URIID /URIID__schemeID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', ram+'URIID__schemeID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', cbc+'EndpointID__schemeID': None})})

    for partyidentification2 in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'}):

        # globalid2 = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'GlobalID'})

        id2 = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'ID'})

        # -/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /ID
        id2.put({'BOTSID': ram+'ID', 'BOTSCONTENT': partyidentification2.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID /ID__schemeID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /ID /ID__schemeID
        id2.put({'BOTSID': ram+'ID', ram+'ID__schemeID': partyidentification2.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyName /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /Name
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CityName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountryID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /Country /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountryName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /CountrySubentity
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountrySubDivisionName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineOne
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineThree
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineTwo
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PostalAddress /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /PostcodeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /ID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyID /CompanyID__schemeID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CityName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /Country /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /CountrySubentity
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountrySubDivisionName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineOne
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineThree
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineTwo
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /PostcodeCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    # -/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'RegistrationName', 'BOTSCONTENT': None})})

    for suppliertaxscheme in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyTaxScheme'}):

        sellertaxregistration = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'})

        # -/Invoice /AccountingSupplierParty /Party /PartyTaxScheme /CompanyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedTaxRegistration /ID
        sellertaxregistration.put({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': 'VA', 'BOTSCONTENT': suppliertaxscheme.get({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

    for customertaxscheme in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyTaxScheme'}):

        buyertaxregistration = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'})

        # -/Invoice /AccountingCustomerParty /Party /PartyTaxScheme /CompanyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedTaxRegistration /ID
        buyertaxregistration.put({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': 'VA', 'BOTSCONTENT': customertaxscheme.get({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

    # -/Invoice /ProjectReference /ID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SpecifiedProcuringProject /ID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SpecifiedProcuringProject'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'ProjectReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    applicableheadertradedelivery = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'})
    # -/Invoice /Delivery /ActualDeliveryDate
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ActualDeliverySupplyChainEvent /OccurrenceDateTime /DateTimeString
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ActualDeliverySupplyChainEvent'}, {'BOTSID': ram+'OccurrenceDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': '102', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cbc+'ActualDeliveryDate', 'BOTSCONTENT': None}))})

    # -/Invoice /ReceiptDocumentReference /ID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ReceivingAdviceReferencedDocument /IssuerAssignedID
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ReceivingAdviceReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'ReceiptDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    for delivery in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}):

        # globalid3 = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'GlobalID'})

        # -/Invoice /Delivery /DeliveryLocation /ID
        deliverylocid = delivery.get({'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})

        if deliverylocid:
            id3 = applicableheadertradedelivery.putloop({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'ID'})

            # -/Invoice /Delivery /DeliveryLocation /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /ID
            id3.put({'BOTSID': ram+'ID', 'BOTSCONTENT': deliverylocid})

            # -/Invoice /Delivery /DeliveryLocation /ID /ID__schemeID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /ID /ID__schemeID
            id3.put({'BOTSID': ram+'ID', ram+'ID__schemeID': delivery.get({'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})})

        # -/Invoice /Delivery /DeliveryLocation /Address /CountrySubentity
        countrysubentity = delivery.get({'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': None})

        if countrysubentity:
            countrysubdivisionname4 = applicableheadertradedelivery.putloop({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName'})

            # -/Invoice /Delivery /DeliveryLocation /Address /CountrySubentity
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CountrySubDivisionName
            countrysubdivisionname4.put({'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': countrysubentity})

    # -/Invoice /Delivery /DeliveryLocation /Description
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /Name
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'Description', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /CityName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CityName
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /Country /IdentificationCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CountryID
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /StreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineOne
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /AddressLine /Line
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineThree
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /AdditionalStreetName
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineTwo
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': None})})

    # -/Invoice /Delivery /DeliveryLocation /Address /PostalZone
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /PostcodeCode
    applicableheadertradedelivery.put({'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': None})})

    for taxtotal in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxTotal'}):

        taxtotalamount = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxTotalAmount'})

        # -/Invoice /TaxTotal /TaxAmount /TaxAmount__currencyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxTotalAmount /TaxTotalAmount__currencyID
        taxtotalamount.put({'BOTSID': ram+'TaxTotalAmount', ram+'TaxTotalAmount__currencyID': taxtotal.get({'BOTSID': cac+'TaxTotal'}, {'BOTSID': cbc+'TaxAmount', cbc+'TaxAmount__currencyID': None})})

        # -/Invoice /TaxTotal /TaxAmount
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxTotalAmount
        taxtotalamount.put({'BOTSID': ram+'TaxTotalAmount', 'BOTSCONTENT': taxtotal.get({'BOTSID': cac+'TaxTotal'}, {'BOTSID': cbc+'TaxAmount', 'BOTSCONTENT': None})})

        for taxsubtotal in taxtotal.getloop({'BOTSID': cac+'TaxTotal'}, {'BOTSID': cac+'TaxSubtotal'}):
            
            applicabletradetax = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxableAmount
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /BasisAmount
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxableAmount', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxableAmount /TaxableAmount__currencyID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /BasisAmount /BasisAmount__currencyID
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'BasisAmount', ram+'BasisAmount__currencyID': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxableAmount', cbc+'TaxableAmount__currencyID': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxAmount
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CalculatedAmount
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CalculatedAmount', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxAmount', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxAmount /TaxAmount__currencyID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CalculatedAmount /CalculatedAmount__currencyID
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CalculatedAmount', ram+'CalculatedAmount__currencyID': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxAmount', cbc+'TaxAmount__currencyID': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxScheme /TaxTypeCode
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CategoryCode
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'TaxTypeCode', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxExemptionReason
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /ExemptionReason
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'ExemptionReason', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'TaxExemptionReason', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxExemptionReasonCode
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /ExemptionReasonCode
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'ExemptionReasonCode', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'TaxExemptionReasonCode', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /Percent
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /RateApplicablePercent
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': None})})

            # -/Invoice /TaxTotal /TaxSubtotal /TaxCategory /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /TypeCode
            applicabletradetax.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': taxsubtotal.get({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    # -/Invoice /TaxPointDate
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /TaxPointDate /DateString
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'TaxPointDate'}, {'BOTSID': udt+'DateString', udt+'DateTimeString__format': '102', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'TaxPointDate', 'BOTSCONTENT': None}))})

    # -/Invoice /InvoicePeriod /EndDate
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /BillingSpecifiedPeriod /EndDateTime /DateTimeString
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'EndDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': '102', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'EndDate', 'BOTSCONTENT': None}))})

    # -/Invoice /InvoicePeriod /StartDate
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /BillingSpecifiedPeriod /StartDateTime /DateTimeString
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'StartDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': '102', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'StartDate', 'BOTSCONTENT': None}))})

    # -/Invoice /PaymentMeans /PaymentMandate /PayerFinancialAccount /ID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /CreditorReferenceID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'CreditorReferenceID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PaymentMandate'}, {'BOTSID': cac+'PayerFinancialAccount'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    # -/Invoice /DocumentCurrencyCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceCurrencyCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceCurrencyCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'DocumentCurrencyCode', 'BOTSCONTENT': None})})

    # -/Invoice /BillingReference /InvoiceDocumentReference /IssueDate
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceReferencedDocument /FormattedIssueDateTime /DateTimeString
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceReferencedDocument'}, {'BOTSID': ram+'FormattedIssueDateTime'}, {'BOTSID': qdt+'DateTimeString', qdt+'DateTimeString__format': '102', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'BillingReference'}, {'BOTSID': cac+'InvoiceDocumentReference'}, {'BOTSID': cbc+'IssueDate', 'BOTSCONTENT': None}))})

    # -/Invoice /BillingReference /InvoiceDocumentReference /ID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceReferencedDocument /IssuerAssignedID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'BillingReference'}, {'BOTSID': cac+'InvoiceDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

    for partyidentification3 in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyIdentification'}):

        # globalid4 = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'GlobalID'})

        id4 = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'ID'})

        # -/Invoice /PayeeParty /PartyIdentification /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /ID
        id4.put({'BOTSID': ram+'ID', 'BOTSCONTENT': partyidentification3.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /PayeeParty /PartyIdentification /ID /ID__schemeID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /ID /ID__schemeID
        id4.put({'BOTSID': ram+'ID', ram+'ID__schemeID': partyidentification3.get({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})})

    # -/Invoice /PayeeParty /PartyName /Name
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /Name
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

    # -/Invoice /PayeeParty /PartyLegalEntity /CompanyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /SpecifiedLegalOrganization /ID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': None})})

    # -/Invoice /PayeeParty /PartyLegalEntity /CompanyID /CompanyID__schemeID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': None})})

    # -/Invoice /AccountingCost
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ReceivableSpecifiedTradeAccountingAccount /ID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ReceivableSpecifiedTradeAccountingAccount'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'AccountingCost', 'BOTSCONTENT': None})})

    for allowancecharge in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AllowanceCharge'}):

        specifiedtradeallowancecharge = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeAllowanceCharge'})

        # -/Invoice /AllowanceCharge /Amount
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /BaseAmount
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /MultiplierFactorNumeric
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CalculationPercent
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CalculationPercent', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'MultiplierFactorNumeric', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /TaxCategory /Percent
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /RateApplicablePercent
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /TaxCategory /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /TypeCode
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /ChargeIndicator
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ChargeIndicator /Indicator
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ChargeIndicator'}, {'BOTSID': udt+'Indicator', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'ChargeIndicator', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /AllowanceChargeReason
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /Reason
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'Reason', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReason', 'BOTSCONTENT': None})})

        # -/Invoice /AllowanceCharge /AllowanceChargeReasonCode
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ReasonCode
        specifiedtradeallowancecharge.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ReasonCode', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReasonCode', 'BOTSCONTENT': None})})

    for paymentterms in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PaymentTerms'}):

        specifiedtradepaymentterms = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradePaymentTerms'})

        # -/Invoice /PaymentMeans /PaymentMandate /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /DirectDebitMandateID
        specifiedtradepaymentterms.put({'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'DirectDebitMandateID', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PaymentMandate'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        for note2 in paymentterms.getloop({'BOTSID': cac+'PaymentTerms'}, {'BOTSID': cbc+'Note'}):

            description3 = specifiedtradepaymentterms.putloop({'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'Description'})

            # -/Invoice /PaymentTerms /Note
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /Description
            description3.put({'BOTSID': ram+'Description', 'BOTSCONTENT': note2.get({'BOTSID': cbc+'Note', 'BOTSCONTENT': None})})

    # -/Invoice /PaymentMeans /PaymentDueDate
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /DueDateDateTime /DateTimeString
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'DueDateDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': '102', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentDueDate', 'BOTSCONTENT': None}))})

    # -/Invoice /LegalMonetaryTotal /AllowanceTotalAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /AllowanceTotalAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'AllowanceTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'AllowanceTotalAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /AllowanceTotalAmount /AllowanceTotalAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /AllowanceTotalAmount /AllowanceTotalAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'AllowanceTotalAmount', ram+'AllowanceTotalAmount__currencyID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'AllowanceTotalAmount', cbc+'AllowanceTotalAmount__currencyID': None})})

    # -/Invoice /LegalMonetaryTotal /ChargeTotalAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /ChargeTotalAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'ChargeTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'ChargeTotalAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /ChargeTotalAmount /ChargeTotalAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /ChargeTotalAmount /ChargeTotalAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'ChargeTotalAmount', ram+'ChargeTotalAmount__currencyID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'ChargeTotalAmount', cbc+'ChargeTotalAmount__currencyID': None})})

    # -/Invoice /LegalMonetaryTotal /PayableAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /DuePayableAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'DuePayableAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /PayableAmount /PayableAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /DuePayableAmount /DuePayableAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'DuePayableAmount', ram+'DuePayableAmount__currencyID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableAmount', cbc+'PayableAmount__currencyID': None})})

    # -/Invoice /LegalMonetaryTotal /TaxInclusiveAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /GrandTotalAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'GrandTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxInclusiveAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /TaxInclusiveAmount /TaxInclusiveAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /GrandTotalAmount /GrandTotalAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'GrandTotalAmount', ram+'GrandTotalAmount__currencyID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxInclusiveAmount', cbc+'TaxInclusiveAmount__currencyID': None})})

    # -/Invoice /LegalMonetaryTotal /LineExtensionAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /LineTotalAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'LineExtensionAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /LineExtensionAmount /LineExtensionAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /LineTotalAmount /LineTotalAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', ram+'LineTotalAmount__currencyID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'LineExtensionAmount', cbc+'LineExtensionAmount__currencyID': None})})

    # -/Invoice /LegalMonetaryTotal /PayableRoundingAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /RoundingAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'RoundingAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableRoundingAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /PayableRoundingAmount /PayableRoundingAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /RoundingAmount /RoundingAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'RoundingAmount', ram+'RoundingAmount__currencyID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableRoundingAmount', cbc+'PayableRoundingAmount__currencyID': None})})

    # -/Invoice /LegalMonetaryTotal /TaxExclusiveAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxBasisTotalAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxBasisTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxExclusiveAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /TaxExclusiveAmount /TaxExclusiveAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxBasisTotalAmount /TaxBasisTotalAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxBasisTotalAmount', ram+'TaxBasisTotalAmount__currencyID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxExclusiveAmount', cbc+'TaxExclusiveAmount__currencyID': None})})

    # -/Invoice /LegalMonetaryTotal /PrepaidAmount
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TotalPrepaidAmount
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TotalPrepaidAmount', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PrepaidAmount', 'BOTSCONTENT': None})})

    # -/Invoice /LegalMonetaryTotal /PrepaidAmount /PrepaidAmount__currencyID
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TotalPrepaidAmount /TotalPrepaidAmount__currencyID
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TotalPrepaidAmount', ram+'TotalPrepaidAmount__currencyID': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PrepaidAmount', cbc+'PrepaidAmount__currencyID': None})})

    for paymentmeans in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PaymentMeans'}):

        for paymentid in paymentmeans.getloop({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentID'}):

            paymentreference = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PaymentReference'})

            # -/Invoice /PaymentMeans /PaymentID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PaymentReference
            paymentreference.put({'BOTSID': ram+'PaymentReference', 'BOTSCONTENT': paymentid.get({'BOTSID': cbc+'PaymentID', 'BOTSCONTENT': None})})

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
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayeePartyCreditorFinancialAccount /IBANID
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayeePartyCreditorFinancialAccount'}, {'BOTSID': ram+'IBANID', 'BOTSCONTENT': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PayeeFinancialAccount'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /PaymentMeans /PayeeFinancialAccount /FinancialInstitutionBranch /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayerSpecifiedDebtorFinancialInstitution /BICID
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayerSpecifiedDebtorFinancialInstitution'}, {'BOTSID': ram+'BICID', 'BOTSCONTENT': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PayeeFinancialAccount'}, {'BOTSID': cac+'FinancialInstitutionBranch'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /PaymentMeans /PaymentMeansCode
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode
        specifiedtradesettlementpaymentmeans.put({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': paymentmeans.get({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', 'BOTSCONTENT': None})})

    # -/Invoice /TaxCurrencyCode
    # +/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /TaxCurrencyCode
    out.put({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'TaxCurrencyCode', 'BOTSCONTENT': inn.get({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'TaxCurrencyCode', 'BOTSCONTENT': None})})

    for invoiceline in inn.getloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'InvoiceLine'}):

        includedsupplychaintradelineitem = out.putloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'IncludedSupplyChainTradeLineItem'})

        # -/Invoice /InvoiceLine /LineExtensionAmount
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeSettlementLineMonetarySummation /LineTotalAmount
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementLineMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'LineExtensionAmount', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /LineExtensionAmount /LineExtensionAmount__currencyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeSettlementLineMonetarySummation /LineTotalAmount /LineTotalAmount__currencyID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementLineMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', ram+'LineTotalAmount__currencyID': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'LineExtensionAmount', cbc+'LineExtensionAmount__currencyID': None})})

        for note3 in invoiceline.getloop({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'Note'}):

            includednote2 = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'AssociatedDocumentLineDocument'}, {'BOTSID': ram+'IncludedNote'})

            # -/Invoice /InvoiceLine /Note
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /AssociatedDocumentLineDocument /IncludedNote /Content
            includednote2.put({'BOTSID': ram+'IncludedNote'}, {'BOTSID': ram+'Content', 'BOTSCONTENT': note3.get({'BOTSID': cbc+'Note', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /AssociatedDocumentLineDocument /LineID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'AssociatedDocumentLineDocument'}, {'BOTSID': ram+'LineID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /OrderLineReference /LineID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /BuyerOrderReferencedDocument /LineID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'BuyerOrderReferencedDocument'}, {'BOTSID': ram+'LineID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'OrderLineReference'}, {'BOTSID': cbc+'LineID', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Price /PriceAmount
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /ChargeAmount
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'PriceAmount', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Price /PriceAmount /PriceAmount__currencyID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /ChargeAmount /ChargeAmount__currencyID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', ram+'ChargeAmount__currencyID': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'PriceAmount', cbc+'PriceAmount__currencyID': None})})

        # -/Invoice /InvoiceLine /InvoicedQuantity
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeDelivery /BilledQuantity
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeDelivery'}, {'BOTSID': ram+'BilledQuantity', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'InvoicedQuantity', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /InvoicedQuantity /InvoicedQuantity__unitCode
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeDelivery /BilledQuantity /BilledQuantity__unitCode
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeDelivery'}, {'BOTSID': ram+'BilledQuantity', ram+'BilledQuantity__unitCode': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'InvoicedQuantity', cbc+'InvoicedQuantity__unitCode': None})})

        for documentreference in invoiceline.getloop({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'DocumentReference'}):

            additionalreferenceddocument2 = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'AdditionalReferencedDocument'})

            # -/Invoice /InvoiceLine /DocumentReference /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /AdditionalReferencedDocument /IssuerAssignedID
            additionalreferenceddocument2.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': documentreference.get({'BOTSID': cac+'DocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /DocumentReference /ID /ID__schemeID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /AdditionalReferencedDocument /IssuerAssignedID /IssuerAssignedID__schemeID
            additionalreferenceddocument2.put({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', ram+'IssuerAssignedID__schemeID': documentreference.get({'BOTSID': cac+'DocumentReference'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})})

        for classifiedtaxcategory in invoiceline.getloop({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'ClassifiedTaxCategory'}):

            applicabletradetax2 = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'})

            # -/Invoice /InvoiceLine /Item /ClassifiedTaxCategory /ID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ApplicableTradeTax /CategoryCode
            applicabletradetax2.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': classifiedtaxcategory.get({'BOTSID': cac+'ClassifiedTaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /Item /ClassifiedTaxCategory /Percent
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ApplicableTradeTax /RateApplicablePercent
            applicabletradetax2.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': classifiedtaxcategory.get({'BOTSID': cac+'ClassifiedTaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': None})})

            # 'VAT'
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ApplicableTradeTax /TypeCode
            applicabletradetax2.put({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': 'VAT'})

        # -/Invoice /InvoiceLine /InvoicePeriod /EndDate
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /BillingSpecifiedPeriod /EndDateTime /DateTimeString
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'EndDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': '102', 'BOTSCONTENT': transformdate(invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'EndDate', 'BOTSCONTENT': None}))})

        # -/Invoice /InvoiceLine /InvoicePeriod /StartDate
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /BillingSpecifiedPeriod /StartDateTime /DateTimeString
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'StartDateTime'}, {'BOTSID': udt+'DateTimeString', udt+'DateTimeString__format': '102', 'BOTSCONTENT': transformdate(invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'StartDate', 'BOTSCONTENT': None}))})

        # -/Invoice /InvoiceLine /AccountingCost
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ReceivableSpecifiedTradeAccountingAccount /ID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'ReceivableSpecifiedTradeAccountingAccount'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'AccountingCost', 'BOTSCONTENT': None})})

        for allowancecharge in invoiceline.getloop({'BOTSID': xmlns+'InvoiceLine'}, {'BOTSID': cac+'AllowanceCharge'}):

            specifiedtradeallowancecharge2 = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeAllowanceCharge'})

            # -/Invoice /InvoiceLine /AllowanceCharge /AllowanceChargeReason
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /Reason
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'Reason', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReason', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /AllowanceCharge /AllowanceChargeReasonCode
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ReasonCode
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ReasonCode', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReasonCode', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /AllowanceCharge /Amount
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /AllowanceCharge /Amount /Amount__currencyID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount /ActualAmount__currencyID
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', ram+'ActualAmount__currencyID': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', cbc+'Amount__currencyID': None})})

            # -/Invoice /InvoiceLine /AllowanceCharge /BaseAmount
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /AllowanceCharge /BaseAmount /BaseAmount__currencyID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount /BasisAmount__currencyID
            specifiedtradeallowancecharge2.put({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', ram+'BasisAmount__currencyID': allowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', cbc+'BaseAmount__currencyID': None})})

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

        if invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': None}):

            grosspriceproducttradeprice = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'})

            # -/Invoice /InvoiceLine /Price /AllowanceCharge /BaseAmount
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /ChargeAmount
            grosspriceproducttradeprice.put({'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /Price /AllowanceCharge /BaseAmount /BaseAmount__currencyID
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /ChargeAmount /ChargeAmount__currencyID
            grosspriceproducttradeprice.put({'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', ram+'ChargeAmount__currencyID': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', cbc+'BaseAmount__currencyID': None})})

            # -/Invoice /InvoiceLine /Price /BaseQuantity
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /BasisQuantity
            grosspriceproducttradeprice.put({'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /Price /BaseQuantity /BaseQuantity__unitCode
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /BasisQuantity /BasisQuantity__unitCode
            grosspriceproducttradeprice.put({'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', ram+'BasisQuantity__unitCode': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', cbc+'BaseQuantity__unitCode': None})})

            # -/Invoice /InvoiceLine /AllowanceCharge /ChargeIndicator
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ChargeIndicator /IndicatorString
            grosspriceproducttradeprice.put({'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ChargeIndicator'}, {'BOTSID': udt+'IndicatorString', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'ChargeIndicator', 'BOTSCONTENT': None})})

            for priceallowancecharge in invoiceline.getloop({'BOTSID': xmlns+'InvoiceLine'}, {'BOTSID': xmlns+'Price'}, {'BOTSID': cac+'AllowanceCharge'}):

                appliedtradeallowancecharge = grosspriceproducttradeprice.putloop({'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'AppliedTradeAllowanceCharge'})

                # -/Invoice /InvoiceLine /Price /AllowanceCharge /Amount
                # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ActualAmount
                appliedtradeallowancecharge.put({'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': priceallowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': None})})

                # -/Invoice /InvoiceLine /Price /AllowanceCharge /Amount /Amount__currencyID
                # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ActualAmount /ActualAmount__currencyID
                appliedtradeallowancecharge.put({'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', ram+'ActualAmount__currencyID': priceallowancecharge.get({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', cbc+'Amount__currencyID': None})})

        for additionalitemproperty in invoiceline.getloop({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'AdditionalItemProperty'}):

            applicableproductcharacteristic = includedsupplychaintradelineitem.putloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'ApplicableProductCharacteristic'})

            # -/Invoice /InvoiceLine /Item /AdditionalItemProperty /Name
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /ApplicableProductCharacteristic /Description
            applicableproductcharacteristic.put({'BOTSID': ram+'ApplicableProductCharacteristic'}, {'BOTSID': ram+'Description', 'BOTSCONTENT': additionalitemproperty.get({'BOTSID': cac+'AdditionalItemProperty'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

            # -/Invoice /InvoiceLine /Item /AdditionalItemProperty /Value
            # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /ApplicableProductCharacteristic /Value
            applicableproductcharacteristic.put({'BOTSID': ram+'ApplicableProductCharacteristic'}, {'BOTSID': ram+'Value', 'BOTSCONTENT': additionalitemproperty.get({'BOTSID': cac+'AdditionalItemProperty'}, {'BOTSID': cbc+'Value', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Item /BuyersItemIdentification /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /BuyerAssignedID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'BuyerAssignedID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'BuyersItemIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        itemdescription = ''
        for description2 in invoiceline.getloop({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Item'}, {'BOTSID': cbc+'Description'}):

            itemdescription += description2.get({'BOTSID': cbc+'Description', 'BOTSCONTENT': None}) or ''

        # -/Invoice /InvoiceLine /Item /Description
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /Description
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'Description', 'BOTSCONTENT': itemdescription or None})

        for commodityclassification in invoiceline.getloop({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'CommodityClassification'}):

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
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'GlobalID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'StandardItemIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Item /StandardItemIdentification /ID /ID__schemeID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /GlobalID /GlobalID__schemeID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'StandardItemIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': None})})

        # -/Invoice /InvoiceLine /Item /Name
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /Name
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Item'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Item /OriginCountry /IdentificationCode
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /OriginTradeCountry /ID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'OriginTradeCountry'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'OriginCountry'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': None})})

        # -/Invoice /InvoiceLine /Item /SellersItemIdentification /ID
        # +/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedTradeProduct /SellerAssignedID
        includedsupplychaintradelineitem.put({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedTradeProduct'}, {'BOTSID': ram+'SellerAssignedID', 'BOTSCONTENT': invoiceline.get({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Item'}, {'BOTSID': cac+'SellersItemIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': None})})
