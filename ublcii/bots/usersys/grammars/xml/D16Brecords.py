# -*- coding: utf-8 -*-

version = '100.D16B'

rsm = '{urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100}'
qdt = '{urn:un:unece:uncefact:data:standard:QualifiedDataType:100}'
udt = '{urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100}'
ram = '{urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100}'


recorddefs = {
rsm+'CrossIndustryInvoice':
    [
    ['BOTSID', 'M', 256, 'AN'],
    [rsm+'CrossIndustryInvoice__xmlns:xsi', 'C', 256, 'AN'],
    ],
rsm+'ExchangedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
rsm+'ExchangedDocumentContext':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
rsm+'SupplyChainTradeTransaction':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
rsm+'ValuationBreakdownStatement':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
qdt+'DateTimeString':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [qdt+'DateTimeString__format', 'C', 256, 'AN'],
    ],
ram+'AbsolutePresenceVolumeMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'AbsolutePresenceVolumeMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'AbsolutePresenceVolumeMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'AbsolutePresenceWeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'AbsolutePresenceWeightMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'AbsolutePresenceWeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'Abstract':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Abstract__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Abstract__languageID', 'C', 256, 'AN'],
    ],
ram+'Access':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Access__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Access__languageID', 'C', 256, 'AN'],
    ],
ram+'AccessAvailabilitySpecifiedPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AccountName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'AccountName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'AccountName__languageID', 'C', 256, 'AN'],
    ],
ram+'ActualAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ActualAmount__currencyID', 'C', 256, 'AN'],
    [ram+'ActualAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'ActualDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ActualDeliverySupplyChainEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ActualDespatchSupplyChainEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ActualDiscountAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ActualDiscountAmount__currencyID', 'C', 256, 'AN'],
    [ram+'ActualDiscountAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'ActualPenaltyAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ActualPenaltyAmount__currencyID', 'C', 256, 'AN'],
    [ram+'ActualPenaltyAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'ActualPickUpSupplyChainEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ActualQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ActualQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'ActualQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'ActualQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'ActualQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'ActualQuantityPercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ActualQuantityPercent__format', 'C', 256, 'AN'],
    ],
ram+'ActualQuantityWorkItemDimension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ActualReceiptSupplyChainEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ActualTradeCurrencyExchange':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ActualWorkItemComplexDescription':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AdditionalReferenceReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AdditionalReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AdditionalStreetName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'AdditionalStreetName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'AdditionalStreetName__languageID', 'C', 256, 'AN'],
    ],
ram+'AgencyID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'AgencyID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'AgencyID__schemeID', 'C', 256, 'AN'],
    [ram+'AgencyID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'AgencyID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'AgencyID__schemeName', 'C', 256, 'AN'],
    [ram+'AgencyID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'AgencyID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'AllowanceCharge':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'AllowanceCharge__languageLocaleID', 'C', 256, 'AN'],
    [ram+'AllowanceCharge__languageID', 'C', 256, 'AN'],
    ],
ram+'AllowanceChargeBasisAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'AllowanceChargeBasisAmount__currencyID', 'C', 256, 'AN'],
    [ram+'AllowanceChargeBasisAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'AllowanceTotalAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'AllowanceTotalAmount__currencyID', 'C', 256, 'AN'],
    [ram+'AllowanceTotalAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'AlternativeClassificationCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'AlternativeClassificationCode__listName', 'C', 256, 'AN'],
    [ram+'AlternativeClassificationCode__name', 'C', 256, 'AN'],
    [ram+'AlternativeClassificationCode__languageID', 'C', 256, 'AN'],
    [ram+'AlternativeClassificationCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'AlternativeClassificationCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'AlternativeClassificationCode__listID', 'C', 256, 'AN'],
    [ram+'AlternativeClassificationCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'AlternativeClassificationCode__listURI', 'C', 256, 'AN'],
    [ram+'AlternativeClassificationCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'AltitudeMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'AltitudeMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'AltitudeMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'AmountTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'AmountTypeCode__listID', 'C', 256, 'AN'],
    [ram+'AmountTypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'AmountTypeCode__listVersionID', 'C', 256, 'AN'],
    [ram+'AmountTypeCode__listURI', 'C', 256, 'AN'],
    ],
ram+'ApplicableDisposalInstructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableHeaderTradeAgreement':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableHeaderTradeDelivery':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableHeaderTradeSettlement':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableMaterialGoodsCharacteristic':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableProductCharacteristic':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableProductCharacteristicCondition':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableReferencedStandard':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableReturnableAssetInstructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableTradeDeliveryTerms':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableTradePaymentDiscountTerms':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableTradePaymentPenaltyTerms':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableTradeProduct':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableTradeSettlementFinancialCard':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicableTradeTax':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ApplicationSpecifiedDocumentContextParameter':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AppliedAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'AppliedAmount__currencyID', 'C', 256, 'AN'],
    [ram+'AppliedAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'AppliedFromLogisticsLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AppliedToLogisticsLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AppliedTradeAllowanceCharge':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AppliedTradeTax':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AreaDensityMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'AreaDensityMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'AreaDensityMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'AssociatedDocumentLineDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AssociatedInvoiceAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'AssociatedInvoiceAmount__currencyID', 'C', 256, 'AN'],
    [ram+'AssociatedInvoiceAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'AssociatedReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AssociatedRegisteredTax':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AttachedSpecifiedBinaryFile':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AttachmentBinaryObject':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 999999, 'AN'],
    [ram+'AttachmentBinaryObject__format', 'C', 256, 'AN'],
    [ram+'AttachmentBinaryObject__encodingCode', 'C', 256, 'AN'],
    [ram+'AttachmentBinaryObject__uri', 'C', 256, 'AN'],
    [ram+'AttachmentBinaryObject__filename', 'C', 256, 'AN'],
    [ram+'AttachmentBinaryObject__characterSetCode', 'C', 256, 'AN'],
    [ram+'AttachmentBinaryObject__mimeCode', 'C', 256, 'AN'],
    ],
ram+'AttentionOf':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'AttentionOf__languageLocaleID', 'C', 256, 'AN'],
    [ram+'AttentionOf__languageID', 'C', 256, 'AN'],
    ],
ram+'AustralianBSBID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'AustralianBSBID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'AustralianBSBID__schemeID', 'C', 256, 'AN'],
    [ram+'AustralianBSBID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'AustralianBSBID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'AustralianBSBID__schemeName', 'C', 256, 'AN'],
    [ram+'AustralianBSBID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'AustralianBSBID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'AustrianBankleitzahlID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'AustrianBankleitzahlID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'AustrianBankleitzahlID__schemeID', 'C', 256, 'AN'],
    [ram+'AustrianBankleitzahlID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'AustrianBankleitzahlID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'AustrianBankleitzahlID__schemeName', 'C', 256, 'AN'],
    [ram+'AustrianBankleitzahlID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'AustrianBankleitzahlID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'AuthorName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'AuthorName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'AuthorName__languageID', 'C', 256, 'AN'],
    ],
ram+'AuthorizedLegalRegistration':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'AutomaticDataCaptureMethodTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'AutomaticDataCaptureMethodTypeCode__listID', 'C', 256, 'AN'],
    [ram+'AutomaticDataCaptureMethodTypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'AutomaticDataCaptureMethodTypeCode__listVersionID', 'C', 256, 'AN'],
    [ram+'AutomaticDataCaptureMethodTypeCode__listURI', 'C', 256, 'AN'],
    ],
ram+'BICID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'BICID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'BICID__schemeID', 'C', 256, 'AN'],
    [ram+'BICID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'BICID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'BICID__schemeName', 'C', 256, 'AN'],
    [ram+'BICID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'BICID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'BIMSpecifiedDocumentContextParameter':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BarcodeTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'BarcodeTypeCode__listName', 'C', 256, 'AN'],
    [ram+'BarcodeTypeCode__name', 'C', 256, 'AN'],
    [ram+'BarcodeTypeCode__languageID', 'C', 256, 'AN'],
    [ram+'BarcodeTypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'BarcodeTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'BarcodeTypeCode__listID', 'C', 256, 'AN'],
    [ram+'BarcodeTypeCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'BarcodeTypeCode__listURI', 'C', 256, 'AN'],
    [ram+'BarcodeTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'BasisAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'BasisAmount__currencyID', 'C', 256, 'AN'],
    [ram+'BasisAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'BasisDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BasisPeriodMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'BasisPeriodMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'BasisPeriodMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'BasisQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'BasisQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'BasisQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'BasisQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'BasisQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'BatchID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'BatchID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'BatchID__schemeID', 'C', 256, 'AN'],
    [ram+'BatchID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'BatchID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'BatchID__schemeName', 'C', 256, 'AN'],
    [ram+'BatchID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'BatchID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'BestBeforeDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BilledQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'BilledQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'BilledQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'BilledQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'BilledQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'BillingSpecifiedPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BrandName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'BrandName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'BrandName__languageID', 'C', 256, 'AN'],
    ],
ram+'BrandOwnerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BreakdownWorkItemQuantityAnalysis':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BuildingName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'BuildingName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'BuildingName__languageID', 'C', 256, 'AN'],
    ],
ram+'BuildingNumber':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'BuildingNumber__languageLocaleID', 'C', 256, 'AN'],
    [ram+'BuildingNumber__languageID', 'C', 256, 'AN'],
    ],
ram+'BusinessProcessSpecifiedDocumentContextParameter':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BuyerAgentTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BuyerAssignedAccountantTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BuyerAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'BuyerAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'BuyerAssignedID__schemeID', 'C', 256, 'AN'],
    [ram+'BuyerAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'BuyerAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'BuyerAssignedID__schemeName', 'C', 256, 'AN'],
    [ram+'BuyerAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'BuyerAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'BuyerDeductibleTaxSpecifiedTradeAccountingAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BuyerNonDeductibleTaxSpecifiedTradeAccountingAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BuyerOrderReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BuyerReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'BuyerReference__languageLocaleID', 'C', 256, 'AN'],
    [ram+'BuyerReference__languageID', 'C', 256, 'AN'],
    ],
ram+'BuyerRepayableTaxSpecifiedTradeAccountingAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BuyerRequisitionerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BuyerTaxRepresentativeTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'BuyerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'CHIPSParticipantID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CHIPSParticipantID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'CHIPSParticipantID__schemeID', 'C', 256, 'AN'],
    [ram+'CHIPSParticipantID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'CHIPSParticipantID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'CHIPSParticipantID__schemeName', 'C', 256, 'AN'],
    [ram+'CHIPSParticipantID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'CHIPSParticipantID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'CHIPSUniversalID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CHIPSUniversalID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'CHIPSUniversalID__schemeID', 'C', 256, 'AN'],
    [ram+'CHIPSUniversalID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'CHIPSUniversalID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'CHIPSUniversalID__schemeName', 'C', 256, 'AN'],
    [ram+'CHIPSUniversalID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'CHIPSUniversalID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'CalculatedAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'CalculatedAmount__currencyID', 'C', 256, 'AN'],
    [ram+'CalculatedAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'CalculatedRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'CalculatedRate__format', 'C', 256, 'AN'],
    ],
ram+'CalculationBasis':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CalculationBasis__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CalculationBasis__languageID', 'C', 256, 'AN'],
    ],
ram+'CalculationBasisCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CalculationBasisCode__listID', 'C', 256, 'AN'],
    [ram+'CalculationBasisCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'CalculationBasisCode__name', 'C', 256, 'AN'],
    [ram+'CalculationBasisCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'CalculationPercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'CalculationPercent__format', 'C', 256, 'AN'],
    ],
ram+'CalculationSequenceNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'CalculationSequenceNumeric__format', 'C', 256, 'AN'],
    ],
ram+'CanadianPaymentsAssociationID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CanadianPaymentsAssociationID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'CanadianPaymentsAssociationID__schemeID', 'C', 256, 'AN'],
    [ram+'CanadianPaymentsAssociationID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'CanadianPaymentsAssociationID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'CanadianPaymentsAssociationID__schemeName', 'C', 256, 'AN'],
    [ram+'CanadianPaymentsAssociationID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'CanadianPaymentsAssociationID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'CardholderName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CardholderName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CardholderName__languageID', 'C', 256, 'AN'],
    ],
ram+'CareOf':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CareOf__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CareOf__languageID', 'C', 256, 'AN'],
    ],
ram+'CarrierTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'CategoryAppliedTax':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'CategoryCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CategoryCode__listName', 'C', 256, 'AN'],
    [ram+'CategoryCode__name', 'C', 256, 'AN'],
    [ram+'CategoryCode__languageID', 'C', 256, 'AN'],
    [ram+'CategoryCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'CategoryCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'CategoryCode__listID', 'C', 256, 'AN'],
    [ram+'CategoryCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'CategoryCode__listURI', 'C', 256, 'AN'],
    [ram+'CategoryCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'CategoryName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CategoryName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CategoryName__languageID', 'C', 256, 'AN'],
    ],
ram+'CategoryTradeTax':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'CertificationEvidenceReferenceReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ChangeReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ChangeReason__languageLocaleID', 'C', 256, 'AN'],
    [ram+'ChangeReason__languageID', 'C', 256, 'AN'],
    ],
ram+'ChangedDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ChangedRecordedStatus':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ChangerName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ChangerName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'ChangerName__languageID', 'C', 256, 'AN'],
    ],
ram+'ChannelCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ChannelCode__listID', 'C', 256, 'AN'],
    [ram+'ChannelCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ChannelCode__listVersionID', 'C', 256, 'AN'],
    [ram+'ChannelCode__listURI', 'C', 256, 'AN'],
    ],
ram+'CharacterSetCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CharacterSetCode__listName', 'C', 256, 'AN'],
    [ram+'CharacterSetCode__name', 'C', 256, 'AN'],
    [ram+'CharacterSetCode__languageID', 'C', 256, 'AN'],
    [ram+'CharacterSetCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'CharacterSetCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'CharacterSetCode__listID', 'C', 256, 'AN'],
    [ram+'CharacterSetCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'CharacterSetCode__listURI', 'C', 256, 'AN'],
    [ram+'CharacterSetCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'CharacteristicCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CharacteristicCode__listID', 'C', 256, 'AN'],
    [ram+'CharacteristicCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'CharacteristicCode__name', 'C', 256, 'AN'],
    [ram+'CharacteristicCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ChargeAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ChargeAmount__currencyID', 'C', 256, 'AN'],
    [ram+'ChargeAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'ChargeCategoryCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ChargeCategoryCode__listName', 'C', 256, 'AN'],
    [ram+'ChargeCategoryCode__name', 'C', 256, 'AN'],
    [ram+'ChargeCategoryCode__languageID', 'C', 256, 'AN'],
    [ram+'ChargeCategoryCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ChargeCategoryCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'ChargeCategoryCode__listID', 'C', 256, 'AN'],
    [ram+'ChargeCategoryCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'ChargeCategoryCode__listURI', 'C', 256, 'AN'],
    [ram+'ChargeCategoryCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ChargeFreeQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ChargeFreeQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'ChargeFreeQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'ChargeFreeQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'ChargeFreeQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'ChargeIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ChargeTotalAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ChargeTotalAmount__currencyID', 'C', 256, 'AN'],
    [ram+'ChargeTotalAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'CityID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CityID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'CityID__schemeID', 'C', 256, 'AN'],
    [ram+'CityID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'CityID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'CityID__schemeName', 'C', 256, 'AN'],
    [ram+'CityID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'CityID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'CityName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CityName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CityName__languageID', 'C', 256, 'AN'],
    ],
ram+'CitySubDivisionName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CitySubDivisionName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CitySubDivisionName__languageID', 'C', 256, 'AN'],
    ],
ram+'ClaimRelatedTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ClassCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ClassCode__listName', 'C', 256, 'AN'],
    [ram+'ClassCode__name', 'C', 256, 'AN'],
    [ram+'ClassCode__languageID', 'C', 256, 'AN'],
    [ram+'ClassCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ClassCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'ClassCode__listID', 'C', 256, 'AN'],
    [ram+'ClassCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'ClassCode__listURI', 'C', 256, 'AN'],
    [ram+'ClassCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ClassName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ClassName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'ClassName__languageID', 'C', 256, 'AN'],
    ],
ram+'ClassProductCharacteristic':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ClearingSystemName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ClearingSystemName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'ClearingSystemName__languageID', 'C', 256, 'AN'],
    ],
ram+'ColourCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ColourCode__listName', 'C', 256, 'AN'],
    [ram+'ColourCode__name', 'C', 256, 'AN'],
    [ram+'ColourCode__languageID', 'C', 256, 'AN'],
    [ram+'ColourCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ColourCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'ColourCode__listID', 'C', 256, 'AN'],
    [ram+'ColourCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'ColourCode__listURI', 'C', 256, 'AN'],
    [ram+'ColourCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ColourDescription':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ColourDescription__languageLocaleID', 'C', 256, 'AN'],
    [ram+'ColourDescription__languageID', 'C', 256, 'AN'],
    ],
ram+'Comment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Comment__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Comment__languageID', 'C', 256, 'AN'],
    ],
ram+'ComparisonMethodCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ComparisonMethodCode__listName', 'C', 256, 'AN'],
    [ram+'ComparisonMethodCode__name', 'C', 256, 'AN'],
    [ram+'ComparisonMethodCode__languageID', 'C', 256, 'AN'],
    [ram+'ComparisonMethodCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ComparisonMethodCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'ComparisonMethodCode__listID', 'C', 256, 'AN'],
    [ram+'ComparisonMethodCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'ComparisonMethodCode__listURI', 'C', 256, 'AN'],
    [ram+'ComparisonMethodCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'CompleteDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'CompleteNumber':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CompleteNumber__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CompleteNumber__languageID', 'C', 256, 'AN'],
    ],
ram+'ComponentWorkItemDimension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ConditionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ConditionCode__listName', 'C', 256, 'AN'],
    [ram+'ConditionCode__name', 'C', 256, 'AN'],
    [ram+'ConditionCode__languageID', 'C', 256, 'AN'],
    [ram+'ConditionCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ConditionCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'ConditionCode__listID', 'C', 256, 'AN'],
    [ram+'ConditionCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'ConditionCode__listURI', 'C', 256, 'AN'],
    [ram+'ConditionCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ConsigneeTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ConsignorTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ConsumptionReportReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'Content':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Content__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Content__languageID', 'C', 256, 'AN'],
    ],
ram+'ContentAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ContentAmount__currencyID', 'C', 256, 'AN'],
    [ram+'ContentAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'ContentCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ContentCode__listName', 'C', 256, 'AN'],
    [ram+'ContentCode__name', 'C', 256, 'AN'],
    [ram+'ContentCode__languageID', 'C', 256, 'AN'],
    [ram+'ContentCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ContentCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'ContentCode__listID', 'C', 256, 'AN'],
    [ram+'ContentCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'ContentCode__listURI', 'C', 256, 'AN'],
    [ram+'ContentCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ContentDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ContentLayerQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ContentLayerQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'ContentLayerQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'ContentLayerQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'ContentLayerQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'ContentTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ContentTypeCode__listName', 'C', 256, 'AN'],
    [ram+'ContentTypeCode__name', 'C', 256, 'AN'],
    [ram+'ContentTypeCode__languageID', 'C', 256, 'AN'],
    [ram+'ContentTypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ContentTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'ContentTypeCode__listID', 'C', 256, 'AN'],
    [ram+'ContentTypeCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'ContentTypeCode__listURI', 'C', 256, 'AN'],
    [ram+'ContentTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ContinuousIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ContractReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ContractualLanguageCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ContractualLanguageCode__listName', 'C', 256, 'AN'],
    [ram+'ContractualLanguageCode__name', 'C', 256, 'AN'],
    [ram+'ContractualLanguageCode__languageID', 'C', 256, 'AN'],
    [ram+'ContractualLanguageCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ContractualLanguageCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'ContractualLanguageCode__listID', 'C', 256, 'AN'],
    [ram+'ContractualLanguageCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'ContractualLanguageCode__listURI', 'C', 256, 'AN'],
    [ram+'ContractualLanguageCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ControlRequirementIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ConversionRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ConversionRate__format', 'C', 256, 'AN'],
    ],
ram+'ConversionRateDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'CopyIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'CostReferenceDimensionPattern':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CostReferenceDimensionPattern__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CostReferenceDimensionPattern__languageID', 'C', 256, 'AN'],
    ],
ram+'CountryID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CountryID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'CountryID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'CountryID__schemeID', 'C', 256, 'AN'],
    ],
ram+'CountryName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CountryName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CountryName__languageID', 'C', 256, 'AN'],
    ],
ram+'CountrySubDivisionID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CountrySubDivisionID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'CountrySubDivisionID__schemeID', 'C', 256, 'AN'],
    [ram+'CountrySubDivisionID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'CountrySubDivisionID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'CountrySubDivisionID__schemeName', 'C', 256, 'AN'],
    [ram+'CountrySubDivisionID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'CountrySubDivisionID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'CountrySubDivisionName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CountrySubDivisionName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CountrySubDivisionName__languageID', 'C', 256, 'AN'],
    ],
ram+'CreationDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'CreationSpecifiedBinaryFile':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'CreditAvailableAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'CreditAvailableAmount__currencyID', 'C', 256, 'AN'],
    [ram+'CreditAvailableAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'CreditLimitAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'CreditLimitAmount__currencyID', 'C', 256, 'AN'],
    [ram+'CreditLimitAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'CreditReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CreditReason__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CreditReason__languageID', 'C', 256, 'AN'],
    ],
ram+'CreditReasonCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CreditReasonCode__listName', 'C', 256, 'AN'],
    [ram+'CreditReasonCode__name', 'C', 256, 'AN'],
    [ram+'CreditReasonCode__languageID', 'C', 256, 'AN'],
    [ram+'CreditReasonCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'CreditReasonCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'CreditReasonCode__listID', 'C', 256, 'AN'],
    [ram+'CreditReasonCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'CreditReasonCode__listURI', 'C', 256, 'AN'],
    [ram+'CreditReasonCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'CreditorReferenceID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CreditorReferenceID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'CreditorReferenceID__schemeID', 'C', 256, 'AN'],
    [ram+'CreditorReferenceID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'CreditorReferenceID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'CreditorReferenceID__schemeName', 'C', 256, 'AN'],
    [ram+'CreditorReferenceID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'CreditorReferenceID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'CreditorReferenceIssuerID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CreditorReferenceIssuerID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'CreditorReferenceIssuerID__schemeID', 'C', 256, 'AN'],
    [ram+'CreditorReferenceIssuerID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'CreditorReferenceIssuerID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'CreditorReferenceIssuerID__schemeName', 'C', 256, 'AN'],
    [ram+'CreditorReferenceIssuerID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'CreditorReferenceIssuerID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'CreditorReferenceType':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CreditorReferenceType__languageLocaleID', 'C', 256, 'AN'],
    [ram+'CreditorReferenceType__languageID', 'C', 256, 'AN'],
    ],
ram+'CreditorReferenceTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CreditorReferenceTypeCode__listName', 'C', 256, 'AN'],
    [ram+'CreditorReferenceTypeCode__name', 'C', 256, 'AN'],
    [ram+'CreditorReferenceTypeCode__languageID', 'C', 256, 'AN'],
    [ram+'CreditorReferenceTypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'CreditorReferenceTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'CreditorReferenceTypeCode__listID', 'C', 256, 'AN'],
    [ram+'CreditorReferenceTypeCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'CreditorReferenceTypeCode__listURI', 'C', 256, 'AN'],
    [ram+'CreditorReferenceTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'CurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'CurrencyCode__listName', 'C', 256, 'AN'],
    [ram+'CurrencyCode__name', 'C', 256, 'AN'],
    [ram+'CurrencyCode__languageID', 'C', 256, 'AN'],
    [ram+'CurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'CurrencyCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'CurrencyCode__listID', 'C', 256, 'AN'],
    [ram+'CurrencyCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'CurrencyCode__listURI', 'C', 256, 'AN'],
    [ram+'CurrencyCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'CustomerFacingTotalUnitQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'CustomerFacingTotalUnitQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'CustomerFacingTotalUnitQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'CustomerFacingTotalUnitQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'CustomerFacingTotalUnitQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'CustomsDutyIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'CustomsExportAgentTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'CustomsImportAgentTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'DeclaredValueForCustomsAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'DeclaredValueForCustomsAmount__currencyID', 'C', 256, 'AN'],
    [ram+'DeclaredValueForCustomsAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'DeclaredValueForStatisticsAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'DeclaredValueForStatisticsAmount__currencyID', 'C', 256, 'AN'],
    [ram+'DeclaredValueForStatisticsAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'DefaultCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'DefaultCurrencyCode__listID', 'C', 256, 'AN'],
    [ram+'DefaultCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'DefaultCurrencyCode__listVersionID', 'C', 256, 'AN'],
    [ram+'DefaultCurrencyCode__listURI', 'C', 256, 'AN'],
    ],
ram+'DefaultLanguageCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'DefaultLanguageCode__listName', 'C', 256, 'AN'],
    [ram+'DefaultLanguageCode__name', 'C', 256, 'AN'],
    [ram+'DefaultLanguageCode__languageID', 'C', 256, 'AN'],
    [ram+'DefaultLanguageCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'DefaultLanguageCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'DefaultLanguageCode__listID', 'C', 256, 'AN'],
    [ram+'DefaultLanguageCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'DefaultLanguageCode__listURI', 'C', 256, 'AN'],
    [ram+'DefaultLanguageCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'DefinedTradeContact':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'DeliveryNoteReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'DeliveryTradeLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'DeliveryTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'DeliveryTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'DeliveryTypeCode__listID', 'C', 256, 'AN'],
    [ram+'DeliveryTypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'DeliveryTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'DemandForecastReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'DepartmentName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'DepartmentName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'DepartmentName__languageID', 'C', 256, 'AN'],
    ],
ram+'DepositValueSpecifiedAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'DepositValueSpecifiedAmount__currencyID', 'C', 256, 'AN'],
    [ram+'DepositValueSpecifiedAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'DepositValueValiditySpecifiedPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'Description':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 9999, 'AN'],
    [ram+'Description__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Description__languageID', 'C', 256, 'AN'],
    ],
ram+'DescriptionBinaryObject':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'DescriptionBinaryObject__format', 'C', 256, 'AN'],
    [ram+'DescriptionBinaryObject__encodingCode', 'C', 256, 'AN'],
    [ram+'DescriptionBinaryObject__uri', 'C', 256, 'AN'],
    [ram+'DescriptionBinaryObject__filename', 'C', 256, 'AN'],
    [ram+'DescriptionBinaryObject__characterSetCode', 'C', 256, 'AN'],
    [ram+'DescriptionBinaryObject__mimeCode', 'C', 256, 'AN'],
    ],
ram+'DescriptionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'DescriptionCode__listName', 'C', 256, 'AN'],
    [ram+'DescriptionCode__name', 'C', 256, 'AN'],
    [ram+'DescriptionCode__languageID', 'C', 256, 'AN'],
    [ram+'DescriptionCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'DescriptionCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'DescriptionCode__listID', 'C', 256, 'AN'],
    [ram+'DescriptionCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'DescriptionCode__listURI', 'C', 256, 'AN'],
    [ram+'DescriptionCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'DesignatedProductClassification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'Designation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Designation__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Designation__languageID', 'C', 256, 'AN'],
    ],
ram+'DespatchAdviceReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'DespatchedQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'DespatchedQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'DespatchedQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'DespatchedQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'DespatchedQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'DiameterMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'DiameterMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'DiameterMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'DirectDebitMandateID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'DirectDebitMandateID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'DirectDebitMandateID__schemeID', 'C', 256, 'AN'],
    [ram+'DirectDebitMandateID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'DirectDebitMandateID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'DirectDebitMandateID__schemeName', 'C', 256, 'AN'],
    [ram+'DirectDebitMandateID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'DirectDebitMandateID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'DirectTelephoneUniversalCommunication':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'DisbursementAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'DisbursementAmount__currencyID', 'C', 256, 'AN'],
    [ram+'DisbursementAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'DiscountIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'DisposalMethodCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'DisposalMethodCode__listName', 'C', 256, 'AN'],
    [ram+'DisposalMethodCode__name', 'C', 256, 'AN'],
    [ram+'DisposalMethodCode__languageID', 'C', 256, 'AN'],
    [ram+'DisposalMethodCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'DisposalMethodCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'DisposalMethodCode__listID', 'C', 256, 'AN'],
    [ram+'DisposalMethodCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'DisposalMethodCode__listURI', 'C', 256, 'AN'],
    [ram+'DisposalMethodCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'DrainedNetWeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'DrainedNetWeightMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'DrainedNetWeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'DueDateDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'DueDateTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'DueDateTypeCode__listID', 'C', 256, 'AN'],
    [ram+'DueDateTypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'DueDateTypeCode__name', 'C', 256, 'AN'],
    [ram+'DueDateTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'DuePayableAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'DuePayableAmount__currencyID', 'C', 256, 'AN'],
    [ram+'DuePayableAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'DurationMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'DurationMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'DurationMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'EarliestOccurrenceDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'EffectiveSpecifiedPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ElementVersionID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ElementVersionID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'ElementVersionID__schemeID', 'C', 256, 'AN'],
    [ram+'ElementVersionID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'ElementVersionID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'ElementVersionID__schemeName', 'C', 256, 'AN'],
    [ram+'ElementVersionID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'ElementVersionID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'EmailURIUniversalCommunication':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'EncodingCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'EncodingCode__listName', 'C', 256, 'AN'],
    [ram+'EncodingCode__name', 'C', 256, 'AN'],
    [ram+'EncodingCode__languageID', 'C', 256, 'AN'],
    [ram+'EncodingCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'EncodingCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'EncodingCode__listID', 'C', 256, 'AN'],
    [ram+'EncodingCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'EncodingCode__listURI', 'C', 256, 'AN'],
    [ram+'EncodingCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'EndDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'EndItemName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'EndItemName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'EndItemName__languageID', 'C', 256, 'AN'],
    ],
ram+'EndItemTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'EndItemTypeCode__listName', 'C', 256, 'AN'],
    [ram+'EndItemTypeCode__name', 'C', 256, 'AN'],
    [ram+'EndItemTypeCode__languageID', 'C', 256, 'AN'],
    [ram+'EndItemTypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'EndItemTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'EndItemTypeCode__listID', 'C', 256, 'AN'],
    [ram+'EndItemTypeCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'EndItemTypeCode__listURI', 'C', 256, 'AN'],
    [ram+'EndItemTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'EndPointURIUniversalCommunication':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ExemptionReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ExemptionReason__languageLocaleID', 'C', 256, 'AN'],
    [ram+'ExemptionReason__languageID', 'C', 256, 'AN'],
    ],
ram+'ExemptionReasonCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ExemptionReasonCode__listName', 'C', 256, 'AN'],
    [ram+'ExemptionReasonCode__name', 'C', 256, 'AN'],
    [ram+'ExemptionReasonCode__languageID', 'C', 256, 'AN'],
    [ram+'ExemptionReasonCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ExemptionReasonCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'ExemptionReasonCode__listID', 'C', 256, 'AN'],
    [ram+'ExemptionReasonCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'ExemptionReasonCode__listURI', 'C', 256, 'AN'],
    [ram+'ExemptionReasonCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ExpiryDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ExpiryDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'FactoringAgreementReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'FactoringListReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'FamilyName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'FamilyName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'FamilyName__languageID', 'C', 256, 'AN'],
    ],
ram+'FaxUniversalCommunication':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'FedwireRoutingNumberID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'FedwireRoutingNumberID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'FedwireRoutingNumberID__schemeID', 'C', 256, 'AN'],
    [ram+'FedwireRoutingNumberID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'FedwireRoutingNumberID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'FedwireRoutingNumberID__schemeName', 'C', 256, 'AN'],
    [ram+'FedwireRoutingNumberID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'FedwireRoutingNumberID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'FileName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'FileName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'FileName__languageID', 'C', 256, 'AN'],
    ],
ram+'FormattedCancellationAnnouncedLaunchDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'FormattedIssueDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'FormattedLatestProductDataChangeDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'FormattedReceivedDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'FreightForwarderTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'FromEventCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'FromEventCode__listID', 'C', 256, 'AN'],
    [ram+'FromEventCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'FromEventCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'GermanBankleitzahlID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'GermanBankleitzahlID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'GermanBankleitzahlID__schemeID', 'C', 256, 'AN'],
    [ram+'GermanBankleitzahlID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'GermanBankleitzahlID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'GermanBankleitzahlID__schemeName', 'C', 256, 'AN'],
    [ram+'GermanBankleitzahlID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'GermanBankleitzahlID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'GivenName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'GivenName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'GivenName__languageID', 'C', 256, 'AN'],
    ],
ram+'GlobalID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'GlobalID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'GlobalID__schemeID', 'C', 256, 'AN'],
    [ram+'GlobalID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'GlobalID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'GlobalID__schemeName', 'C', 256, 'AN'],
    [ram+'GlobalID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'GlobalID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'GlobalSerialID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'GlobalSerialID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'GlobalSerialID__schemeID', 'C', 256, 'AN'],
    [ram+'GlobalSerialID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'GlobalSerialID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'GlobalSerialID__schemeName', 'C', 256, 'AN'],
    [ram+'GlobalSerialID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'GlobalSerialID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'GrandTotalAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'GrandTotalAmount__currencyID', 'C', 256, 'AN'],
    [ram+'GrandTotalAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'GrossLineTotalAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'GrossLineTotalAmount__currencyID', 'C', 256, 'AN'],
    [ram+'GrossLineTotalAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'GrossPriceProductTradePrice':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'GrossVolumeMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'GrossVolumeMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'GrossVolumeMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'GrossWeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'GrossWeightMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'GrossWeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'GroupingCentreTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'GuaranteeMethodCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'GuaranteeMethodCode__listID', 'C', 256, 'AN'],
    [ram+'GuaranteeMethodCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'GuaranteeMethodCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'GuidelineSpecifiedDocumentContextParameter':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'HeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'HeightMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'HeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'HellenicBankID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'HellenicBankID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'HellenicBankID__schemeID', 'C', 256, 'AN'],
    [ram+'HellenicBankID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'HellenicBankID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'HellenicBankID__schemeName', 'C', 256, 'AN'],
    [ram+'HellenicBankID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'HellenicBankID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'HongKongBankID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'HongKongBankID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'HongKongBankID__schemeID', 'C', 256, 'AN'],
    [ram+'HongKongBankID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'HongKongBankID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'HongKongBankID__schemeName', 'C', 256, 'AN'],
    [ram+'HongKongBankID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'HongKongBankID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'IBANID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'IBANID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'IBANID__schemeID', 'C', 256, 'AN'],
    [ram+'IBANID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'IBANID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'IBANID__schemeName', 'C', 256, 'AN'],
    [ram+'IBANID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'IBANID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'ID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'ID__schemeID', 'C', 256, 'AN'],
    [ram+'ID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'ID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'ID__schemeName', 'C', 256, 'AN'],
    [ram+'ID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'ID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'Identification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Identification__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Identification__languageID', 'C', 256, 'AN'],
    ],
ram+'IncludedBinaryObject':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'IncludedBinaryObject__format', 'C', 256, 'AN'],
    [ram+'IncludedBinaryObject__encodingCode', 'C', 256, 'AN'],
    [ram+'IncludedBinaryObject__uri', 'C', 256, 'AN'],
    [ram+'IncludedBinaryObject__filename', 'C', 256, 'AN'],
    [ram+'IncludedBinaryObject__characterSetCode', 'C', 256, 'AN'],
    [ram+'IncludedBinaryObject__mimeCode', 'C', 256, 'AN'],
    ],
ram+'IncludedNote':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'IncludedReferencedProduct':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'IncludedSpecifiedMarketplace':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'IncludedSubordinateTradeLineItem':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'IncludedSupplyChainConsignmentItem':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'IncludedSupplyChainPackaging':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'IncludedSupplyChainTradeLineItem':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'IncludedTradeTax':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'InclusiveIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'Index':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Index__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Index__languageID', 'C', 256, 'AN'],
    ],
ram+'IndexValue':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'IndexValue__format', 'C', 256, 'AN'],
    ],
ram+'IndianFinancialSystemID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'IndianFinancialSystemID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'IndianFinancialSystemID__schemeID', 'C', 256, 'AN'],
    [ram+'IndianFinancialSystemID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'IndianFinancialSystemID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'IndianFinancialSystemID__schemeName', 'C', 256, 'AN'],
    [ram+'IndianFinancialSystemID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'IndianFinancialSystemID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'IndividualTradeProductInstance':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'IndustryAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'IndustryAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'IndustryAssignedID__schemeID', 'C', 256, 'AN'],
    [ram+'IndustryAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'IndustryAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'IndustryAssignedID__schemeName', 'C', 256, 'AN'],
    [ram+'IndustryAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'IndustryAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'Information':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Information__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Information__languageID', 'C', 256, 'AN'],
    ],
ram+'InformationAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'InformationAmount__currencyID', 'C', 256, 'AN'],
    [ram+'InformationAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'InformationNote':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'InspectionReferenceReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'InstantMessagingUniversalCommunication':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'InstructionTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'InstructionTypeCode__listName', 'C', 256, 'AN'],
    [ram+'InstructionTypeCode__name', 'C', 256, 'AN'],
    [ram+'InstructionTypeCode__languageID', 'C', 256, 'AN'],
    [ram+'InstructionTypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'InstructionTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'InstructionTypeCode__listID', 'C', 256, 'AN'],
    [ram+'InstructionTypeCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'InstructionTypeCode__listURI', 'C', 256, 'AN'],
    [ram+'InstructionTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'InsurancePremiumAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'InsurancePremiumAmount__currencyID', 'C', 256, 'AN'],
    [ram+'InsurancePremiumAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'InterestRatePercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'InterestRatePercent__format', 'C', 256, 'AN'],
    ],
ram+'InvoiceAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'InvoiceAmount__currencyID', 'C', 256, 'AN'],
    [ram+'InvoiceAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'InvoiceApplicableTradeCurrencyExchange':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'InvoiceCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'InvoiceCurrencyCode__listID', 'C', 256, 'AN'],
    [ram+'InvoiceCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'InvoiceCurrencyCode__listVersionID', 'C', 256, 'AN'],
    [ram+'InvoiceCurrencyCode__listURI', 'C', 256, 'AN'],
    ],
ram+'InvoiceDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'InvoiceIssuerReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'InvoiceIssuerReference__languageLocaleID', 'C', 256, 'AN'],
    [ram+'InvoiceIssuerReference__languageID', 'C', 256, 'AN'],
    ],
ram+'InvoiceReferenceReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'InvoiceReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'InvoiceeTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'InvoicerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'IrishNSCID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'IrishNSCID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'IrishNSCID__schemeID', 'C', 256, 'AN'],
    [ram+'IrishNSCID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'IrishNSCID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'IrishNSCID__schemeName', 'C', 256, 'AN'],
    [ram+'IrishNSCID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'IrishNSCID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'IssueDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'IssuerAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'IssuerAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'IssuerAssignedID__schemeID', 'C', 256, 'AN'],
    [ram+'IssuerAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'IssuerAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'IssuerAssignedID__schemeName', 'C', 256, 'AN'],
    [ram+'IssuerAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'IssuerAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'IssuerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'IssuingCompanyName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'IssuingCompanyName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'IssuingCompanyName__languageID', 'C', 256, 'AN'],
    ],
ram+'ItalianDomesticID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ItalianDomesticID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'ItalianDomesticID__schemeID', 'C', 256, 'AN'],
    [ram+'ItalianDomesticID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'ItalianDomesticID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'ItalianDomesticID__schemeName', 'C', 256, 'AN'],
    [ram+'ItalianDomesticID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'ItalianDomesticID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'ItemBasicWorkItem':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ItemBuyerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ItemGroupedWorkItem':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ItemSellerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'JapanFinancialInstitutionCommonID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'JapanFinancialInstitutionCommonID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'JapanFinancialInstitutionCommonID__schemeID', 'C', 256, 'AN'],
    [ram+'JapanFinancialInstitutionCommonID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'JapanFinancialInstitutionCommonID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'JapanFinancialInstitutionCommonID__schemeName', 'C', 256, 'AN'],
    [ram+'JapanFinancialInstitutionCommonID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'JapanFinancialInstitutionCommonID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'JobTitle':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'JobTitle__languageLocaleID', 'C', 256, 'AN'],
    [ram+'JobTitle__languageID', 'C', 256, 'AN'],
    ],
ram+'Jurisdiction':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Jurisdiction__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Jurisdiction__languageID', 'C', 256, 'AN'],
    ],
ram+'KanbanID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'KanbanID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'KanbanID__schemeID', 'C', 256, 'AN'],
    [ram+'KanbanID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'KanbanID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'KanbanID__schemeName', 'C', 256, 'AN'],
    [ram+'KanbanID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'KanbanID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'LanguageID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'LanguageID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'LanguageID__schemeID', 'C', 256, 'AN'],
    [ram+'LanguageID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'LanguageID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'LanguageID__schemeName', 'C', 256, 'AN'],
    [ram+'LanguageID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'LanguageID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'LatestOccurrenceDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'LatitudeMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'LatitudeMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'LatitudeMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'LayerTotalUnitQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'LayerTotalUnitQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'LayerTotalUnitQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'LayerTotalUnitQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'LayerTotalUnitQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'LegalClassificationCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'LegalClassificationCode__listName', 'C', 256, 'AN'],
    [ram+'LegalClassificationCode__name', 'C', 256, 'AN'],
    [ram+'LegalClassificationCode__languageID', 'C', 256, 'AN'],
    [ram+'LegalClassificationCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'LegalClassificationCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'LegalClassificationCode__listID', 'C', 256, 'AN'],
    [ram+'LegalClassificationCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'LegalClassificationCode__listURI', 'C', 256, 'AN'],
    [ram+'LegalClassificationCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'LegalRightsOwnerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'LengthMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'LengthMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'LengthMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'LetterOfCreditReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'LineFive':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'LineFive__languageLocaleID', 'C', 256, 'AN'],
    [ram+'LineFive__languageID', 'C', 256, 'AN'],
    ],
ram+'LineFour':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'LineFour__languageLocaleID', 'C', 256, 'AN'],
    [ram+'LineFour__languageID', 'C', 256, 'AN'],
    ],
ram+'LineID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'LineID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'LineID__schemeID', 'C', 256, 'AN'],
    [ram+'LineID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'LineID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'LineID__schemeName', 'C', 256, 'AN'],
    [ram+'LineID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'LineID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'LineOne':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'LineOne__languageLocaleID', 'C', 256, 'AN'],
    [ram+'LineOne__languageID', 'C', 256, 'AN'],
    ],
ram+'LineStatusCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'LineStatusCode__listID', 'C', 256, 'AN'],
    [ram+'LineStatusCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'LineStatusCode__listVersionID', 'C', 256, 'AN'],
    [ram+'LineStatusCode__listURI', 'C', 256, 'AN'],
    ],
ram+'LineStatusReasonCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'LineStatusReasonCode__listName', 'C', 256, 'AN'],
    [ram+'LineStatusReasonCode__name', 'C', 256, 'AN'],
    [ram+'LineStatusReasonCode__languageID', 'C', 256, 'AN'],
    [ram+'LineStatusReasonCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'LineStatusReasonCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'LineStatusReasonCode__listID', 'C', 256, 'AN'],
    [ram+'LineStatusReasonCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'LineStatusReasonCode__listURI', 'C', 256, 'AN'],
    [ram+'LineStatusReasonCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'LineThree':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'LineThree__languageLocaleID', 'C', 256, 'AN'],
    [ram+'LineThree__languageID', 'C', 256, 'AN'],
    ],
ram+'LineTotalAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'LineTotalAmount__currencyID', 'C', 256, 'AN'],
    [ram+'LineTotalAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'LineTotalBasisAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'LineTotalBasisAmount__currencyID', 'C', 256, 'AN'],
    [ram+'LineTotalBasisAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'LineTwo':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'LineTwo__languageLocaleID', 'C', 256, 'AN'],
    [ram+'LineTwo__languageID', 'C', 256, 'AN'],
    ],
ram+'LinearSpatialDimension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'LoadingLengthMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'LoadingLengthMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'LoadingLengthMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'LocationFinancialInstitutionAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'LogoAssociatedSpecifiedBinaryFile':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'LongitudeMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'LongitudeMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'LongitudeMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'MIMECode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'MIMECode__listName', 'C', 256, 'AN'],
    [ram+'MIMECode__name', 'C', 256, 'AN'],
    [ram+'MIMECode__languageID', 'C', 256, 'AN'],
    [ram+'MIMECode__listAgencyID', 'C', 256, 'AN'],
    [ram+'MIMECode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'MIMECode__listID', 'C', 256, 'AN'],
    [ram+'MIMECode__listAgencyName', 'C', 256, 'AN'],
    [ram+'MIMECode__listURI', 'C', 256, 'AN'],
    [ram+'MIMECode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'MSDSReferenceReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ManufacturerAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ManufacturerAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'ManufacturerAssignedID__schemeID', 'C', 256, 'AN'],
    [ram+'ManufacturerAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'ManufacturerAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'ManufacturerAssignedID__schemeName', 'C', 256, 'AN'],
    [ram+'ManufacturerAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'ManufacturerAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'ManufacturerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'MarketID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'MarketID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'MarketID__schemeID', 'C', 256, 'AN'],
    [ram+'MarketID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'MarketID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'MarketID__schemeName', 'C', 256, 'AN'],
    [ram+'MarketID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'MarketID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'MaterialID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'MaterialID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'MaterialID__schemeID', 'C', 256, 'AN'],
    [ram+'MaterialID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'MaterialID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'MaterialID__schemeName', 'C', 256, 'AN'],
    [ram+'MaterialID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'MaterialID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'MaximumLinearSpatialDimension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'MaximumQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'MaximumQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'MaximumQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'MaximumQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'MaximumQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'MaximumStackabilityQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'MaximumStackabilityQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'MaximumStackabilityQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'MaximumStackabilityQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'MaximumStackabilityQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'MaximumStackabilityWeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'MaximumStackabilityWeightMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'MaximumStackabilityWeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'MeasurementMethodCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'MeasurementMethodCode__listName', 'C', 256, 'AN'],
    [ram+'MeasurementMethodCode__name', 'C', 256, 'AN'],
    [ram+'MeasurementMethodCode__languageID', 'C', 256, 'AN'],
    [ram+'MeasurementMethodCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'MeasurementMethodCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'MeasurementMethodCode__listID', 'C', 256, 'AN'],
    [ram+'MeasurementMethodCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'MeasurementMethodCode__listURI', 'C', 256, 'AN'],
    [ram+'MeasurementMethodCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'MeasurementMethodID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'MeasurementMethodID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'MeasurementMethodID__schemeID', 'C', 256, 'AN'],
    [ram+'MeasurementMethodID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'MeasurementMethodID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'MeasurementMethodID__schemeName', 'C', 256, 'AN'],
    [ram+'MeasurementMethodID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'MeasurementMethodID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'MessageStandardSpecifiedDocumentContextParameter':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'MicrochipIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'MiddleName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'MiddleName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'MiddleName__languageID', 'C', 256, 'AN'],
    ],
ram+'MinimumLinearSpatialDimension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'MinimumQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'MinimumQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'MinimumQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'MinimumQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'MinimumQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'MobileTelephoneUniversalCommunication':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'Mode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Mode__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Mode__languageID', 'C', 256, 'AN'],
    ],
ram+'ModeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ModeCode__listID', 'C', 256, 'AN'],
    [ram+'ModeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ModeCode__name', 'C', 256, 'AN'],
    [ram+'ModeCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'Name':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Name__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Name__languageID', 'C', 256, 'AN'],
    ],
ram+'NatureIdentificationTransportCargo':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'NetIncludingTaxesLineTotalAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'NetIncludingTaxesLineTotalAmount__currencyID', 'C', 256, 'AN'],
    [ram+'NetIncludingTaxesLineTotalAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'NetLineTotalAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'NetLineTotalAmount__currencyID', 'C', 256, 'AN'],
    [ram+'NetLineTotalAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'NetPriceIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'NetPriceProductTradePrice':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'NetWeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'NetWeightMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'NetWeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'NewZealandNCCID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'NewZealandNCCID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'NewZealandNCCID__schemeID', 'C', 256, 'AN'],
    [ram+'NewZealandNCCID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'NewZealandNCCID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'NewZealandNCCID__schemeName', 'C', 256, 'AN'],
    [ram+'NewZealandNCCID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'NewZealandNCCID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'NextInvoiceDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'OccurrenceDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'OccurrenceLogisticsLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'OccurrenceSpecifiedPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'OpenIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'OperationalCategoryCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'OperationalCategoryCode__listID', 'C', 256, 'AN'],
    [ram+'OperationalCategoryCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'OperationalCategoryCode__name', 'C', 256, 'AN'],
    [ram+'OperationalCategoryCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'OrderResponseReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'OrderUnitConversionFactorNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'OrderUnitConversionFactorNumeric__format', 'C', 256, 'AN'],
    ],
ram+'OrderingAvailablePeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'OriginTradeCountry':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'OwnerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PackageQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'PackageQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'PackageQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'PackageQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'PackageQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'PackagingSupplyChainEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PackingListReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PaidAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'PaidAmount__currencyID', 'C', 256, 'AN'],
    [ram+'PaidAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'ParentLineID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ParentLineID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'ParentLineID__schemeID', 'C', 256, 'AN'],
    [ram+'ParentLineID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'ParentLineID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'ParentLineID__schemeName', 'C', 256, 'AN'],
    [ram+'ParentLineID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'ParentLineID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'PartID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PartID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'PartID__schemeID', 'C', 256, 'AN'],
    [ram+'PartID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'PartID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'PartID__schemeName', 'C', 256, 'AN'],
    [ram+'PartID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'PartID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'PartialPaymentAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'PartialPaymentAmount__currencyID', 'C', 256, 'AN'],
    [ram+'PartialPaymentAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'PartialPaymentPercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'PartialPaymentPercent__format', 'C', 256, 'AN'],
    ],
ram+'PayableSpecifiedTradeAccountingAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PayeePartyCreditorFinancialAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PayeeSpecifiedCreditorFinancialInstitution':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PayeeTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PayerPartyDebtorFinancialAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PayerSpecifiedDebtorFinancialInstitution':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PayerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PayingPartyRoleCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PayingPartyRoleCode__listID', 'C', 256, 'AN'],
    [ram+'PayingPartyRoleCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'PayingPartyRoleCode__name', 'C', 256, 'AN'],
    [ram+'PayingPartyRoleCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'PaymentApplicableTradeCurrencyExchange':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PaymentArrangementCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PaymentArrangementCode__listName', 'C', 256, 'AN'],
    [ram+'PaymentArrangementCode__name', 'C', 256, 'AN'],
    [ram+'PaymentArrangementCode__languageID', 'C', 256, 'AN'],
    [ram+'PaymentArrangementCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'PaymentArrangementCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'PaymentArrangementCode__listID', 'C', 256, 'AN'],
    [ram+'PaymentArrangementCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'PaymentArrangementCode__listURI', 'C', 256, 'AN'],
    [ram+'PaymentArrangementCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'PaymentChannelCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PaymentChannelCode__listID', 'C', 256, 'AN'],
    [ram+'PaymentChannelCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'PaymentChannelCode__name', 'C', 256, 'AN'],
    [ram+'PaymentChannelCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'PaymentCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PaymentCurrencyCode__listID', 'C', 256, 'AN'],
    [ram+'PaymentCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'PaymentCurrencyCode__listVersionID', 'C', 256, 'AN'],
    [ram+'PaymentCurrencyCode__listURI', 'C', 256, 'AN'],
    ],
ram+'PaymentMeansID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PaymentMeansID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'PaymentMeansID__schemeID', 'C', 256, 'AN'],
    [ram+'PaymentMeansID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'PaymentMeansID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'PaymentMeansID__schemeName', 'C', 256, 'AN'],
    [ram+'PaymentMeansID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'PaymentMeansID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'PaymentMethodCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PaymentMethodCode__listName', 'C', 256, 'AN'],
    [ram+'PaymentMethodCode__name', 'C', 256, 'AN'],
    [ram+'PaymentMethodCode__languageID', 'C', 256, 'AN'],
    [ram+'PaymentMethodCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'PaymentMethodCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'PaymentMethodCode__listID', 'C', 256, 'AN'],
    [ram+'PaymentMethodCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'PaymentMethodCode__listURI', 'C', 256, 'AN'],
    [ram+'PaymentMethodCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'PaymentPlaceLogisticsLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PaymentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PaymentReference__languageLocaleID', 'C', 256, 'AN'],
    [ram+'PaymentReference__languageID', 'C', 256, 'AN'],
    ],
ram+'PerPackageUnitQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'PerPackageUnitQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'PerPackageUnitQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'PerPackageUnitQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'PerPackageUnitQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'PersonID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PersonID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'PersonID__schemeID', 'C', 256, 'AN'],
    [ram+'PersonID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'PersonID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'PersonID__schemeName', 'C', 256, 'AN'],
    [ram+'PersonID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'PersonID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'PersonName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PersonName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'PersonName__languageID', 'C', 256, 'AN'],
    ],
ram+'PhysicalGeographicalCoordinate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PlaceApplicableTradeLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PolishNationalClearingID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PolishNationalClearingID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'PolishNationalClearingID__schemeID', 'C', 256, 'AN'],
    [ram+'PolishNationalClearingID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'PolishNationalClearingID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'PolishNationalClearingID__schemeName', 'C', 256, 'AN'],
    [ram+'PolishNationalClearingID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'PolishNationalClearingID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'PortugueseNCCID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PortugueseNCCID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'PortugueseNCCID__schemeID', 'C', 256, 'AN'],
    [ram+'PortugueseNCCID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'PortugueseNCCID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'PortugueseNCCID__schemeName', 'C', 256, 'AN'],
    [ram+'PortugueseNCCID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'PortugueseNCCID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'PostOfficeBox':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PostOfficeBox__languageLocaleID', 'C', 256, 'AN'],
    [ram+'PostOfficeBox__languageID', 'C', 256, 'AN'],
    ],
ram+'PostalTradeAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PostcodeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PostcodeCode__listName', 'C', 256, 'AN'],
    [ram+'PostcodeCode__name', 'C', 256, 'AN'],
    [ram+'PostcodeCode__languageID', 'C', 256, 'AN'],
    [ram+'PostcodeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'PostcodeCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'PostcodeCode__listID', 'C', 256, 'AN'],
    [ram+'PostcodeCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'PostcodeCode__listURI', 'C', 256, 'AN'],
    [ram+'PostcodeCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'PrepaidIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PresentationSpecifiedBinaryFile':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PreviousDeliverySupplyChainEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PreviousRevisionID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PreviousRevisionID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'PreviousRevisionID__schemeID', 'C', 256, 'AN'],
    [ram+'PreviousRevisionID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'PreviousRevisionID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'PreviousRevisionID__schemeName', 'C', 256, 'AN'],
    [ram+'PreviousRevisionID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'PreviousRevisionID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'PriceListID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PriceListID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'PriceListID__schemeID', 'C', 256, 'AN'],
    [ram+'PriceListID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'PriceListID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'PriceListID__schemeName', 'C', 256, 'AN'],
    [ram+'PriceListID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'PriceListID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'PriceListItemID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PriceListItemID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'PriceListItemID__schemeID', 'C', 256, 'AN'],
    [ram+'PriceListItemID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'PriceListItemID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'PriceListItemID__schemeName', 'C', 256, 'AN'],
    [ram+'PriceListItemID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'PriceListItemID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'PriceListReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PrimaryClassificationCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PrimaryClassificationCode__listName', 'C', 256, 'AN'],
    [ram+'PrimaryClassificationCode__name', 'C', 256, 'AN'],
    [ram+'PrimaryClassificationCode__languageID', 'C', 256, 'AN'],
    [ram+'PrimaryClassificationCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'PrimaryClassificationCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'PrimaryClassificationCode__listID', 'C', 256, 'AN'],
    [ram+'PrimaryClassificationCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'PrimaryClassificationCode__listURI', 'C', 256, 'AN'],
    [ram+'PrimaryClassificationCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ProFormaInvoiceReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ProductEndUserTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ProductGroupID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ProductGroupID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'ProductGroupID__schemeID', 'C', 256, 'AN'],
    [ram+'ProductGroupID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'ProductGroupID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'ProductGroupID__schemeName', 'C', 256, 'AN'],
    [ram+'ProductGroupID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'ProductGroupID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'ProductUnitQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ProductUnitQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'ProductUnitQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'ProductUnitQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'ProductUnitQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'ProductValueExcludingTobaccoTaxInformationAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ProductValueExcludingTobaccoTaxInformationAmount__currencyID', 'C', 256, 'AN'],
    [ram+'ProductValueExcludingTobaccoTaxInformationAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'ProductWeightLossInformationAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ProductWeightLossInformationAmount__currencyID', 'C', 256, 'AN'],
    [ram+'ProductWeightLossInformationAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'ProductionSupplyChainEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PromotionalDealReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ProportionalConstituentPercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ProportionalConstituentPercent__format', 'C', 256, 'AN'],
    ],
ram+'ProprietaryID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ProprietaryID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'ProprietaryID__schemeID', 'C', 256, 'AN'],
    [ram+'ProprietaryID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'ProprietaryID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'ProprietaryID__schemeName', 'C', 256, 'AN'],
    [ram+'ProprietaryID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'ProprietaryID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'PurchaseConditionsReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'PurchaseSpecifiedTradeAccountingAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'Purpose':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Purpose__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Purpose__languageID', 'C', 256, 'AN'],
    ],
ram+'PurposeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'PurposeCode__listID', 'C', 256, 'AN'],
    [ram+'PurposeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'PurposeCode__listVersionID', 'C', 256, 'AN'],
    [ram+'PurposeCode__listURI', 'C', 256, 'AN'],
    ],
ram+'QueryID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'QueryID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'QueryID__schemeID', 'C', 256, 'AN'],
    [ram+'QueryID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'QueryID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'QueryID__schemeName', 'C', 256, 'AN'],
    [ram+'QueryID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'QueryID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'QuotationReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'RateApplicablePercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'RateApplicablePercent__format', 'C', 256, 'AN'],
    ],
ram+'ReaderSpecifiedBinaryFile':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'Reason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Reason__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Reason__languageID', 'C', 256, 'AN'],
    ],
ram+'ReasonCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ReasonCode__listID', 'C', 256, 'AN'],
    [ram+'ReasonCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ReasonCode__listVersionID', 'C', 256, 'AN'],
    [ram+'ReasonCode__listURI', 'C', 256, 'AN'],
    ],
ram+'ReceivableSpecifiedTradeAccountingAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ReceivedQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ReceivedQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'ReceivedQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'ReceivedQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'ReceivedQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'ReceivingAdviceReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'RecyclingDescriptionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'RecyclingDescriptionCode__listName', 'C', 256, 'AN'],
    [ram+'RecyclingDescriptionCode__name', 'C', 256, 'AN'],
    [ram+'RecyclingDescriptionCode__languageID', 'C', 256, 'AN'],
    [ram+'RecyclingDescriptionCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'RecyclingDescriptionCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'RecyclingDescriptionCode__listID', 'C', 256, 'AN'],
    [ram+'RecyclingDescriptionCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'RecyclingDescriptionCode__listURI', 'C', 256, 'AN'],
    [ram+'RecyclingDescriptionCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'RecyclingProcedure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'RecyclingProcedure__languageLocaleID', 'C', 256, 'AN'],
    [ram+'RecyclingProcedure__languageID', 'C', 256, 'AN'],
    ],
ram+'Reference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Reference__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Reference__languageID', 'C', 256, 'AN'],
    ],
ram+'ReferenceFileBinaryObject':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ReferenceFileBinaryObject__format', 'C', 256, 'AN'],
    [ram+'ReferenceFileBinaryObject__encodingCode', 'C', 256, 'AN'],
    [ram+'ReferenceFileBinaryObject__uri', 'C', 256, 'AN'],
    [ram+'ReferenceFileBinaryObject__filename', 'C', 256, 'AN'],
    [ram+'ReferenceFileBinaryObject__characterSetCode', 'C', 256, 'AN'],
    [ram+'ReferenceFileBinaryObject__mimeCode', 'C', 256, 'AN'],
    ],
ram+'ReferenceID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ReferenceID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'ReferenceID__schemeID', 'C', 256, 'AN'],
    [ram+'ReferenceID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'ReferenceID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'ReferenceID__schemeName', 'C', 256, 'AN'],
    [ram+'ReferenceID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'ReferenceID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'ReferenceTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ReferenceTypeCode__listID', 'C', 256, 'AN'],
    [ram+'ReferenceTypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ReferenceTypeCode__name', 'C', 256, 'AN'],
    [ram+'ReferenceTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ReferencedSpecifiedBinaryFile':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'RegistrationID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'RegistrationID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'RegistrationID__schemeID', 'C', 256, 'AN'],
    [ram+'RegistrationID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'RegistrationID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'RegistrationID__schemeName', 'C', 256, 'AN'],
    [ram+'RegistrationID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'RegistrationID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'RelatedAppliedAllowanceCharge':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'RelatedSupplyChainConsignment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'RelationshipTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'RelationshipTypeCode__listName', 'C', 256, 'AN'],
    [ram+'RelationshipTypeCode__name', 'C', 256, 'AN'],
    [ram+'RelationshipTypeCode__languageID', 'C', 256, 'AN'],
    [ram+'RelationshipTypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'RelationshipTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'RelationshipTypeCode__listID', 'C', 256, 'AN'],
    [ram+'RelationshipTypeCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'RelationshipTypeCode__listURI', 'C', 256, 'AN'],
    [ram+'RelationshipTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'RelevantTradeLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'RequestedActionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'RequestedActionCode__listName', 'C', 256, 'AN'],
    [ram+'RequestedActionCode__name', 'C', 256, 'AN'],
    [ram+'RequestedActionCode__languageID', 'C', 256, 'AN'],
    [ram+'RequestedActionCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'RequestedActionCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'RequestedActionCode__listID', 'C', 256, 'AN'],
    [ram+'RequestedActionCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'RequestedActionCode__listURI', 'C', 256, 'AN'],
    [ram+'RequestedActionCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'RequestedDeliverySupplyChainEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'RequestedQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'RequestedQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'RequestedQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'RequestedQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'RequestedQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'RequestingSpecificationQuery':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'RequisitionerReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'RespondingSpecificationResponse':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'Responsibility':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Responsibility__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Responsibility__languageID', 'C', 256, 'AN'],
    ],
ram+'RetailValueExcludingTaxInformationAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'RetailValueExcludingTaxInformationAmount__currencyID', 'C', 256, 'AN'],
    [ram+'RetailValueExcludingTaxInformationAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'RevisionDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'RevisionID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'RevisionID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'RevisionID__schemeID', 'C', 256, 'AN'],
    [ram+'RevisionID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'RevisionID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'RevisionID__schemeName', 'C', 256, 'AN'],
    [ram+'RevisionID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'RevisionID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'RoleCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'RoleCode__listID', 'C', 256, 'AN'],
    [ram+'RoleCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'RoleCode__name', 'C', 256, 'AN'],
    [ram+'RoleCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'RoundingAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'RoundingAmount__currencyID', 'C', 256, 'AN'],
    [ram+'RoundingAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'RussianCentralBankID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'RussianCentralBankID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'RussianCentralBankID__schemeID', 'C', 256, 'AN'],
    [ram+'RussianCentralBankID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'RussianCentralBankID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'RussianCentralBankID__schemeName', 'C', 256, 'AN'],
    [ram+'RussianCentralBankID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'RussianCentralBankID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'SICID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SICID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'SICID__schemeID', 'C', 256, 'AN'],
    [ram+'SICID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'SICID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'SICID__schemeName', 'C', 256, 'AN'],
    [ram+'SICID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'SICID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'SalesAgentTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SalesMethodCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SalesMethodCode__listName', 'C', 256, 'AN'],
    [ram+'SalesMethodCode__name', 'C', 256, 'AN'],
    [ram+'SalesMethodCode__languageID', 'C', 256, 'AN'],
    [ram+'SalesMethodCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'SalesMethodCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'SalesMethodCode__listID', 'C', 256, 'AN'],
    [ram+'SalesMethodCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'SalesMethodCode__listURI', 'C', 256, 'AN'],
    [ram+'SalesMethodCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'SalesSpecifiedTradeAccountingAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ScenarioSpecifiedDocumentContextParameter':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SeasonCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SeasonCode__listName', 'C', 256, 'AN'],
    [ram+'SeasonCode__name', 'C', 256, 'AN'],
    [ram+'SeasonCode__languageID', 'C', 256, 'AN'],
    [ram+'SeasonCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'SeasonCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'SeasonCode__listID', 'C', 256, 'AN'],
    [ram+'SeasonCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'SeasonCode__listURI', 'C', 256, 'AN'],
    [ram+'SeasonCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'SectionName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SectionName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'SectionName__languageID', 'C', 256, 'AN'],
    ],
ram+'SellByDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SellerAssignedAccountantTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SellerAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SellerAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'SellerAssignedID__schemeID', 'C', 256, 'AN'],
    [ram+'SellerAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'SellerAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'SellerAssignedID__schemeName', 'C', 256, 'AN'],
    [ram+'SellerAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'SellerAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'SellerOrderReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SellerPayableTaxSpecifiedTradeAccountingAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SellerRefundableTaxSpecifiedTradeAccountingAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SellerTaxRepresentativeTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SellerTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SequenceNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'SequenceNumeric__format', 'C', 256, 'AN'],
    ],
ram+'SerialID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SerialID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'SerialID__schemeID', 'C', 256, 'AN'],
    [ram+'SerialID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'SerialID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'SerialID__schemeName', 'C', 256, 'AN'],
    [ram+'SerialID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'SerialID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'ServiceCategoryCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ServiceCategoryCode__listName', 'C', 256, 'AN'],
    [ram+'ServiceCategoryCode__name', 'C', 256, 'AN'],
    [ram+'ServiceCategoryCode__languageID', 'C', 256, 'AN'],
    [ram+'ServiceCategoryCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ServiceCategoryCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'ServiceCategoryCode__listID', 'C', 256, 'AN'],
    [ram+'ServiceCategoryCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'ServiceCategoryCode__listURI', 'C', 256, 'AN'],
    [ram+'ServiceCategoryCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ServiceSupplyTradeCountry':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SetTriggerCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SetTriggerCode__listID', 'C', 256, 'AN'],
    [ram+'SetTriggerCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'SetTriggerCode__listVersionID', 'C', 256, 'AN'],
    [ram+'SetTriggerCode__listURI', 'C', 256, 'AN'],
    ],
ram+'SettlementPeriodMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'SettlementPeriodMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'SettlementPeriodMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'ShipFromTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ShipToTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SizeMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'SizeMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'SizeMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'SourceCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SourceCurrencyCode__listID', 'C', 256, 'AN'],
    [ram+'SourceCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'SourceCurrencyCode__listVersionID', 'C', 256, 'AN'],
    [ram+'SourceCurrencyCode__listURI', 'C', 256, 'AN'],
    ],
ram+'SourceUnitBasisNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'SourceUnitBasisNumeric__format', 'C', 256, 'AN'],
    ],
ram+'SouthAfricanNCCID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SouthAfricanNCCID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'SouthAfricanNCCID__schemeID', 'C', 256, 'AN'],
    [ram+'SouthAfricanNCCID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'SouthAfricanNCCID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'SouthAfricanNCCID__schemeName', 'C', 256, 'AN'],
    [ram+'SouthAfricanNCCID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'SouthAfricanNCCID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'SpanishDomesticInterbankingID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SpanishDomesticInterbankingID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'SpanishDomesticInterbankingID__schemeID', 'C', 256, 'AN'],
    [ram+'SpanishDomesticInterbankingID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'SpanishDomesticInterbankingID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'SpanishDomesticInterbankingID__schemeName', 'C', 256, 'AN'],
    [ram+'SpanishDomesticInterbankingID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'SpanishDomesticInterbankingID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'SpecifiedAdvancePayment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedContactPerson':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedDeliveryAdjustment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedDocumentVersion':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedFinancialAdjustment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedLegalOrganization':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedLineTradeAgreement':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedLineTradeDelivery':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedLineTradeSettlement':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedLogisticsServiceCharge':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedLogisticsTransportMovement':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedNote':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedPackagingMarking':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedProcuringProject':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedReferencedProduct':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedSubordinateLineTradeAgreement':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedSubordinateLineTradeDelivery':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedSubordinateLineTradeSettlement':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedTaxRegistration':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedTradeAccountingAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedTradeAllowanceCharge':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedTradePaymentTerms':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedTradeProduct':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedTradeSettlementFinancialCard':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedTradeSettlementHeaderMonetarySummation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedTradeSettlementLineMonetarySummation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedTradeSettlementPaymentMeans':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SpecifiedTransactionID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SpecifiedTransactionID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'SpecifiedTransactionID__schemeID', 'C', 256, 'AN'],
    [ram+'SpecifiedTransactionID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'SpecifiedTransactionID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'SpecifiedTransactionID__schemeName', 'C', 256, 'AN'],
    [ram+'SpecifiedTransactionID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'SpecifiedTransactionID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'StageCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'StageCode__listID', 'C', 256, 'AN'],
    [ram+'StageCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'StageCode__name', 'C', 256, 'AN'],
    [ram+'StageCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'StartDateFlexibilityCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'StartDateFlexibilityCode__listName', 'C', 256, 'AN'],
    [ram+'StartDateFlexibilityCode__name', 'C', 256, 'AN'],
    [ram+'StartDateFlexibilityCode__languageID', 'C', 256, 'AN'],
    [ram+'StartDateFlexibilityCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'StartDateFlexibilityCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'StartDateFlexibilityCode__listID', 'C', 256, 'AN'],
    [ram+'StartDateFlexibilityCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'StartDateFlexibilityCode__listURI', 'C', 256, 'AN'],
    [ram+'StartDateFlexibilityCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'StartDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'StatisticalClassificationCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'StatisticalClassificationCode__listID', 'C', 256, 'AN'],
    [ram+'StatisticalClassificationCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'StatisticalClassificationCode__name', 'C', 256, 'AN'],
    [ram+'StatisticalClassificationCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'StatusCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'StatusCode__listID', 'C', 256, 'AN'],
    [ram+'StatusCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'StatusCode__name', 'C', 256, 'AN'],
    [ram+'StatusCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'StreetName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'StreetName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'StreetName__languageID', 'C', 256, 'AN'],
    ],
ram+'SubBrandName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SubBrandName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'SubBrandName__languageID', 'C', 256, 'AN'],
    ],
ram+'SubClassCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SubClassCode__listName', 'C', 256, 'AN'],
    [ram+'SubClassCode__name', 'C', 256, 'AN'],
    [ram+'SubClassCode__languageID', 'C', 256, 'AN'],
    [ram+'SubClassCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'SubClassCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'SubClassCode__listID', 'C', 256, 'AN'],
    [ram+'SubClassCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'SubClassCode__listURI', 'C', 256, 'AN'],
    [ram+'SubClassCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'SubDivisionBranchFinancialInstitution':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'Subject':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Subject__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Subject__languageID', 'C', 256, 'AN'],
    ],
ram+'SubjectCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SubjectCode__listName', 'C', 256, 'AN'],
    [ram+'SubjectCode__name', 'C', 256, 'AN'],
    [ram+'SubjectCode__languageID', 'C', 256, 'AN'],
    [ram+'SubjectCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'SubjectCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'SubjectCode__listID', 'C', 256, 'AN'],
    [ram+'SubjectCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'SubjectCode__listURI', 'C', 256, 'AN'],
    [ram+'SubjectCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'SubordinateBasicWorkItem':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SubordinateTradeCountrySubDivision':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SubsetSpecifiedDocumentContextParameter':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SubsetWorkItemComplexDescription':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SubtotalCalculatedTradeTax':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SupplierAssignedSerialID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SupplierAssignedSerialID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'SupplierAssignedSerialID__schemeID', 'C', 256, 'AN'],
    [ram+'SupplierAssignedSerialID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'SupplierAssignedSerialID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'SupplierAssignedSerialID__schemeName', 'C', 256, 'AN'],
    [ram+'SupplierAssignedSerialID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'SupplierAssignedSerialID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'SupplyInstructionReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'SwissBCID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SwissBCID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'SwissBCID__schemeID', 'C', 256, 'AN'],
    [ram+'SwissBCID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'SwissBCID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'SwissBCID__schemeName', 'C', 256, 'AN'],
    [ram+'SwissBCID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'SwissBCID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'SystemID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SystemID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'SystemID__schemeID', 'C', 256, 'AN'],
    [ram+'SystemID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'SystemID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'SystemID__schemeName', 'C', 256, 'AN'],
    [ram+'SystemID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'SystemID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'SystemName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'SystemName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'SystemName__languageID', 'C', 256, 'AN'],
    ],
ram+'TargetCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'TargetCurrencyCode__listID', 'C', 256, 'AN'],
    [ram+'TargetCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'TargetCurrencyCode__listVersionID', 'C', 256, 'AN'],
    [ram+'TargetCurrencyCode__listURI', 'C', 256, 'AN'],
    ],
ram+'TargetUnitBaseNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TargetUnitBaseNumeric__format', 'C', 256, 'AN'],
    ],
ram+'TariffClassCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'TariffClassCode__listID', 'C', 256, 'AN'],
    [ram+'TariffClassCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'TariffClassCode__name', 'C', 256, 'AN'],
    [ram+'TariffClassCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'TariffQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TariffQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'TariffQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'TariffQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'TariffQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'TaxApplicableTradeCurrencyExchange':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'TaxBasisAllowanceRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TaxBasisAllowanceRate__format', 'C', 256, 'AN'],
    ],
ram+'TaxBasisTotalAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TaxBasisTotalAmount__currencyID', 'C', 256, 'AN'],
    [ram+'TaxBasisTotalAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'TaxCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'TaxCurrencyCode__listID', 'C', 256, 'AN'],
    [ram+'TaxCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'TaxCurrencyCode__listVersionID', 'C', 256, 'AN'],
    [ram+'TaxCurrencyCode__listURI', 'C', 256, 'AN'],
    ],
ram+'TaxPointDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'TaxTotalAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TaxTotalAmount__currencyID', 'C', 256, 'AN'],
    [ram+'TaxTotalAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'TelephoneUniversalCommunication':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'TelexUniversalCommunication':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'TermsAndConditionsDescription':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'TermsAndConditionsDescription__languageLocaleID', 'C', 256, 'AN'],
    [ram+'TermsAndConditionsDescription__languageID', 'C', 256, 'AN'],
    ],
ram+'TermsAndConditionsDescriptionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'TermsAndConditionsDescriptionCode__listName', 'C', 256, 'AN'],
    [ram+'TermsAndConditionsDescriptionCode__name', 'C', 256, 'AN'],
    [ram+'TermsAndConditionsDescriptionCode__languageID', 'C', 256, 'AN'],
    [ram+'TermsAndConditionsDescriptionCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'TermsAndConditionsDescriptionCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'TermsAndConditionsDescriptionCode__listID', 'C', 256, 'AN'],
    [ram+'TermsAndConditionsDescriptionCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'TermsAndConditionsDescriptionCode__listURI', 'C', 256, 'AN'],
    [ram+'TermsAndConditionsDescriptionCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'TestIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'TheoreticalWeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TheoreticalWeightMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'TheoreticalWeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'Title':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Title__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Title__languageID', 'C', 256, 'AN'],
    ],
ram+'TotalAdjustmentAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TotalAdjustmentAmount__currencyID', 'C', 256, 'AN'],
    [ram+'TotalAdjustmentAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'TotalAllowanceChargeAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TotalAllowanceChargeAmount__currencyID', 'C', 256, 'AN'],
    [ram+'TotalAllowanceChargeAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'TotalCalculatedPrice':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'TotalChargeAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TotalChargeAmount__currencyID', 'C', 256, 'AN'],
    [ram+'TotalChargeAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'TotalDepositFeeInformationAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TotalDepositFeeInformationAmount__currencyID', 'C', 256, 'AN'],
    [ram+'TotalDepositFeeInformationAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'TotalDiscountAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TotalDiscountAmount__currencyID', 'C', 256, 'AN'],
    [ram+'TotalDiscountAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'TotalPrepaidAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TotalPrepaidAmount__currencyID', 'C', 256, 'AN'],
    [ram+'TotalPrepaidAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'TotalQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TotalQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'TotalQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'TotalQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'TotalQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'TotalQuantityClassificationCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'TotalQuantityClassificationCode__listName', 'C', 256, 'AN'],
    [ram+'TotalQuantityClassificationCode__name', 'C', 256, 'AN'],
    [ram+'TotalQuantityClassificationCode__languageID', 'C', 256, 'AN'],
    [ram+'TotalQuantityClassificationCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'TotalQuantityClassificationCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'TotalQuantityClassificationCode__listID', 'C', 256, 'AN'],
    [ram+'TotalQuantityClassificationCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'TotalQuantityClassificationCode__listURI', 'C', 256, 'AN'],
    [ram+'TotalQuantityClassificationCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'TotalQuantityWorkItemQuantityAnalysis':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'TotalRetailValueInformationAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'TotalRetailValueInformationAmount__currencyID', 'C', 256, 'AN'],
    [ram+'TotalRetailValueInformationAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'TradeComparisonReferencePrice':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'TradeName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'TradeName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'TradeName__languageID', 'C', 256, 'AN'],
    ],
ram+'TradingBusinessName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'TradingBusinessName__languageLocaleID', 'C', 256, 'AN'],
    [ram+'TradingBusinessName__languageID', 'C', 256, 'AN'],
    ],
ram+'TransportContractReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'TransportPaymentMethodCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'TransportPaymentMethodCode__listName', 'C', 256, 'AN'],
    [ram+'TransportPaymentMethodCode__name', 'C', 256, 'AN'],
    [ram+'TransportPaymentMethodCode__languageID', 'C', 256, 'AN'],
    [ram+'TransportPaymentMethodCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'TransportPaymentMethodCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'TransportPaymentMethodCode__listID', 'C', 256, 'AN'],
    [ram+'TransportPaymentMethodCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'TransportPaymentMethodCode__listURI', 'C', 256, 'AN'],
    [ram+'TransportPaymentMethodCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'Type':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Type__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Type__languageID', 'C', 256, 'AN'],
    ],
ram+'TypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'TypeCode__listID', 'C', 256, 'AN'],
    [ram+'TypeCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'TypeCode__name', 'C', 256, 'AN'],
    [ram+'TypeCode__listVersionID', 'C', 256, 'AN'],
    [ram+'TypeCode__listURI', 'C', 256, 'AN'],
    ],
ram+'TypeExtensionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'TypeExtensionCode__listID', 'C', 256, 'AN'],
    [ram+'TypeExtensionCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'TypeExtensionCode__name', 'C', 256, 'AN'],
    [ram+'TypeExtensionCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'UKSortCodeID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'UKSortCodeID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'UKSortCodeID__schemeID', 'C', 256, 'AN'],
    [ram+'UKSortCodeID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'UKSortCodeID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'UKSortCodeID__schemeName', 'C', 256, 'AN'],
    [ram+'UKSortCodeID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'UKSortCodeID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'URIID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'URIID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'URIID__schemeID', 'C', 256, 'AN'],
    [ram+'URIID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'URIID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'URIID__schemeName', 'C', 256, 'AN'],
    [ram+'URIID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'URIID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'URIUniversalCommunication':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'UltimateCustomerOrderReferencedDocument':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'UltimatePayeeTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'UltimateShipToTradeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'UnitBasisAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'UnitBasisAmount__currencyID', 'C', 256, 'AN'],
    [ram+'UnitBasisAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'UnitCalculatedPrice':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'UnitQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'UnitQuantity__unitCode', 'C', 256, 'AN'],
    [ram+'UnitQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [ram+'UnitQuantity__unitCodeListID', 'C', 256, 'AN'],
    [ram+'UnitQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
ram+'UseDescription':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'UseDescription__languageLocaleID', 'C', 256, 'AN'],
    [ram+'UseDescription__languageID', 'C', 256, 'AN'],
    ],
ram+'UsedCapacityCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'UsedCapacityCode__listID', 'C', 256, 'AN'],
    [ram+'UsedCapacityCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'UsedCapacityCode__name', 'C', 256, 'AN'],
    [ram+'UsedCapacityCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'UsedLogisticsTransportMeans':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'UtilizedLogisticsTransportEquipment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'VOIPUniversalCommunication':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ValidFromDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ValiditySpecifiedPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'Value':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'Value__languageLocaleID', 'C', 256, 'AN'],
    [ram+'Value__languageID', 'C', 256, 'AN'],
    ],
ram+'ValueCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'ValueCode__listName', 'C', 256, 'AN'],
    [ram+'ValueCode__name', 'C', 256, 'AN'],
    [ram+'ValueCode__languageID', 'C', 256, 'AN'],
    [ram+'ValueCode__listAgencyID', 'C', 256, 'AN'],
    [ram+'ValueCode__listSchemeURI', 'C', 256, 'AN'],
    [ram+'ValueCode__listID', 'C', 256, 'AN'],
    [ram+'ValueCode__listAgencyName', 'C', 256, 'AN'],
    [ram+'ValueCode__listURI', 'C', 256, 'AN'],
    [ram+'ValueCode__listVersionID', 'C', 256, 'AN'],
    ],
ram+'ValueDateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ValueIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'ValueMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'ValueMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'ValueMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'ValueSpecifiedBinaryFile':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'VariableMeasureIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'VerificationNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'VerificationNumeric__format', 'C', 256, 'AN'],
    ],
ram+'VersionID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'VersionID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'VersionID__schemeID', 'C', 256, 'AN'],
    [ram+'VersionID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'VersionID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'VersionID__schemeName', 'C', 256, 'AN'],
    [ram+'VersionID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'VersionID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'VirtualIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ram+'WebsiteURIID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ram+'WebsiteURIID__schemeDataURI', 'C', 256, 'AN'],
    [ram+'WebsiteURIID__schemeID', 'C', 256, 'AN'],
    [ram+'WebsiteURIID__schemeAgencyName', 'C', 256, 'AN'],
    [ram+'WebsiteURIID__schemeAgencyID', 'C', 256, 'AN'],
    [ram+'WebsiteURIID__schemeName', 'C', 256, 'AN'],
    [ram+'WebsiteURIID__schemeVersionID', 'C', 256, 'AN'],
    [ram+'WebsiteURIID__schemeURI', 'C', 256, 'AN'],
    ],
ram+'WeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'WeightMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'WeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
ram+'WidthMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [ram+'WidthMeasure__unitCode', 'C', 256, 'AN'],
    [ram+'WidthMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
udt+'Date':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
udt+'DateString':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [udt+'DateString__format', 'C', 256, 'AN'],
    ],
udt+'DateTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
udt+'DateTimeString':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [udt+'DateTimeString__format', 'C', 256, 'AN'],
    ],
udt+'Indicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
udt+'IndicatorString':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [udt+'IndicatorString__format', 'C', 256, 'AN'],
    ],
}
