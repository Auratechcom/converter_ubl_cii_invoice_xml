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


def main(inn, out):

    # IN Message: xml/D16B_CII
    inn_syntax = get_grammar(inn).syntax
    rsm = inn_syntax['rsm']
    qdt = inn_syntax['qdt']
    udt = inn_syntax['udt']
    ram = inn_syntax['ram']

    # OUT Message: xml/UBL21_INVOICE
    out_syntax = get_grammar(out).syntax
    xmlns = out_syntax['xmlns']
    cbc = out_syntax['cbc']
    cac = out_syntax['cac']

    # +/Invoice /UBLVersionID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'UBLVersionID', 'BOTSCONTENT': out_syntax['reference']})

    # -/CrossIndustryInvoice /ExchangedDocumentContext /GuidelineSpecifiedDocumentContextParameter /ID
    # +/Invoice /ProfileID
    profileid = inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocumentContext'}, {'BOTSID': ram+'GuidelineSpecifiedDocumentContextParameter'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'ProfileID', 'BOTSCONTENT': profileid})

    # -/CrossIndustryInvoice /ExchangedDocument /ID
    # +/Invoice /ID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    for includednote in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'IncludedNote'}):

        for content in includednote.getloop({'BOTSID': ram+'IncludedNote'}, {'BOTSID': ram+'Content'}):

            note = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'Note'})

            # -/CrossIndustryInvoice /ExchangedDocument /IncludedNote /Content
            # +/Invoice /Note
            note.put({'BOTSID': cbc+'Note', 'BOTSCONTENT': content.get({'BOTSID': ram+'Content', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /ExchangedDocument /IssueDateTime /DateTimeString
    # +/Invoice /IssueDate
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'IssueDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'IssueDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /ExchangedDocument /TypeCode
    # +/Invoice /InvoiceTypeCode
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'InvoiceTypeCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'ExchangedDocument'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': None})})

    for additionalreferenceddocument in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'AdditionalReferencedDocument'}):

        additionaldocumentreference = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AdditionalDocumentReference'})

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
        additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /Name
        # +/Invoice /AdditionalDocumentReference /DocumentDescription
        additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'DocumentDescription', 'BOTSCONTENT': additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /ReferenceTypeCode
        # +/Invoice /AdditionalDocumentReference /ID /ID__schemeID
        additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'ReferenceTypeCode', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /AdditionalReferencedDocument /URIID
        # +/Invoice /AdditionalDocumentReference /Attachment /ExternalReference /URI
        additionaldocumentreference.put({'BOTSID': cac+'AdditionalDocumentReference'}, {'BOTSID': cac+'Attachment'}, {'BOTSID': cac+'ExternalReference'}, {'BOTSID': cbc+'URI', 'BOTSCONTENT': additionalreferenceddocument.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerOrderReferencedDocument /IssuerAssignedID
    # +/Invoice /ContractDocumentReference /ID
    # out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'ContractDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerOrderReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerOrderReferencedDocument /IssuerAssignedID
    # +/Invoice /OrderReference /ID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'OrderReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerOrderReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerReference
    # +/Invoice /BuyerReference
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'BuyerReference', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerReference', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /EmailURIUniversalCommunication /URIID
    # +/Invoice /AccountingCustomerParty /AccountingContact /ElectronicMail
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'ElectronicMail', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'EmailURIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /FaxUniversalCommunication /CompleteNumber
    # +/Invoice /AccountingCustomerParty /AccountingContact /Telefax
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Telefax', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'FaxUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /PersonName
    # +/Invoice /AccountingCustomerParty /AccountingContact /Name
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'PersonName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /DefinedTradeContact /TelephoneUniversalCommunication /CompleteNumber
    # +/Invoice /AccountingCustomerParty /AccountingContact /Telephone
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Telephone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'TelephoneUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': None})})

    for description in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'Description'}):

        partylegalentity = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /Description
        # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyLegalForm
        partylegalentity.put({'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyLegalForm', 'BOTSCONTENT': description.get({'BOTSID': ram+'Description', 'BOTSCONTENT': None})})

    for id in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'ID'}):

        partyidentification = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /ID
        # +/Invoice /AccountingCustomerParty /Party /PartyIdentification /ID
        partyidentification.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': id.get({'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /ID /ID__schemeID
        # +/Invoice /AccountingCustomerParty /Party /PartyIdentification /ID /ID__schemeID
        partyidentification.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': id.get({'BOTSID': ram+'ID', ram+'ID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /Name
    # +/Invoice /AccountingCustomerParty /Party /PartyName /Name
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CityName
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /CityName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountryID
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /Country /IdentificationCode
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountryName
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /Country /Name
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /CountrySubDivisionName
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /CountrySubentity
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineOne
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /StreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineThree
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /AddressLine /Line
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /LineTwo
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /AdditionalStreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /PostalTradeAddress /PostcodeCode
    # +/Invoice /AccountingCustomerParty /Party /PostalAddress /PostalZone
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /ID
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /CompanyID /CompanyID__schemeID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CityName
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /CityName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryID
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /Country /IdentificationCode
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryName
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /Country /Name
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountrySubDivisionName
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /CountrySubentity
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineOne
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /StreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineThree
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /AddressLine /Line
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineTwo
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /AdditionalStreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /PostcodeCode
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationAddress /PostalZone
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    # +/Invoice /AccountingCustomerParty /Party /PartyLegalEntity /RegistrationName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'RegistrationName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /URIUniversalCommunication /URIID
    # +/Invoice /AccountingCustomerParty /Party /EndpointID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /URIUniversalCommunication /URIID /URIID__schemeID
    # +/Invoice /AccountingCustomerParty /Party /EndpointID /EndpointID__schemeID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', cbc+'EndpointID__schemeID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', ram+'URIID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /ContractReferencedDocument /IssuerAssignedID
    # +/Invoice /ContractDocumentReference /ID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'ContractDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'ContractReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /ContractReferencedDocument /ReferenceTypeCode
    reftypecode = inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'ContractReferencedDocument'}, {'BOTSID': ram+'ReferenceTypeCode', 'BOTSCONTENT': None})

    documenttypecode = None
    if reftypecode == 'BC':
        documenttypecode = 'Bon de commande'
    elif reftypecode == 'CT':
        documenttypecode = 'Contrat'

    # +/Invoice /ContractDocumentReference /DocumentTypeCode
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'ContractDocumentReference'}, {'BOTSID': cbc+'DocumentTypeCode', 'BOTSCONTENT': documenttypecode})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerOrderReferencedDocument /IssuerAssignedID
    # +/Invoice /OrderReference /SalesOrderID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'OrderReference'}, {'BOTSID': cbc+'SalesOrderID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerOrderReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CityName
    # +/Invoice /TaxRepresentativeParty /PostalAddress /CityName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CountryID
    # +/Invoice /TaxRepresentativeParty /PostalAddress /Country /IdentificationCode
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /CountrySubDivisionName
    # +/Invoice /TaxRepresentativeParty /PostalAddress /CountrySubentity
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineOne
    # +/Invoice /TaxRepresentativeParty /PostalAddress /StreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineThree
    # +/Invoice /TaxRepresentativeParty /PostalAddress /AddressLine /Line
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /LineTwo
    # +/Invoice /TaxRepresentativeParty /PostalAddress /AdditionalStreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /PostalTradeAddress /PostcodeCode
    # +/Invoice /TaxRepresentativeParty /PostalAddress /PostalZone
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    # +/Invoice /Delivery /DeliveryParty /PartyName /Name
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    # +/Invoice /TaxRepresentativeParty /PartyName /Name
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': None})})

    for specifiedtaxregistration in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTaxRepresentativeTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'}):

        partytaxscheme3 = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxRepresentativeParty'}, {'BOTSID': cac+'PartyTaxScheme'})

        # Fixed: 'VAT'
        # +/Invoice /TaxRepresentativeParty /PartyTaxScheme /TaxScheme /ID
        partytaxscheme3.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': 'VAT'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTaxRepresentativeTradeParty /SpecifiedTaxRegistration /ID
        # +/Invoice /TaxRepresentativeParty /PartyTaxScheme /CompanyID
        partytaxscheme3.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': specifiedtaxregistration.get({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /EmailURIUniversalCommunication /URIID
    # +/Invoice /AccountingSupplierParty /AccountingContact /ElectronicMail
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'ElectronicMail', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'EmailURIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /FaxUniversalCommunication /CompleteNumber
    # +/Invoice /AccountingSupplierParty /AccountingContact /Telefax
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Telefax', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'FaxUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /PersonName
    # +/Invoice /AccountingSupplierParty /AccountingContact /Name
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'PersonName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /DefinedTradeContact /TelephoneUniversalCommunication /CompleteNumber
    # +/Invoice /AccountingSupplierParty /AccountingContact /Telephone
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'AccountingContact'}, {'BOTSID': cbc+'Telephone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'DefinedTradeContact'}, {'BOTSID': ram+'TelephoneUniversalCommunication'}, {'BOTSID': ram+'CompleteNumber', 'BOTSCONTENT': None})})

    for description2 in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'Description'}):

        partylegalentity2 = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /Description
        # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyLegalForm
        partylegalentity2.put({'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyLegalForm', 'BOTSCONTENT': description2.get({'BOTSID': ram+'Description', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /URIUniversalCommunication /URIID
    # +/Invoice /AccountingSupplierParty /Party /EndpointID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /URIUniversalCommunication /URIID /URIID__schemeID
    # +/Invoice /AccountingSupplierParty /Party /EndpointID /EndpointID__schemeID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cbc+'EndpointID', cbc+'EndpointID__schemeID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'URIUniversalCommunication'}, {'BOTSID': ram+'URIID', ram+'URIID__schemeID': None})})

    # for globalid2 in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'GlobalID'}):

        # partyidentification2 = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /GlobalID /GlobalID__schemeID
        # +/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID /ID__schemeID
        # partyidentification2.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': globalid2.get({'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': None})})

    for id2 in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'ID'}):

        partyidentification2 = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyIdentification'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /ID
        # +/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID
        partyidentification2.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': id2.get({'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /ID /ID__schemeID
        # +/Invoice /AccountingSupplierParty /Party /PartyIdentification /ID /ID__schemeID
        partyidentification2.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': id2.get({'BOTSID': ram+'ID', ram+'ID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /Name
    # +/Invoice /AccountingSupplierParty /Party /PartyName /Name
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CityName
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /CityName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountryID
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /Country /IdentificationCode
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountryName
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /Country /Name
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /CountrySubDivisionName
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /CountrySubentity
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineOne
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /StreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineThree
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /AddressLine /Line
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /LineTwo
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /AdditionalStreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /PostalTradeAddress /PostcodeCode
    # +/Invoice /AccountingSupplierParty /Party /PostalAddress /PostalZone
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PostalAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /ID
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /CompanyID /CompanyID__schemeID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CityName
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /CityName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryID
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /Country /IdentificationCode
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountryName
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /Country /Name
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /CountrySubDivisionName
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /CountrySubentity
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineOne
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /StreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineThree
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /AddressLine /Line
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /LineTwo
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /AdditionalStreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /PostalTradeAddress /PostcodeCode
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationAddress /PostalZone
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cac+'RegistrationAddress'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedLegalOrganization /TradingBusinessName
    # +/Invoice /AccountingSupplierParty /Party /PartyLegalEntity /RegistrationName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'RegistrationName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'TradingBusinessName', 'BOTSCONTENT': None})})

    for sellertaxregistration in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SellerTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'}):

        suppliertaxscheme = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingSupplierParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyTaxScheme'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SellerTradeParty /SpecifiedTaxRegistration /ID
        # +/Invoice /AccountingSupplierParty /Party /PartyTaxScheme /CompanyID
        suppliertaxscheme.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': sellertaxregistration.get({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        # Fixed: 'VAT'
        # +/Invoice /AccountingSupplierParty /Party /PartyTaxScheme /TaxScheme /ID
        suppliertaxscheme.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': 'VAT'})

    for buyertaxregistration in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'BuyerTradeParty'}, {'BOTSID': ram+'SpecifiedTaxRegistration'}):

        customertaxscheme = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AccountingCustomerParty'}, {'BOTSID': cac+'Party'}, {'BOTSID': cac+'PartyTaxScheme'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /BuyerTradeParty /SpecifiedTaxRegistration /ID
        # +/Invoice /AccountingCustomerParty /Party /PartyTaxScheme /CompanyID
        customertaxscheme.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': buyertaxregistration.get({'BOTSID': ram+'SpecifiedTaxRegistration'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        # Fixed: 'VAT'
        # +/Invoice /AccountingCustomerParty /Party /PartyTaxScheme /TaxScheme /ID
        customertaxscheme.put({'BOTSID': cac+'PartyTaxScheme'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': 'VAT'})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeAgreement /SpecifiedProcuringProject /ID
    # +/Invoice /ProjectReference /ID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'ProjectReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeAgreement'}, {'BOTSID': ram+'SpecifiedProcuringProject'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ActualDeliverySupplyChainEvent /OccurrenceDateTime /DateTimeString
    # +/Invoice /Delivery /ActualDeliveryDate
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cbc+'ActualDeliveryDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ActualDeliverySupplyChainEvent'}, {'BOTSID': ram+'OccurrenceDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ReceivingAdviceReferencedDocument /IssuerAssignedID
    # +/Invoice /ReceiptDocumentReference /ID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'ReceiptDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ReceivingAdviceReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    for globalid3 in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'GlobalID'}):

        delivery = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /GlobalID /GlobalID__schemeID
        # +/Invoice /Delivery /DeliveryLocation /ID /ID__schemeID
        delivery.put({'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': globalid3.get({'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': None})})

    for id3 in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'ID'}):

        delivery = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /ID
        # +/Invoice /Delivery /DeliveryLocation /ID
        delivery.put({'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': id3.get({'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /ID /ID__schemeID
        # +/Invoice /Delivery /DeliveryLocation /ID /ID__schemeID
        delivery.put({'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': id3.get({'BOTSID': ram+'ID', ram+'ID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /Name
    # +/Invoice /Delivery /DeliveryLocation /Description
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cbc+'Description', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CityName
    # +/Invoice /Delivery /DeliveryLocation /Address /CityName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'CityName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CityName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CountryID
    # +/Invoice /Delivery /DeliveryLocation /Address /Country /IdentificationCode
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cac+'Country'}, {'BOTSID': cbc+'IdentificationCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountryID', 'BOTSCONTENT': None})})

    for countrysubdivisionname4 in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'CountrySubDivisionName'}):

        delivery = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /CountrySubDivisionName
        # +/Invoice /Delivery /DeliveryLocation /Address /CountrySubentity
        delivery.put({'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'CountrySubentity', 'BOTSCONTENT': countrysubdivisionname4.get({'BOTSID': ram+'CountrySubDivisionName', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineOne
    # +/Invoice /Delivery /DeliveryLocation /Address /StreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'StreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineOne', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineThree
    # +/Invoice /Delivery /DeliveryLocation /Address /AddressLine /Line
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cac+'AddressLine'}, {'BOTSID': cbc+'Line', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineThree', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /LineTwo
    # +/Invoice /Delivery /DeliveryLocation /Address /AdditionalStreetName
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'AdditionalStreetName', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'LineTwo', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeDelivery /ShipToTradeParty /PostalTradeAddress /PostcodeCode
    # +/Invoice /Delivery /DeliveryLocation /Address /PostalZone
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'Delivery'}, {'BOTSID': cac+'DeliveryLocation'}, {'BOTSID': cac+'Address'}, {'BOTSID': cbc+'PostalZone', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeDelivery'}, {'BOTSID': ram+'ShipToTradeParty'}, {'BOTSID': ram+'PostalTradeAddress'}, {'BOTSID': ram+'PostcodeCode', 'BOTSCONTENT': None})})

    # update for nocheck
    taxtotal = None

    for taxtotalamount in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxTotalAmount'}):

        taxtotal = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxTotal'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxTotalAmount
        # +/Invoice /TaxTotal /TaxAmount
        taxtotal.put({'BOTSID': cac+'TaxTotal'}, {'BOTSID': cbc+'TaxAmount', 'BOTSCONTENT': taxtotalamount.get({'BOTSID': ram+'TaxTotalAmount', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxTotalAmount /TaxTotalAmount__currencyID
        # +/Invoice /TaxTotal /TaxAmount /TaxAmount__currencyID
        taxtotal.put({'BOTSID': cac+'TaxTotal'}, {'BOTSID': cbc+'TaxAmount', cbc+'TaxAmount__currencyID': taxtotalamount.get({'BOTSID': ram+'TaxTotalAmount', ram+'TaxTotalAmount__currencyID': None})})

    if not taxtotal:
        taxtotal = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'TaxTotal'})

    for applicabletradetax in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'}):

        taxsubtotal = taxtotal.putloop({'BOTSID': cac+'TaxTotal'}, {'BOTSID': cac+'TaxSubtotal'})

        # Fixed: 'VAT'
        # +/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxScheme /ID
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': 'VAT'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /BasisAmount
        # +/Invoice /TaxTotal /TaxSubtotal /TaxableAmount
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxableAmount', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /BasisAmount /BasisAmount__currencyID
        # +/Invoice /TaxTotal /TaxSubtotal /TaxableAmount /TaxableAmount__currencyID
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxableAmount', cbc+'TaxableAmount__currencyID': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'BasisAmount', ram+'BasisAmount__currencyID': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CalculatedAmount
        # +/Invoice /TaxTotal /TaxSubtotal /TaxAmount
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxAmount', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CalculatedAmount', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CalculatedAmount /CalculatedAmount__currencyID
        # +/Invoice /TaxTotal /TaxSubtotal /TaxAmount /TaxAmount__currencyID
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'TaxAmount', cbc+'TaxAmount__currencyID': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CalculatedAmount', ram+'CalculatedAmount__currencyID': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /ExemptionReason
        # +/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxExemptionReason
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'TaxExemptionReason', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'ExemptionReason', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /CategoryCode
        # +/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxScheme /TaxTypeCode
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'TaxTypeCode', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /ExemptionReasonCode
        # +/Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxExemptionReasonCode
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'TaxExemptionReasonCode', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'ExemptionReasonCode', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /RateApplicablePercent
        # +/Invoice /TaxTotal /TaxSubtotal /Percent
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /TypeCode
        # +/Invoice /TaxTotal /TaxSubtotal /TaxCategory /ID
        taxsubtotal.put({'BOTSID': cac+'TaxSubtotal'}, {'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': applicabletradetax.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ApplicableTradeTax /TaxPointDate /DateString
    # +/Invoice /TaxPointDate
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'TaxPointDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'TaxPointDate'}, {'BOTSID': udt+'DateString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /BillingSpecifiedPeriod /EndDateTime /DateTimeString
    # +/Invoice /InvoicePeriod /EndDate
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'EndDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'EndDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /BillingSpecifiedPeriod /StartDateTime /DateTimeString
    # +/Invoice /InvoicePeriod /StartDate
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'StartDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'StartDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /CreditorReferenceID
    # +/Invoice /PaymentMeans /PaymentMandate /PayerFinancialAccount /ID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PaymentMandate'}, {'BOTSID': cac+'PayerFinancialAccount'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'CreditorReferenceID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceCurrencyCode
    # +/Invoice /DocumentCurrencyCode
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'DocumentCurrencyCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceCurrencyCode', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceReferencedDocument /FormattedIssueDateTime /DateTimeString
    # +/Invoice /BillingReference /InvoiceDocumentReference /IssueDate
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'BillingReference'}, {'BOTSID': cac+'InvoiceDocumentReference'}, {'BOTSID': cbc+'IssueDate', 'BOTSCONTENT': transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceReferencedDocument'}, {'BOTSID': ram+'FormattedIssueDateTime'}, {'BOTSID': qdt+'DateTimeString', 'BOTSCONTENT': None}))})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /InvoiceReferencedDocument /IssuerAssignedID
    # +/Invoice /BillingReference /InvoiceDocumentReference /ID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'BillingReference'}, {'BOTSID': cac+'InvoiceDocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'InvoiceReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

    # for globalid4 in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'GlobalID'}):

        # partyidentification3 = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyIdentification'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /GlobalID /GlobalID__schemeID
        # +/Invoice /PayeeParty /PartyIdentification /ID /ID__schemeID
        # partyidentification3.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': globalid4.get({'BOTSID': ram+'GlobalID', ram+'GlobalID__schemeID': None})})

    for id4 in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'ID'}):

        partyidentification3 = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyIdentification'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /ID
        # +/Invoice /PayeeParty /PartyIdentification /ID
        partyidentification3.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': id4.get({'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /ID /ID__schemeID
        # +/Invoice /PayeeParty /PartyIdentification /ID /ID__schemeID
        partyidentification3.put({'BOTSID': cac+'PartyIdentification'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': id4.get({'BOTSID': ram+'ID', ram+'ID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /Name
    # +/Invoice /PayeeParty /PartyName /Name
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyName'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'Name', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /SpecifiedLegalOrganization /ID
    # +/Invoice /PayeeParty /PartyLegalEntity /CompanyID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /PayeeTradeParty /SpecifiedLegalOrganization /ID /ID__schemeID
    # +/Invoice /PayeeParty /PartyLegalEntity /CompanyID /CompanyID__schemeID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PayeeParty'}, {'BOTSID': cac+'PartyLegalEntity'}, {'BOTSID': cbc+'CompanyID', cbc+'CompanyID__schemeID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'PayeeTradeParty'}, {'BOTSID': ram+'SpecifiedLegalOrganization'}, {'BOTSID': ram+'ID', ram+'ID__schemeID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /ReceivableSpecifiedTradeAccountingAccount /ID
    # +/Invoice /AccountingCost
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'AccountingCost', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'ReceivableSpecifiedTradeAccountingAccount'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

    for specifiedtradeallowancecharge in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}):

        allowancecharge = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'AllowanceCharge'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount
        # +/Invoice /AllowanceCharge /Amount
        allowancecharge.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': specifiedtradeallowancecharge.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount
        # +/Invoice /AllowanceCharge /BaseAmount
        allowancecharge.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': specifiedtradeallowancecharge.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CalculationPercent
        # +/Invoice /AllowanceCharge /MultiplierFactorNumeric
        allowancecharge.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'MultiplierFactorNumeric', 'BOTSCONTENT': specifiedtradeallowancecharge.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CalculationPercent', 'BOTSCONTENT': None})})

        for categorytradetax in specifiedtradeallowancecharge.getloop({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'CategoryTradeTax'}):

            taxcategory = allowancecharge.putloop({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cac+'TaxCategory'})

            # Fixed: 'VAT'
            # +/Invoice /AllowanceCharge /TaxCategory /TaxScheme /ID
            taxcategory.put({'BOTSID': cac+'TaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': 'VAT'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /RateApplicablePercent
            # +/Invoice /AllowanceCharge /TaxCategory /Percent
            taxcategory.put({'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': categorytradetax.get({'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeAllowanceCharge /CategoryTradeTax /TypeCode
            # +/Invoice /AllowanceCharge /TaxCategory /ID
            taxcategory.put({'BOTSID': cac+'TaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': categorytradetax.get({'BOTSID': ram+'CategoryTradeTax'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': None})})

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

        paymentterms = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PaymentTerms'})

        for description3 in specifiedtradepaymentterms.getloop({'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'Description'}):

            note2 = paymentterms.putloop({'BOTSID': cac+'PaymentTerms'}, {'BOTSID': cbc+'Note'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /Description
            # +/Invoice /PaymentTerms /Note
            note2.put({'BOTSID': cbc+'Note', 'BOTSCONTENT': description3.get({'BOTSID': ram+'Description', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /AllowanceTotalAmount
    # +/Invoice /LegalMonetaryTotal /AllowanceTotalAmount
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'AllowanceTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'AllowanceTotalAmount', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /AllowanceTotalAmount /AllowanceTotalAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /AllowanceTotalAmount /AllowanceTotalAmount__currencyID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'AllowanceTotalAmount', cbc+'AllowanceTotalAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'AllowanceTotalAmount', ram+'AllowanceTotalAmount__currencyID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /ChargeTotalAmount
    # +/Invoice /LegalMonetaryTotal /ChargeTotalAmount
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'ChargeTotalAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'ChargeTotalAmount', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /ChargeTotalAmount /ChargeTotalAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /ChargeTotalAmount /ChargeTotalAmount__currencyID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'ChargeTotalAmount', cbc+'ChargeTotalAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'ChargeTotalAmount', ram+'ChargeTotalAmount__currencyID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /DuePayableAmount
    # +/Invoice /LegalMonetaryTotal /PayableAmount
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'DuePayableAmount', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /DuePayableAmount /DuePayableAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /PayableAmount /PayableAmount__currencyID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableAmount', cbc+'PayableAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'DuePayableAmount', ram+'DuePayableAmount__currencyID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /GrandTotalAmount
    # +/Invoice /LegalMonetaryTotal /TaxInclusiveAmount
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxInclusiveAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'GrandTotalAmount', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /GrandTotalAmount /GrandTotalAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /TaxInclusiveAmount /TaxInclusiveAmount__currencyID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxInclusiveAmount', cbc+'TaxInclusiveAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'GrandTotalAmount', ram+'GrandTotalAmount__currencyID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /LineTotalAmount
    # +/Invoice /LegalMonetaryTotal /LineExtensionAmount
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'LineExtensionAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /LineTotalAmount /LineTotalAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /LineExtensionAmount /LineExtensionAmount__currencyID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'LineExtensionAmount', cbc+'LineExtensionAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', ram+'LineTotalAmount__currencyID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /RoundingAmount
    # +/Invoice /LegalMonetaryTotal /PayableRoundingAmount
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableRoundingAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'RoundingAmount', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /RoundingAmount /RoundingAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /PayableRoundingAmount /PayableRoundingAmount__currencyID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PayableRoundingAmount', cbc+'PayableRoundingAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'RoundingAmount', ram+'RoundingAmount__currencyID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxBasisTotalAmount
    # +/Invoice /LegalMonetaryTotal /TaxExclusiveAmount
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxExclusiveAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxBasisTotalAmount', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TaxBasisTotalAmount /TaxBasisTotalAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /TaxExclusiveAmount /TaxExclusiveAmount__currencyID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'TaxExclusiveAmount', cbc+'TaxExclusiveAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TaxBasisTotalAmount', ram+'TaxBasisTotalAmount__currencyID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TotalPrepaidAmount
    # +/Invoice /LegalMonetaryTotal /PrepaidAmount
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PrepaidAmount', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TotalPrepaidAmount', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementHeaderMonetarySummation /TotalPrepaidAmount /TotalPrepaidAmount__currencyID
    # +/Invoice /LegalMonetaryTotal /PrepaidAmount /PrepaidAmount__currencyID
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'LegalMonetaryTotal'}, {'BOTSID': cbc+'PrepaidAmount', cbc+'PrepaidAmount__currencyID': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementHeaderMonetarySummation'}, {'BOTSID': ram+'TotalPrepaidAmount', ram+'TotalPrepaidAmount__currencyID': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /DueDateDateTime /DateTimeString
    duedate = transformdate(inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradePaymentTerms'}, {'BOTSID': ram+'DueDateDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))

    for specifiedtradesettlementpaymentmeans in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}):

        paymentmeans = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'PaymentMeans'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradePaymentTerms /DueDateDateTime /DateTimeString
        # +/Invoice /PaymentMeans /PaymentDueDate
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentDueDate', 'BOTSCONTENT': duedate})

        # Fixed: 'N/A'
        # +/Invoice /PaymentMeans /CardAccount /NetworkID
        # paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'CardAccount'}, {'BOTSID': cbc+'NetworkID', 'BOTSCONTENT': 'N/A'})

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

        name = ''
        for information in specifiedtradesettlementpaymentmeans.getloop({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'Information'}):
            name += information.get({'BOTSID': ram+'Information', 'BOTSCONTENT': None})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /Information
        # +/Invoice /PaymentMeans /PaymentMeansCode /PaymentMeansCode__name
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', cbc+'PaymentMeansCode__name': name})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /TypeCode
        # +/Invoice /PaymentMeans /PaymentMeansCode
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cbc+'PaymentMeansCode', 'BOTSCONTENT': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'TypeCode', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayeePartyCreditorFinancialAccount /AccountName
        # +/Invoice /PaymentMeans /PayeeFinancialAccount /Name
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PayeeFinancialAccount'}, {'BOTSID': cbc+'Name', 'BOTSCONTENT': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayeePartyCreditorFinancialAccount'}, {'BOTSID': ram+'AccountName', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayeePartyCreditorFinancialAccount /IBANID
        # +/Invoice /PaymentMeans /PayeeFinancialAccount /ID
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PayeeFinancialAccount'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayeePartyCreditorFinancialAccount'}, {'BOTSID': ram+'IBANID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /SpecifiedTradeSettlementPaymentMeans /PayerSpecifiedDebtorFinancialInstitution /BICID
        # +/Invoice /PaymentMeans /PayeeFinancialAccount /FinancialInstitutionBranch /ID
        paymentmeans.put({'BOTSID': cac+'PaymentMeans'}, {'BOTSID': cac+'PayeeFinancialAccount'}, {'BOTSID': cac+'FinancialInstitutionBranch'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': specifiedtradesettlementpaymentmeans.get({'BOTSID': ram+'SpecifiedTradeSettlementPaymentMeans'}, {'BOTSID': ram+'PayerSpecifiedDebtorFinancialInstitution'}, {'BOTSID': ram+'BICID', 'BOTSCONTENT': None})})

    # -/CrossIndustryInvoice /SupplyChainTradeTransaction /ApplicableHeaderTradeSettlement /TaxCurrencyCode
    # +/Invoice /TaxCurrencyCode
    out.put({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cbc+'TaxCurrencyCode', 'BOTSCONTENT': inn.get({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'ApplicableHeaderTradeSettlement'}, {'BOTSID': ram+'TaxCurrencyCode', 'BOTSCONTENT': None})})

    for includedsupplychaintradelineitem in inn.getloop({'BOTSID': rsm+'CrossIndustryInvoice'}, {'BOTSID': rsm+'SupplyChainTradeTransaction'}, {'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}):

        invoiceline = out.putloop({'BOTSID': xmlns+'Invoice'}, {'BOTSID': cac+'InvoiceLine'})

        item = invoiceline.putloop({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Item'})

        for includednote2 in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'AssociatedDocumentLineDocument'}, {'BOTSID': ram+'IncludedNote'}):

            for content2 in includednote2.getloop({'BOTSID': ram+'IncludedNote'}, {'BOTSID': ram+'Content'}):

                note3 = invoiceline.putloop({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'Note'})

                # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /AssociatedDocumentLineDocument /IncludedNote /Content
                # +/Invoice /InvoiceLine /Note
                note3.put({'BOTSID': cbc+'Note', 'BOTSCONTENT': content2.get({'BOTSID': ram+'Content', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /AssociatedDocumentLineDocument /LineID
        # +/Invoice /InvoiceLine /ID
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'AssociatedDocumentLineDocument'}, {'BOTSID': ram+'LineID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /BuyerOrderReferencedDocument /LineID
        # +/Invoice /InvoiceLine /OrderLineReference /LineID
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'OrderLineReference'}, {'BOTSID': cbc+'LineID', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'BuyerOrderReferencedDocument'}, {'BOTSID': ram+'LineID', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /BasisQuantity
        # +/Invoice /InvoiceLine /Price /BaseQuantity
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /BasisQuantity /BasisQuantity__unitCode
        # +/Invoice /InvoiceLine /Price /BaseQuantity /BaseQuantity__unitCode
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'BaseQuantity', cbc+'BaseQuantity__unitCode': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'BasisQuantity', ram+'BasisQuantity__unitCode': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /ChargeAmount
        # +/Invoice /InvoiceLine /Price /PriceAmount
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'PriceAmount', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /NetPriceProductTradePrice /ChargeAmount /ChargeAmount__currencyID
        # +/Invoice /InvoiceLine /Price /PriceAmount /PriceAmount__currencyID
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cbc+'PriceAmount', cbc+'PriceAmount__currencyID': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'NetPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', ram+'ChargeAmount__currencyID': None})})

        # if includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'AppliedTradeAllowanceCharge'}):
            
        for appliedtradeallowancecharge in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'AppliedTradeAllowanceCharge'}):

            allowancecharge2 = invoiceline.putloop({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'Price'}, {'BOTSID': cac+'AllowanceCharge'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ActualAmount
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /Amount
            allowancecharge2.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': appliedtradeallowancecharge.get({'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ActualAmount /ActualAmount__currencyID
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /Amount /Amount__currencyID
            allowancecharge2.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', cbc+'Amount__currencyID': appliedtradeallowancecharge.get({'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', ram+'ActualAmount__currencyID': None})})

            # Fixed: 'False'
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /ChargeIndicator
            allowancecharge2.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'ChargeIndicator', 'BOTSCONTENT': 'False'})

            # !!!!!
            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /ChargeAmount
            # +/Invoice /InvoiceLine /Price /AllowanceCharge /BaseAmount
            # allowancecharge2.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'ChargeAmount', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeDelivery /BilledQuantity
        # +/Invoice /InvoiceLine /InvoicedQuantity
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'InvoicedQuantity', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeDelivery'}, {'BOTSID': ram+'BilledQuantity', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeDelivery /BilledQuantity /BilledQuantity__unitCode
        # +/Invoice /InvoiceLine /InvoicedQuantity /InvoicedQuantity__unitCode
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'InvoicedQuantity', cbc+'InvoicedQuantity__unitCode': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeDelivery'}, {'BOTSID': ram+'BilledQuantity', ram+'BilledQuantity__unitCode': None})})

        for additionalreferenceddocument2 in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'AdditionalReferencedDocument'}):

            documentreference = invoiceline.putloop({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'DocumentReference'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /AdditionalReferencedDocument /IssuerAssignedID
            # +/Invoice /InvoiceLine /DocumentReference /ID
            documentreference.put({'BOTSID': cac+'DocumentReference'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': additionalreferenceddocument2.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /AdditionalReferencedDocument /IssuerAssignedID /IssuerAssignedID__schemeID
            # +/Invoice /InvoiceLine /DocumentReference /ID /ID__schemeID
            documentreference.put({'BOTSID': cac+'DocumentReference'}, {'BOTSID': cbc+'ID', cbc+'ID__schemeID': additionalreferenceddocument2.get({'BOTSID': ram+'AdditionalReferencedDocument'}, {'BOTSID': ram+'IssuerAssignedID', ram+'IssuerAssignedID__schemeID': None})})

        for applicabletradetax2 in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'ApplicableTradeTax'}):

            classifiedtaxcategory = item.putloop({'BOTSID': cac+'Item'}, {'BOTSID': cac+'ClassifiedTaxCategory'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ApplicableTradeTax /CategoryCode
            # +/Invoice /InvoiceLine /Item /ClassifiedTaxCategory /ID
            classifiedtaxcategory.put({'BOTSID': cac+'ClassifiedTaxCategory'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': applicabletradetax2.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'CategoryCode', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ApplicableTradeTax /RateApplicablePercent
            # +/Invoice /InvoiceLine /Item /ClassifiedTaxCategory /Percent
            classifiedtaxcategory.put({'BOTSID': cac+'ClassifiedTaxCategory'}, {'BOTSID': cbc+'Percent', 'BOTSCONTENT': applicabletradetax2.get({'BOTSID': ram+'ApplicableTradeTax'}, {'BOTSID': ram+'RateApplicablePercent', 'BOTSCONTENT': None})})

            # Fixed: 'VAT'
            # +/Invoice /InvoiceLine /Item /ClassifiedTaxCategory /TaxScheme /ID
            classifiedtaxcategory.put({'BOTSID': cac+'ClassifiedTaxCategory'}, {'BOTSID': cac+'TaxScheme'}, {'BOTSID': cbc+'ID', 'BOTSCONTENT': 'VAT'})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /BillingSpecifiedPeriod /EndDateTime /DateTimeString
        # +/Invoice /InvoiceLine /InvoicePeriod /EndDate
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'EndDate', 'BOTSCONTENT': transformdate(includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'EndDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /BillingSpecifiedPeriod /StartDateTime /DateTimeString
        # +/Invoice /InvoiceLine /InvoicePeriod /StartDate
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'InvoicePeriod'}, {'BOTSID': cbc+'StartDate', 'BOTSCONTENT': transformdate(includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'BillingSpecifiedPeriod'}, {'BOTSID': ram+'StartDateTime'}, {'BOTSID': udt+'DateTimeString', 'BOTSCONTENT': None}))})

        for receivablespecifiedtradeaccountingaccount2 in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'ReceivableSpecifiedTradeAccountingAccount'}):

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /ReceivableSpecifiedTradeAccountingAccount /ID
            # +/Invoice /InvoiceLine /AccountingCost
            invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'AccountingCost', 'BOTSCONTENT': receivablespecifiedtradeaccountingaccount2.get({'BOTSID': ram+'ReceivableSpecifiedTradeAccountingAccount'}, {'BOTSID': ram+'ID', 'BOTSCONTENT': None})})

        for specifiedtradeallowancecharge2 in includedsupplychaintradelineitem.getloop({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}):

            allowancecharge3 = invoiceline.putloop({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cac+'AllowanceCharge'})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount
            # +/Invoice /InvoiceLine /AllowanceCharge /Amount
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', 'BOTSCONTENT': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ActualAmount /ActualAmount__currencyID
            # +/Invoice /InvoiceLine /AllowanceCharge /Amount /Amount__currencyID
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'Amount', cbc+'Amount__currencyID': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ActualAmount', ram+'ActualAmount__currencyID': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount
            # +/Invoice /InvoiceLine /AllowanceCharge /BaseAmount
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', 'BOTSCONTENT': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /BasisAmount /BasisAmount__currencyID
            # +/Invoice /InvoiceLine /AllowanceCharge /BaseAmount /BaseAmount__currencyID
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'BaseAmount', cbc+'BaseAmount__currencyID': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'BasisAmount', ram+'BasisAmount__currencyID': None})})

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

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /Reason
            # +/Invoice /InvoiceLine /AllowanceCharge /AllowanceChargeReason
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReason', 'BOTSCONTENT': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'Reason', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeAllowanceCharge /ReasonCode
            # +/Invoice /InvoiceLine /AllowanceCharge /AllowanceChargeReasonCode
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'AllowanceChargeReasonCode', 'BOTSCONTENT': specifiedtradeallowancecharge2.get({'BOTSID': ram+'SpecifiedTradeAllowanceCharge'}, {'BOTSID': ram+'ReasonCode', 'BOTSCONTENT': None})})

            # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeAgreement /GrossPriceProductTradePrice /AppliedTradeAllowanceCharge /ChargeIndicator /IndicatorString
            # +/Invoice /InvoiceLine /AllowanceCharge /ChargeIndicator
            allowancecharge3.put({'BOTSID': cac+'AllowanceCharge'}, {'BOTSID': cbc+'ChargeIndicator', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeAgreement'}, {'BOTSID': ram+'GrossPriceProductTradePrice'}, {'BOTSID': ram+'AppliedTradeAllowanceCharge'}, {'BOTSID': ram+'ChargeIndicator'}, {'BOTSID': udt+'IndicatorString', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeSettlementLineMonetarySummation /LineTotalAmount
        # +/Invoice /InvoiceLine /LineExtensionAmount
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'LineExtensionAmount', 'BOTSCONTENT': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementLineMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', 'BOTSCONTENT': None})})

        # -/CrossIndustryInvoice /SupplyChainTradeTransaction /IncludedSupplyChainTradeLineItem /SpecifiedLineTradeSettlement /SpecifiedTradeSettlementLineMonetarySummation /LineTotalAmount /LineTotalAmount__currencyID
        # +/Invoice /InvoiceLine /LineExtensionAmount /LineExtensionAmount__currencyID
        invoiceline.put({'BOTSID': cac+'InvoiceLine'}, {'BOTSID': cbc+'LineExtensionAmount', cbc+'LineExtensionAmount__currencyID': includedsupplychaintradelineitem.get({'BOTSID': ram+'IncludedSupplyChainTradeLineItem'}, {'BOTSID': ram+'SpecifiedLineTradeSettlement'}, {'BOTSID': ram+'SpecifiedTradeSettlementLineMonetarySummation'}, {'BOTSID': ram+'LineTotalAmount', ram+'LineTotalAmount__currencyID': None})})

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
