# -*- coding: utf-8 -*-
# Author: Ludovic Watteaux

from copy import deepcopy
from bots.botsconfig import ID, MIN, MAX, LEVEL

from .D16Brecords import (rsm, qdt, udt, ram)


sequences = {}


def sequence(seq):
    return deepcopy(sequences[seq][LEVEL])


sequences[qdt+'FormattedDateTimeType'] = {ID: qdt+'FormattedDateTimeType', MIN: 1, MAX: 1, LEVEL: [
    {ID: qdt+'DateTimeString', MIN: 1, MAX: 1},
]}

sequences[ram+'ContactPersonType'] = {ID: ram+'ContactPersonType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'GivenName', MIN: 0, MAX: 1},
    {ID: ram+'MiddleName', MIN: 0, MAX: 1},
    {ID: ram+'FamilyName', MIN: 0, MAX: 1},
]}

sequences[ram+'CreditorFinancialAccountType'] = {ID: ram+'CreditorFinancialAccountType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'IBANID', MIN: 0, MAX: 1},
    {ID: ram+'AccountName', MIN: 0, MAX: 1},
    {ID: ram+'ProprietaryID', MIN: 0, MAX: 1},
]}

sequences[ram+'DebtorFinancialAccountType'] = {ID: ram+'DebtorFinancialAccountType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'IBANID', MIN: 0, MAX: 1},
    {ID: ram+'AccountName', MIN: 0, MAX: 1},
    {ID: ram+'ProprietaryID', MIN: 0, MAX: 1},
]}

sequences[ram+'DisposalInstructionsType'] = {ID: ram+'DisposalInstructionsType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'MaterialID', MIN: 0, MAX: 1},
    {ID: ram+'RecyclingDescriptionCode', MIN: 0, MAX: 99999},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'RecyclingProcedure', MIN: 0, MAX: 99999},
]}

sequences[ram+'FinancialInstitutionAddressType'] = {ID: ram+'FinancialInstitutionAddressType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'PostcodeCode', MIN: 0, MAX: 1},
    {ID: ram+'BuildingNumber', MIN: 0, MAX: 1},
    {ID: ram+'LineOne', MIN: 0, MAX: 1},
    {ID: ram+'LineTwo', MIN: 0, MAX: 1},
    {ID: ram+'LineThree', MIN: 0, MAX: 1},
    {ID: ram+'LineFour', MIN: 0, MAX: 1},
    {ID: ram+'LineFive', MIN: 0, MAX: 1},
    {ID: ram+'StreetName', MIN: 0, MAX: 1},
    {ID: ram+'CityName', MIN: 0, MAX: 1},
    {ID: ram+'CountrySubDivisionID', MIN: 0, MAX: 1},
    {ID: ram+'CountryID', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'DepartmentName', MIN: 0, MAX: 1},
    {ID: ram+'PostOfficeBox', MIN: 0, MAX: 1},
    {ID: ram+'CityID', MIN: 0, MAX: 1},
    {ID: ram+'CountrySubDivisionName', MIN: 0, MAX: 1},
    {ID: ram+'CountryName', MIN: 0, MAX: 1},
]}

sequences[ram+'GeographicalCoordinateType'] = {ID: ram+'GeographicalCoordinateType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'AltitudeMeasure', MIN: 0, MAX: 1},
    {ID: ram+'LatitudeMeasure', MIN: 0, MAX: 1},
    {ID: ram+'LongitudeMeasure', MIN: 0, MAX: 1},
    {ID: ram+'SystemID', MIN: 0, MAX: 1},
]}

sequences[ram+'LegalRegistrationType'] = {ID: ram+'LegalRegistrationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'ID', MIN: 0, MAX: 1},
]}

sequences[ram+'MaterialGoodsCharacteristicType'] = {ID: ram+'MaterialGoodsCharacteristicType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'ProportionalConstituentPercent', MIN: 0, MAX: 1},
    {ID: ram+'AbsolutePresenceWeightMeasure', MIN: 0, MAX: 1},
    {ID: ram+'AbsolutePresenceVolumeMeasure', MIN: 0, MAX: 1},
]}

sequences[ram+'NoteType'] = {ID: ram+'NoteType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'Subject', MIN: 0, MAX: 1},
    {ID: ram+'ContentCode', MIN: 0, MAX: 1},
    {ID: ram+'Content', MIN: 0, MAX: 99999},
    {ID: ram+'SubjectCode', MIN: 0, MAX: 1},
    {ID: ram+'ID', MIN: 0, MAX: 1},
]}

sequences[ram+'ProcuringProjectType'] = {ID: ram+'ProcuringProjectType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 1, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 1, MAX: 1},
]}

sequences[ram+'ProductCharacteristicConditionType'] = {ID: ram+'ProductCharacteristicConditionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 99999},
    {ID: ram+'ValueMeasure', MIN: 0, MAX: 1},
]}

sequences[ram+'ReferencedProductType'] = {ID: ram+'ReferencedProductType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 99999},
    {ID: ram+'GlobalID', MIN: 0, MAX: 99999},
    {ID: ram+'SellerAssignedID', MIN: 0, MAX: 1},
    {ID: ram+'BuyerAssignedID', MIN: 0, MAX: 1},
    {ID: ram+'ManufacturerAssignedID', MIN: 0, MAX: 99999},
    {ID: ram+'IndustryAssignedID', MIN: 0, MAX: 99999},
    {ID: ram+'Name', MIN: 0, MAX: 99999},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'RelationshipTypeCode', MIN: 0, MAX: 99999},
    {ID: ram+'UnitQuantity', MIN: 0, MAX: 99999},
]}

sequences[ram+'ReferencedStandardType'] = {ID: ram+'ReferencedStandardType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'VersionID', MIN: 0, MAX: 1},
    {ID: ram+'ElementVersionID', MIN: 0, MAX: 1},
    {ID: ram+'URIID', MIN: 0, MAX: 1},
    {ID: ram+'PartID', MIN: 0, MAX: 1},
    {ID: ram+'AgencyID', MIN: 0, MAX: 1},
]}

sequences[ram+'SpatialDimensionType'] = {ID: ram+'SpatialDimensionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ValueMeasure', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'WidthMeasure', MIN: 0, MAX: 1},
    {ID: ram+'LengthMeasure', MIN: 0, MAX: 1},
    {ID: ram+'HeightMeasure', MIN: 0, MAX: 1},
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'DiameterMeasure', MIN: 0, MAX: 1},
]}

sequences[ram+'SpecificationQueryType'] = {ID: ram+'SpecificationQueryType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 1, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Content', MIN: 1, MAX: 1},
    {ID: ram+'ContractualLanguageCode', MIN: 0, MAX: 1},
]}

sequences[ram+'SpecificationResponseType'] = {ID: ram+'SpecificationResponseType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 1, MAX: 1},
    {ID: ram+'QueryID', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Content', MIN: 1, MAX: 1},
    {ID: ram+'ContractualLanguageCode', MIN: 0, MAX: 1},
]}

sequences[ram+'TradeAccountingAccountType'] = {ID: ram+'TradeAccountingAccountType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 1, MAX: 1},
    {ID: ram+'SetTriggerCode', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'AmountTypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 1},
    {ID: ram+'CostReferenceDimensionPattern', MIN: 0, MAX: 1},
]}

sequences[ram+'TradeAddressType'] = {ID: ram+'TradeAddressType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'PostcodeCode', MIN: 0, MAX: 1},
    {ID: ram+'PostOfficeBox', MIN: 0, MAX: 1},
    {ID: ram+'BuildingName', MIN: 0, MAX: 1},
    {ID: ram+'LineOne', MIN: 0, MAX: 1},
    {ID: ram+'LineTwo', MIN: 0, MAX: 1},
    {ID: ram+'LineThree', MIN: 0, MAX: 1},
    {ID: ram+'LineFour', MIN: 0, MAX: 1},
    {ID: ram+'LineFive', MIN: 0, MAX: 1},
    {ID: ram+'StreetName', MIN: 0, MAX: 1},
    {ID: ram+'CityName', MIN: 0, MAX: 1},
    {ID: ram+'CitySubDivisionName', MIN: 0, MAX: 1},
    {ID: ram+'CountryID', MIN: 0, MAX: 1},
    {ID: ram+'CountryName', MIN: 0, MAX: 99999},
    {ID: ram+'CountrySubDivisionID', MIN: 0, MAX: 1},
    {ID: ram+'CountrySubDivisionName', MIN: 0, MAX: 99999},
    {ID: ram+'AttentionOf', MIN: 0, MAX: 1},
    {ID: ram+'CareOf', MIN: 0, MAX: 1},
    {ID: ram+'BuildingNumber', MIN: 0, MAX: 1},
    {ID: ram+'DepartmentName', MIN: 0, MAX: 1},
    {ID: ram+'AdditionalStreetName', MIN: 0, MAX: 1},
]}

sequences[ram+'TradeCountrySubDivisionType'] = {ID: ram+'TradeCountrySubDivisionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 99999},
]}

sequences[ram+'TradeLocationType'] = {ID: ram+'TradeLocationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'CountryID', MIN: 0, MAX: 1},
    {ID: ram+'CountryName', MIN: 0, MAX: 1},
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 1},
]}

sequences[ram+'TradeSettlementHeaderMonetarySummationType'] = {ID: ram+'TradeSettlementHeaderMonetarySummationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'LineTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'ChargeTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'AllowanceTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TaxBasisTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TaxTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'RoundingAmount', MIN: 0, MAX: 99999},
    {ID: ram+'GrandTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'InformationAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TotalPrepaidAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TotalDiscountAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TotalAllowanceChargeAmount', MIN: 0, MAX: 99999},
    {ID: ram+'DuePayableAmount', MIN: 0, MAX: 99999},
    {ID: ram+'RetailValueExcludingTaxInformationAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TotalDepositFeeInformationAmount', MIN: 0, MAX: 99999},
    {ID: ram+'ProductValueExcludingTobaccoTaxInformationAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TotalRetailValueInformationAmount', MIN: 0, MAX: 99999},
    {ID: ram+'GrossLineTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'NetLineTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'NetIncludingTaxesLineTotalAmount', MIN: 0, MAX: 99999},
]}

sequences[ram+'TradeSettlementLineMonetarySummationType'] = {ID: ram+'TradeSettlementLineMonetarySummationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'LineTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'ChargeTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'AllowanceTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TaxBasisTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TaxTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'GrandTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'InformationAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TotalAllowanceChargeAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TotalRetailValueInformationAmount', MIN: 0, MAX: 99999},
    {ID: ram+'GrossLineTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'NetLineTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'NetIncludingTaxesLineTotalAmount', MIN: 0, MAX: 99999},
    {ID: ram+'ProductWeightLossInformationAmount', MIN: 0, MAX: 99999},
]}

sequences[ram+'TransportCargoType'] = {ID: ram+'TransportCargoType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Identification', MIN: 0, MAX: 1},
    {ID: ram+'OperationalCategoryCode', MIN: 0, MAX: 1},
    {ID: ram+'StatisticalClassificationCode', MIN: 0, MAX: 1},
]}

sequences[ram+'UniversalCommunicationType'] = {ID: ram+'UniversalCommunicationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'URIID', MIN: 0, MAX: 1},
    {ID: ram+'ChannelCode', MIN: 0, MAX: 1},
    {ID: ram+'CompleteNumber', MIN: 0, MAX: 1},
]}

sequences[udt+'DateTimeType'] = {ID: udt+'DateTimeType', MIN: 1, MAX: 1, LEVEL: [
    {ID: udt+'DateTimeString', MIN: 0, MAX: 1},
    {ID: udt+'DateTime', MIN: 0, MAX: 1},
]}

sequences[udt+'DateType'] = {ID: udt+'DateType', MIN: 1, MAX: 1, LEVEL: [
    {ID: udt+'DateString', MIN: 0, MAX: 1},
    {ID: udt+'Date', MIN: 0, MAX: 1},
]}

sequences[udt+'IndicatorType'] = {ID: udt+'IndicatorType', MIN: 1, MAX: 1, LEVEL: [
    {ID: udt+'IndicatorString', MIN: 0, MAX: 1},
    {ID: udt+'Indicator', MIN: 0, MAX: 1},
]}

sequences[ram+'AppliedTaxType'] = {ID: ram+'AppliedTaxType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'CalculatedAmount', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'CalculatedRate', MIN: 0, MAX: 1},
    {ID: ram+'BasisAmount', MIN: 0, MAX: 1},
    {ID: ram+'TaxPointDate', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateType')},
]}

sequences[ram+'AvailablePeriodType'] = {ID: ram+'AvailablePeriodType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'StartDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'EndDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'Description', MIN: 0, MAX: 1},
]}

sequences[ram+'BranchFinancialInstitutionType'] = {ID: ram+'BranchFinancialInstitutionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 1},
    {ID: ram+'LocationFinancialInstitutionAddress', MIN: 0, MAX: 1, LEVEL: sequence(ram+'FinancialInstitutionAddressType')},
]}

sequences[ram+'DeliveryAdjustmentType'] = {ID: ram+'DeliveryAdjustmentType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ReasonCode', MIN: 0, MAX: 1},
    {ID: ram+'Reason', MIN: 0, MAX: 99999},
    {ID: ram+'ActualAmount', MIN: 0, MAX: 99999},
    {ID: ram+'ActualQuantity', MIN: 0, MAX: 1},
    {ID: ram+'ActualDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
]}

sequences[ram+'DocumentLineDocumentType'] = {ID: ram+'DocumentLineDocumentType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'LineID', MIN: 0, MAX: 1},
    {ID: ram+'ParentLineID', MIN: 0, MAX: 1},
    {ID: ram+'LineStatusCode', MIN: 0, MAX: 1},
    {ID: ram+'LineStatusReasonCode', MIN: 0, MAX: 1},
    {ID: ram+'IncludedNote', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'NoteType')},
]}

sequences[ram+'DocumentVersionType'] = {ID: ram+'DocumentVersionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 1},
    {ID: ram+'IssueDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
]}

sequences[ram+'LegalOrganizationType'] = {ID: ram+'LegalOrganizationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'LegalClassificationCode', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 1},
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'TradingBusinessName', MIN: 0, MAX: 1},
    {ID: ram+'PostalTradeAddress', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeAddressType')},
    {ID: ram+'AuthorizedLegalRegistration', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'LegalRegistrationType')},
]}

sequences[ram+'LogisticsLocationType'] = {ID: ram+'LogisticsLocationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 99999},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'PhysicalGeographicalCoordinate', MIN: 0, MAX: 1, LEVEL: sequence(ram+'GeographicalCoordinateType')},
    {ID: ram+'PostalTradeAddress', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeAddressType')},
]}

sequences[ram+'LogisticsTransportEquipmentType'] = {ID: ram+'LogisticsTransportEquipmentType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'LoadingLengthMeasure', MIN: 0, MAX: 1},
    {ID: ram+'CategoryCode', MIN: 0, MAX: 1},
    {ID: ram+'CharacteristicCode', MIN: 0, MAX: 1},
    {ID: ram+'UsedCapacityCode', MIN: 0, MAX: 1},
    {ID: ram+'LinearSpatialDimension', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpatialDimensionType')},
]}

sequences[ram+'PackagingMarkingType'] = {ID: ram+'PackagingMarkingType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'TypeCode', MIN: 0, MAX: 99999},
    {ID: ram+'Content', MIN: 0, MAX: 99999},
    {ID: ram+'ContentDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'ContentAmount', MIN: 0, MAX: 99999},
    {ID: ram+'BarcodeTypeCode', MIN: 0, MAX: 99999},
    {ID: ram+'ContentCode', MIN: 0, MAX: 99999},
    {ID: ram+'AutomaticDataCaptureMethodTypeCode', MIN: 0, MAX: 99999},
]}

sequences[ram+'RecordedStatusType'] = {ID: ram+'RecordedStatusType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ConditionCode', MIN: 1, MAX: 1},
    {ID: ram+'ChangerName', MIN: 0, MAX: 1},
    {ID: ram+'ChangedDateTime', MIN: 1, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
]}

sequences[ram+'ReferencePriceType'] = {ID: ram+'ReferencePriceType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ChargeAmount', MIN: 0, MAX: 1},
    {ID: ram+'BasisQuantity', MIN: 0, MAX: 99999},
    {ID: ram+'NetPriceIndicator', MIN: 0, MAX: 99999, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'ComparisonMethodCode', MIN: 0, MAX: 1},
]}

sequences[ram+'RegisteredTaxType'] = {ID: ram+'RegisteredTaxType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'ExemptionReasonCode', MIN: 0, MAX: 1},
    {ID: ram+'ExemptionReason', MIN: 0, MAX: 99999},
    {ID: ram+'CurrencyCode', MIN: 0, MAX: 1},
    {ID: ram+'Jurisdiction', MIN: 0, MAX: 99999},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'CustomsDutyIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
]}

sequences[ram+'SpecifiedPeriodType'] = {ID: ram+'SpecifiedPeriodType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'DurationMeasure', MIN: 0, MAX: 99999},
    {ID: ram+'InclusiveIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'StartDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'EndDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'CompleteDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'OpenIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'SeasonCode', MIN: 0, MAX: 1},
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 99999},
    {ID: ram+'SequenceNumeric', MIN: 0, MAX: 1},
    {ID: ram+'StartDateFlexibilityCode', MIN: 0, MAX: 1},
    {ID: ram+'ContinuousIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'PurposeCode', MIN: 0, MAX: 1},
]}

sequences[ram+'SupplyChainConsignmentItemType'] = {ID: ram+'SupplyChainConsignmentItemType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'TypeExtensionCode', MIN: 0, MAX: 1},
    {ID: ram+'DeclaredValueForCustomsAmount', MIN: 0, MAX: 1},
    {ID: ram+'DeclaredValueForStatisticsAmount', MIN: 0, MAX: 1},
    {ID: ram+'InvoiceAmount', MIN: 0, MAX: 99999},
    {ID: ram+'GrossWeightMeasure', MIN: 0, MAX: 1},
    {ID: ram+'NetWeightMeasure', MIN: 0, MAX: 1},
    {ID: ram+'TariffQuantity', MIN: 0, MAX: 1},
    {ID: ram+'NatureIdentificationTransportCargo', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TransportCargoType')},
]}

sequences[ram+'TradeContactType'] = {ID: ram+'TradeContactType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'PersonName', MIN: 0, MAX: 1},
    {ID: ram+'DepartmentName', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'JobTitle', MIN: 0, MAX: 1},
    {ID: ram+'Responsibility', MIN: 0, MAX: 1},
    {ID: ram+'PersonID', MIN: 0, MAX: 99999},
    {ID: ram+'TelephoneUniversalCommunication', MIN: 0, MAX: 1, LEVEL: sequence(ram+'UniversalCommunicationType')},
    {ID: ram+'DirectTelephoneUniversalCommunication', MIN: 0, MAX: 1, LEVEL: sequence(ram+'UniversalCommunicationType')},
    {ID: ram+'MobileTelephoneUniversalCommunication', MIN: 0, MAX: 1, LEVEL: sequence(ram+'UniversalCommunicationType')},
    {ID: ram+'FaxUniversalCommunication', MIN: 0, MAX: 1, LEVEL: sequence(ram+'UniversalCommunicationType')},
    {ID: ram+'EmailURIUniversalCommunication', MIN: 0, MAX: 1, LEVEL: sequence(ram+'UniversalCommunicationType')},
    {ID: ram+'TelexUniversalCommunication', MIN: 0, MAX: 1, LEVEL: sequence(ram+'UniversalCommunicationType')},
    {ID: ram+'VOIPUniversalCommunication', MIN: 0, MAX: 1, LEVEL: sequence(ram+'UniversalCommunicationType')},
    {ID: ram+'InstantMessagingUniversalCommunication', MIN: 0, MAX: 1, LEVEL: sequence(ram+'UniversalCommunicationType')},
    {ID: ram+'SpecifiedNote', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'NoteType')},
    {ID: ram+'SpecifiedContactPerson', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ContactPersonType')},
]}

sequences[ram+'TradeCountryType'] = {ID: ram+'TradeCountryType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 99999},
    {ID: ram+'SubordinateTradeCountrySubDivision', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeCountrySubDivisionType')},
]}

sequences[ram+'TradeDeliveryTermsType'] = {ID: ram+'TradeDeliveryTermsType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'DeliveryTypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'RelevantTradeLocation', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeLocationType')},
]}

sequences[ram+'TradePaymentDiscountTermsType'] = {ID: ram+'TradePaymentDiscountTermsType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'BasisDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'BasisPeriodMeasure', MIN: 0, MAX: 1},
    {ID: ram+'BasisAmount', MIN: 0, MAX: 1},
    {ID: ram+'CalculationPercent', MIN: 0, MAX: 1},
    {ID: ram+'ActualDiscountAmount', MIN: 0, MAX: 1},
]}

sequences[ram+'TradePaymentPenaltyTermsType'] = {ID: ram+'TradePaymentPenaltyTermsType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'BasisDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'BasisPeriodMeasure', MIN: 0, MAX: 1},
    {ID: ram+'BasisAmount', MIN: 0, MAX: 1},
    {ID: ram+'CalculationPercent', MIN: 0, MAX: 1},
    {ID: ram+'ActualPenaltyAmount', MIN: 0, MAX: 1},
]}

sequences[ram+'TradeSettlementFinancialCardType'] = {ID: ram+'TradeSettlementFinancialCardType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'MicrochipIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'CardholderName', MIN: 0, MAX: 1},
    {ID: ram+'ExpiryDate', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateType')},
    {ID: ram+'VerificationNumeric', MIN: 0, MAX: 1},
    {ID: ram+'ValidFromDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'CreditLimitAmount', MIN: 0, MAX: 99999},
    {ID: ram+'CreditAvailableAmount', MIN: 0, MAX: 99999},
    {ID: ram+'InterestRatePercent', MIN: 0, MAX: 1},
    {ID: ram+'IssuingCompanyName', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 1},
]}

sequences[ram+'TradeTaxType'] = {ID: ram+'TradeTaxType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'CalculatedAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'ExemptionReason', MIN: 0, MAX: 1},
    {ID: ram+'CalculatedRate', MIN: 0, MAX: 1},
    {ID: ram+'CalculationSequenceNumeric', MIN: 0, MAX: 1},
    {ID: ram+'BasisQuantity', MIN: 0, MAX: 1},
    {ID: ram+'BasisAmount', MIN: 0, MAX: 99999},
    {ID: ram+'UnitBasisAmount', MIN: 0, MAX: 99999},
    {ID: ram+'LineTotalBasisAmount', MIN: 0, MAX: 99999},
    {ID: ram+'AllowanceChargeBasisAmount', MIN: 0, MAX: 99999},
    {ID: ram+'CategoryCode', MIN: 0, MAX: 1},
    {ID: ram+'CurrencyCode', MIN: 0, MAX: 1},
    {ID: ram+'Jurisdiction', MIN: 0, MAX: 99999},
    {ID: ram+'CustomsDutyIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'ExemptionReasonCode', MIN: 0, MAX: 1},
    {ID: ram+'TaxBasisAllowanceRate', MIN: 0, MAX: 1},
    {ID: ram+'TaxPointDate', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateType')},
    {ID: ram+'Type', MIN: 0, MAX: 1},
    {ID: ram+'InformationAmount', MIN: 0, MAX: 99999},
    {ID: ram+'CategoryName', MIN: 0, MAX: 99999},
    {ID: ram+'DueDateTypeCode', MIN: 0, MAX: 1},
    {ID: ram+'RateApplicablePercent', MIN: 0, MAX: 1},
    {ID: ram+'SpecifiedTradeAccountingAccount', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'ServiceSupplyTradeCountry', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeCountryType')},
    {ID: ram+'BuyerRepayableTaxSpecifiedTradeAccountingAccount', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'SellerPayableTaxSpecifiedTradeAccountingAccount', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'SellerRefundableTaxSpecifiedTradeAccountingAccount', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'BuyerDeductibleTaxSpecifiedTradeAccountingAccount', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'BuyerNonDeductibleTaxSpecifiedTradeAccountingAccount', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'PlaceApplicableTradeLocation', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeLocationType')},
]}

sequences[ram+'TaxRegistrationType'] = {ID: ram+'TaxRegistrationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'AssociatedRegisteredTax', MIN: 0, MAX: 1, LEVEL: sequence(ram+'RegisteredTaxType')},
]}

sequences[ram+'SpecifiedBinaryFileType'] = {ID: ram+'SpecifiedBinaryFileType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 99999},
    {ID: ram+'Title', MIN: 0, MAX: 99999},
    {ID: ram+'AuthorName', MIN: 0, MAX: 99999},
    {ID: ram+'VersionID', MIN: 0, MAX: 1},
    {ID: ram+'FileName', MIN: 0, MAX: 1},
    {ID: ram+'URIID', MIN: 0, MAX: 1},
    {ID: ram+'MIMECode', MIN: 0, MAX: 1},
    {ID: ram+'EncodingCode', MIN: 0, MAX: 1},
    {ID: ram+'CharacterSetCode', MIN: 0, MAX: 1},
    {ID: ram+'IncludedBinaryObject', MIN: 0, MAX: 99999},
    {ID: ram+'Access', MIN: 0, MAX: 99999},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'SizeMeasure', MIN: 0, MAX: 1},
    {ID: ram+'AccessAvailabilitySpecifiedPeriod', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpecifiedPeriodType')},
]}

sequences[ram+'TradePartyType'] = {ID: ram+'TradePartyType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 99999},
    {ID: ram+'GlobalID', MIN: 0, MAX: 99999},
    {ID: ram+'Name', MIN: 0, MAX: 1},
    {ID: ram+'RoleCode', MIN: 0, MAX: 99999},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'SpecifiedLegalOrganization', MIN: 0, MAX: 1, LEVEL: sequence(ram+'LegalOrganizationType')},
    {ID: ram+'DefinedTradeContact', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeContactType')},
    {ID: ram+'PostalTradeAddress', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeAddressType')},
    {ID: ram+'URIUniversalCommunication', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'UniversalCommunicationType')},
    {ID: ram+'SpecifiedTaxRegistration', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TaxRegistrationType')},
    {ID: ram+'EndPointURIUniversalCommunication', MIN: 0, MAX: 1, LEVEL: sequence(ram+'UniversalCommunicationType')},
    {ID: ram+'LogoAssociatedSpecifiedBinaryFile', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SpecifiedBinaryFileType')},
]}

sequences[ram+'ReferencedDocumentType'] = {ID: ram+'ReferencedDocumentType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'IssuerAssignedID', MIN: 0, MAX: 1},
    {ID: ram+'URIID', MIN: 0, MAX: 1},
    {ID: ram+'StatusCode', MIN: 0, MAX: 1},
    {ID: ram+'CopyIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'LineID', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'GlobalID', MIN: 0, MAX: 1},
    {ID: ram+'RevisionID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 99999},
    {ID: ram+'AttachmentBinaryObject', MIN: 0, MAX: 99999},
    {ID: ram+'Information', MIN: 0, MAX: 99999},
    {ID: ram+'ReferenceTypeCode', MIN: 0, MAX: 1},
    {ID: ram+'SectionName', MIN: 0, MAX: 99999},
    {ID: ram+'PreviousRevisionID', MIN: 0, MAX: 99999},
    {ID: ram+'FormattedIssueDateTime', MIN: 0, MAX: 1, LEVEL: sequence(qdt+'FormattedDateTimeType')},
    {ID: ram+'EffectiveSpecifiedPeriod', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpecifiedPeriodType')},
    {ID: ram+'IssuerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'AttachedSpecifiedBinaryFile', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SpecifiedBinaryFileType')},
]}

sequences[ram+'TradeCurrencyExchangeType'] = {ID: ram+'TradeCurrencyExchangeType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'SourceCurrencyCode', MIN: 1, MAX: 1},
    {ID: ram+'SourceUnitBasisNumeric', MIN: 0, MAX: 1},
    {ID: ram+'TargetCurrencyCode', MIN: 1, MAX: 1},
    {ID: ram+'TargetUnitBaseNumeric', MIN: 0, MAX: 1},
    {ID: ram+'MarketID', MIN: 0, MAX: 1},
    {ID: ram+'ConversionRate', MIN: 1, MAX: 1},
    {ID: ram+'ConversionRateDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'AssociatedReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
]}

sequences[ram+'TradeAllowanceChargeType'] = {ID: ram+'TradeAllowanceChargeType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ChargeIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'SequenceNumeric', MIN: 0, MAX: 1},
    {ID: ram+'CalculationPercent', MIN: 0, MAX: 1},
    {ID: ram+'BasisAmount', MIN: 0, MAX: 1},
    {ID: ram+'BasisQuantity', MIN: 0, MAX: 1},
    {ID: ram+'PrepaidIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'ActualAmount', MIN: 0, MAX: 99999},
    {ID: ram+'UnitBasisAmount', MIN: 0, MAX: 1},
    {ID: ram+'ReasonCode', MIN: 0, MAX: 1},
    {ID: ram+'Reason', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'CategoryTradeTax', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeTaxType')},
    {ID: ram+'ActualTradeCurrencyExchange', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeCurrencyExchangeType')},
]}

sequences[ram+'TradePriceType'] = {ID: ram+'TradePriceType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'ChargeAmount', MIN: 1, MAX: 99999},
    {ID: ram+'BasisQuantity', MIN: 0, MAX: 1},
    {ID: ram+'MinimumQuantity', MIN: 0, MAX: 1},
    {ID: ram+'MaximumQuantity', MIN: 0, MAX: 1},
    {ID: ram+'ChangeReason', MIN: 0, MAX: 99999},
    {ID: ram+'OrderUnitConversionFactorNumeric', MIN: 0, MAX: 1},
    {ID: ram+'AppliedTradeAllowanceCharge', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAllowanceChargeType')},
    {ID: ram+'ValiditySpecifiedPeriod', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpecifiedPeriodType')},
    {ID: ram+'IncludedTradeTax', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeTaxType')},
    {ID: ram+'DeliveryTradeLocation', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeLocationType')},
    {ID: ram+'TradeComparisonReferencePrice', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencePriceType')},
    {ID: ram+'AssociatedReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
]}

sequences[ram+'SubordinateLineTradeAgreementType'] = {ID: ram+'SubordinateLineTradeAgreementType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'SellerOrderReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'BuyerOrderReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'AdditionalReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'GrossPriceProductTradePrice', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePriceType')},
    {ID: ram+'NetPriceProductTradePrice', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePriceType')},
]}

sequences[ram+'WorkItemComplexDescriptionType'] = {ID: ram+'WorkItemComplexDescriptionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'Abstract', MIN: 0, MAX: 99999},
    {ID: ram+'Content', MIN: 0, MAX: 99999},
    {ID: ram+'ContractualLanguageCode', MIN: 0, MAX: 1},
    {ID: ram+'RequestingSpecificationQuery', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SpecificationQueryType')},
    {ID: ram+'RespondingSpecificationResponse', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SpecificationResponseType')},
    {ID: ram+'SubsetWorkItemComplexDescription', MIN: 0, MAX: 1},
]}

sequences[ram+'SupplyChainEventType'] = {ID: ram+'SupplyChainEventType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'OccurrenceDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'DescriptionBinaryObject', MIN: 0, MAX: 99999},
    {ID: ram+'UnitQuantity', MIN: 0, MAX: 1},
    {ID: ram+'LatestOccurrenceDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'EarliestOccurrenceDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'OccurrenceSpecifiedPeriod', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpecifiedPeriodType')},
    {ID: ram+'OccurrenceLogisticsLocation', MIN: 0, MAX: 1, LEVEL: sequence(ram+'LogisticsLocationType')},
]}

sequences[ram+'LogisticsTransportMeansType'] = {ID: ram+'LogisticsTransportMeansType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Type', MIN: 0, MAX: 1},
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 1},
    {ID: ram+'OwnerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
]}

sequences[ram+'LogisticsTransportMovementType'] = {ID: ram+'LogisticsTransportMovementType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'StageCode', MIN: 0, MAX: 1},
    {ID: ram+'ModeCode', MIN: 0, MAX: 1},
    {ID: ram+'Mode', MIN: 0, MAX: 1},
    {ID: ram+'UsedLogisticsTransportMeans', MIN: 0, MAX: 1, LEVEL: sequence(ram+'LogisticsTransportMeansType')},
]}

sequences[ram+'SupplyChainConsignmentType'] = {ID: ram+'SupplyChainConsignmentType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'GrossWeightMeasure', MIN: 0, MAX: 99999},
    {ID: ram+'NetWeightMeasure', MIN: 0, MAX: 99999},
    {ID: ram+'GrossVolumeMeasure', MIN: 0, MAX: 99999},
    {ID: ram+'InsurancePremiumAmount', MIN: 0, MAX: 1},
    {ID: ram+'AssociatedInvoiceAmount', MIN: 0, MAX: 99999},
    {ID: ram+'TotalChargeAmount', MIN: 0, MAX: 1},
    {ID: ram+'DeclaredValueForCustomsAmount', MIN: 0, MAX: 1},
    {ID: ram+'PackageQuantity', MIN: 0, MAX: 1},
    {ID: ram+'ConsignorTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'ConsigneeTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'CarrierTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'FreightForwarderTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'DeliveryTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'CustomsImportAgentTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'CustomsExportAgentTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'GroupingCentreTradeParty', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'TransportContractReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'AssociatedReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'IncludedSupplyChainConsignmentItem', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SupplyChainConsignmentItemType')},
    {ID: ram+'UtilizedLogisticsTransportEquipment', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'LogisticsTransportEquipmentType')},
    {ID: ram+'SpecifiedLogisticsTransportMovement', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'LogisticsTransportMovementType')},
]}

sequences[ram+'HeaderTradeDeliveryType'] = {ID: ram+'HeaderTradeDeliveryType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'RelatedSupplyChainConsignment', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainConsignmentType')},
    {ID: ram+'ShipToTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'UltimateShipToTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'ShipFromTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'ActualDespatchSupplyChainEvent', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'ActualPickUpSupplyChainEvent', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'ActualDeliverySupplyChainEvent', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'ActualReceiptSupplyChainEvent', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'AdditionalReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'DespatchAdviceReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'ReceivingAdviceReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'DeliveryNoteReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'ConsumptionReportReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'PreviousDeliverySupplyChainEvent', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'PackingListReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
]}

sequences[ram+'HeaderTradeAgreementType'] = {ID: ram+'HeaderTradeAgreementType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'Reference', MIN: 0, MAX: 99999},
    {ID: ram+'BuyerReference', MIN: 0, MAX: 1},
    {ID: ram+'SellerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'BuyerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'SalesAgentTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'BuyerRequisitionerTradeParty', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'BuyerAssignedAccountantTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'SellerAssignedAccountantTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'BuyerTaxRepresentativeTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'SellerTaxRepresentativeTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'ProductEndUserTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'ApplicableTradeDeliveryTerms', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeDeliveryTermsType')},
    {ID: ram+'SellerOrderReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'BuyerOrderReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'QuotationReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'OrderResponseReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'ContractReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'DemandForecastReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'SupplyInstructionReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'PromotionalDealReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'PriceListReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'AdditionalReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'RequisitionerReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'BuyerAgentTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'PurchaseConditionsReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'SpecifiedProcuringProject', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ProcuringProjectType')},
    {ID: ram+'UltimateCustomerOrderReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
]}

sequences[ram+'LogisticsServiceChargeType'] = {ID: ram+'LogisticsServiceChargeType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'PaymentArrangementCode', MIN: 0, MAX: 1},
    {ID: ram+'TariffClassCode', MIN: 0, MAX: 1},
    {ID: ram+'ChargeCategoryCode', MIN: 0, MAX: 1},
    {ID: ram+'ServiceCategoryCode', MIN: 0, MAX: 1},
    {ID: ram+'DisbursementAmount', MIN: 0, MAX: 99999},
    {ID: ram+'AppliedAmount', MIN: 0, MAX: 99999},
    {ID: ram+'AllowanceCharge', MIN: 0, MAX: 1},
    {ID: ram+'PayingPartyRoleCode', MIN: 0, MAX: 1},
    {ID: ram+'CalculationBasisCode', MIN: 0, MAX: 1},
    {ID: ram+'CalculationBasis', MIN: 0, MAX: 1},
    {ID: ram+'TransportPaymentMethodCode', MIN: 0, MAX: 1},
    {ID: ram+'PaymentPlaceLogisticsLocation', MIN: 0, MAX: 1, LEVEL: sequence(ram+'LogisticsLocationType')},
    {ID: ram+'AppliedFromLogisticsLocation', MIN: 0, MAX: 1, LEVEL: sequence(ram+'LogisticsLocationType')},
    {ID: ram+'AppliedToLogisticsLocation', MIN: 0, MAX: 1, LEVEL: sequence(ram+'LogisticsLocationType')},
    {ID: ram+'AppliedTradeTax', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeTaxType')},
]}

sequences[ram+'TradePaymentTermsType'] = {ID: ram+'TradePaymentTermsType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'FromEventCode', MIN: 0, MAX: 1},
    {ID: ram+'SettlementPeriodMeasure', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'DueDateDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'InstructionTypeCode', MIN: 0, MAX: 1},
    {ID: ram+'DirectDebitMandateID', MIN: 0, MAX: 99999},
    {ID: ram+'PartialPaymentPercent', MIN: 0, MAX: 1},
    {ID: ram+'PaymentMeansID', MIN: 0, MAX: 99999},
    {ID: ram+'PartialPaymentAmount', MIN: 0, MAX: 99999},
    {ID: ram+'ApplicableTradePaymentPenaltyTerms', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePaymentPenaltyTermsType')},
    {ID: ram+'ApplicableTradePaymentDiscountTerms', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePaymentDiscountTermsType')},
    {ID: ram+'PayeeTradeParty', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradePartyType')},
]}

sequences[ram+'FinancialAdjustmentType'] = {ID: ram+'FinancialAdjustmentType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ReasonCode', MIN: 0, MAX: 1},
    {ID: ram+'Reason', MIN: 0, MAX: 99999},
    {ID: ram+'ActualAmount', MIN: 0, MAX: 99999},
    {ID: ram+'ActualQuantity', MIN: 0, MAX: 1},
    {ID: ram+'ActualDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'ClaimRelatedTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'InvoiceReferenceReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
]}

sequences[ram+'AdvancePaymentType'] = {ID: ram+'AdvancePaymentType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'PaidAmount', MIN: 1, MAX: 1},
    {ID: ram+'FormattedReceivedDateTime', MIN: 0, MAX: 1, LEVEL: sequence(qdt+'FormattedDateTimeType')},
    {ID: ram+'IncludedTradeTax', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeTaxType')},
]}

sequences[ram+'CreditorFinancialInstitutionType'] = {ID: ram+'CreditorFinancialInstitutionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'BICID', MIN: 0, MAX: 1},
    {ID: ram+'CHIPSUniversalID', MIN: 0, MAX: 1},
    {ID: ram+'NewZealandNCCID', MIN: 0, MAX: 1},
    {ID: ram+'IrishNSCID', MIN: 0, MAX: 1},
    {ID: ram+'UKSortCodeID', MIN: 0, MAX: 1},
    {ID: ram+'CHIPSParticipantID', MIN: 0, MAX: 1},
    {ID: ram+'SwissBCID', MIN: 0, MAX: 1},
    {ID: ram+'FedwireRoutingNumberID', MIN: 0, MAX: 1},
    {ID: ram+'PortugueseNCCID', MIN: 0, MAX: 1},
    {ID: ram+'RussianCentralBankID', MIN: 0, MAX: 1},
    {ID: ram+'ItalianDomesticID', MIN: 0, MAX: 1},
    {ID: ram+'AustrianBankleitzahlID', MIN: 0, MAX: 1},
    {ID: ram+'CanadianPaymentsAssociationID', MIN: 0, MAX: 1},
    {ID: ram+'SICID', MIN: 0, MAX: 1},
    {ID: ram+'GermanBankleitzahlID', MIN: 0, MAX: 1},
    {ID: ram+'SpanishDomesticInterbankingID', MIN: 0, MAX: 1},
    {ID: ram+'SouthAfricanNCCID', MIN: 0, MAX: 1},
    {ID: ram+'HongKongBankID', MIN: 0, MAX: 1},
    {ID: ram+'AustralianBSBID', MIN: 0, MAX: 1},
    {ID: ram+'IndianFinancialSystemID', MIN: 0, MAX: 1},
    {ID: ram+'HellenicBankID', MIN: 0, MAX: 1},
    {ID: ram+'PolishNationalClearingID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 1},
    {ID: ram+'ClearingSystemName', MIN: 0, MAX: 1},
    {ID: ram+'JapanFinancialInstitutionCommonID', MIN: 0, MAX: 1},
    {ID: ram+'LocationFinancialInstitutionAddress', MIN: 0, MAX: 1, LEVEL: sequence(ram+'FinancialInstitutionAddressType')},
    {ID: ram+'SubDivisionBranchFinancialInstitution', MIN: 0, MAX: 1, LEVEL: sequence(ram+'BranchFinancialInstitutionType')},
]}

sequences[ram+'DebtorFinancialInstitutionType'] = {ID: ram+'DebtorFinancialInstitutionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'BICID', MIN: 0, MAX: 1},
    {ID: ram+'ClearingSystemName', MIN: 0, MAX: 1},
    {ID: ram+'CHIPSUniversalID', MIN: 0, MAX: 1},
    {ID: ram+'NewZealandNCCID', MIN: 0, MAX: 1},
    {ID: ram+'IrishNSCID', MIN: 0, MAX: 1},
    {ID: ram+'UKSortCodeID', MIN: 0, MAX: 1},
    {ID: ram+'CHIPSParticipantID', MIN: 0, MAX: 1},
    {ID: ram+'SwissBCID', MIN: 0, MAX: 1},
    {ID: ram+'FedwireRoutingNumberID', MIN: 0, MAX: 1},
    {ID: ram+'PortugueseNCCID', MIN: 0, MAX: 1},
    {ID: ram+'RussianCentralBankID', MIN: 0, MAX: 1},
    {ID: ram+'ItalianDomesticID', MIN: 0, MAX: 1},
    {ID: ram+'AustrianBankleitzahlID', MIN: 0, MAX: 1},
    {ID: ram+'CanadianPaymentsAssociationID', MIN: 0, MAX: 1},
    {ID: ram+'SICID', MIN: 0, MAX: 1},
    {ID: ram+'GermanBankleitzahlID', MIN: 0, MAX: 1},
    {ID: ram+'SpanishDomesticInterbankingID', MIN: 0, MAX: 1},
    {ID: ram+'SouthAfricanNCCID', MIN: 0, MAX: 1},
    {ID: ram+'HongKongBankID', MIN: 0, MAX: 1},
    {ID: ram+'AustralianBSBID', MIN: 0, MAX: 1},
    {ID: ram+'IndianFinancialSystemID', MIN: 0, MAX: 1},
    {ID: ram+'HellenicBankID', MIN: 0, MAX: 1},
    {ID: ram+'PolishNationalClearingID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 1},
    {ID: ram+'JapanFinancialInstitutionCommonID', MIN: 0, MAX: 1},
    {ID: ram+'LocationFinancialInstitutionAddress', MIN: 0, MAX: 1, LEVEL: sequence(ram+'FinancialInstitutionAddressType')},
    {ID: ram+'SubDivisionBranchFinancialInstitution', MIN: 0, MAX: 1, LEVEL: sequence(ram+'BranchFinancialInstitutionType')},
]}

sequences[ram+'TradeSettlementPaymentMeansType'] = {ID: ram+'TradeSettlementPaymentMeansType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'PaymentChannelCode', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'GuaranteeMethodCode', MIN: 0, MAX: 1},
    {ID: ram+'PaymentMethodCode', MIN: 0, MAX: 1},
    {ID: ram+'Information', MIN: 0, MAX: 99999},
    {ID: ram+'ID', MIN: 0, MAX: 99999},
    {ID: ram+'ApplicableTradeSettlementFinancialCard', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeSettlementFinancialCardType')},
    {ID: ram+'PayerPartyDebtorFinancialAccount', MIN: 0, MAX: 1, LEVEL: sequence(ram+'DebtorFinancialAccountType')},
    {ID: ram+'PayeePartyCreditorFinancialAccount', MIN: 0, MAX: 1, LEVEL: sequence(ram+'CreditorFinancialAccountType')},
    {ID: ram+'PayerSpecifiedDebtorFinancialInstitution', MIN: 0, MAX: 1, LEVEL: sequence(ram+'DebtorFinancialInstitutionType')},
    {ID: ram+'PayeeSpecifiedCreditorFinancialInstitution', MIN: 0, MAX: 1, LEVEL: sequence(ram+'CreditorFinancialInstitutionType')},
]}

sequences[ram+'HeaderTradeSettlementType'] = {ID: ram+'HeaderTradeSettlementType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'DuePayableAmount', MIN: 0, MAX: 99999},
    {ID: ram+'CreditorReferenceTypeCode', MIN: 0, MAX: 99999},
    {ID: ram+'CreditorReferenceType', MIN: 0, MAX: 99999},
    {ID: ram+'CreditorReferenceIssuerID', MIN: 0, MAX: 99999},
    {ID: ram+'CreditorReferenceID', MIN: 0, MAX: 1},
    {ID: ram+'PaymentReference', MIN: 0, MAX: 99999},
    {ID: ram+'TaxCurrencyCode', MIN: 0, MAX: 1},
    {ID: ram+'InvoiceCurrencyCode', MIN: 0, MAX: 1},
    {ID: ram+'PaymentCurrencyCode', MIN: 0, MAX: 1},
    {ID: ram+'InvoiceIssuerReference', MIN: 0, MAX: 1},
    {ID: ram+'InvoiceDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'NextInvoiceDateTime', MIN: 0, MAX: 99999, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'CreditReasonCode', MIN: 0, MAX: 1},
    {ID: ram+'CreditReason', MIN: 0, MAX: 99999},
    {ID: ram+'InvoicerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'InvoiceeTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'PayeeTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'PayerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'TaxApplicableTradeCurrencyExchange', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeCurrencyExchangeType')},
    {ID: ram+'InvoiceApplicableTradeCurrencyExchange', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeCurrencyExchangeType')},
    {ID: ram+'PaymentApplicableTradeCurrencyExchange', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeCurrencyExchangeType')},
    {ID: ram+'SpecifiedTradeSettlementPaymentMeans', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeSettlementPaymentMeansType')},
    {ID: ram+'ApplicableTradeTax', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeTaxType')},
    {ID: ram+'BillingSpecifiedPeriod', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpecifiedPeriodType')},
    {ID: ram+'SpecifiedTradeAllowanceCharge', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAllowanceChargeType')},
    {ID: ram+'SubtotalCalculatedTradeTax', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeTaxType')},
    {ID: ram+'SpecifiedLogisticsServiceCharge', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'LogisticsServiceChargeType')},
    {ID: ram+'SpecifiedTradePaymentTerms', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradePaymentTermsType')},
    {ID: ram+'SpecifiedTradeSettlementHeaderMonetarySummation', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeSettlementHeaderMonetarySummationType')},
    {ID: ram+'SpecifiedFinancialAdjustment', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'FinancialAdjustmentType')},
    {ID: ram+'InvoiceReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'ProFormaInvoiceReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'LetterOfCreditReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'FactoringAgreementReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'FactoringListReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'PayableSpecifiedTradeAccountingAccount', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'ReceivableSpecifiedTradeAccountingAccount', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'PurchaseSpecifiedTradeAccountingAccount', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'SalesSpecifiedTradeAccountingAccount', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'SpecifiedTradeSettlementFinancialCard', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeSettlementFinancialCardType')},
    {ID: ram+'SpecifiedAdvancePayment', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'AdvancePaymentType')},
    {ID: ram+'UltimatePayeeTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
]}

sequences[ram+'SpecifiedMarketplaceType'] = {ID: ram+'SpecifiedMarketplaceType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 1},
    {ID: ram+'VirtualIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'WebsiteURIID', MIN: 0, MAX: 99999},
    {ID: ram+'SalesMethodCode', MIN: 0, MAX: 1},
    {ID: ram+'OrderingAvailablePeriod', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'AvailablePeriodType')},
]}

sequences[ram+'LineTradeAgreementType'] = {ID: ram+'LineTradeAgreementType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'BuyerReference', MIN: 0, MAX: 1},
    {ID: ram+'BuyerRequisitionerTradeParty', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'ApplicableTradeDeliveryTerms', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeDeliveryTermsType')},
    {ID: ram+'SellerOrderReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'BuyerOrderReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'QuotationReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'ContractReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'DemandForecastReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'PromotionalDealReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'AdditionalReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'GrossPriceProductTradePrice', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePriceType')},
    {ID: ram+'NetPriceProductTradePrice', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePriceType')},
    {ID: ram+'RequisitionerReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'ItemSellerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'ItemBuyerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'IncludedSpecifiedMarketplace', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpecifiedMarketplaceType')},
    {ID: ram+'UltimateCustomerOrderReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
]}

sequences[ram+'ProductCharacteristicType'] = {ID: ram+'ProductCharacteristicType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 99999},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'ValueMeasure', MIN: 0, MAX: 1},
    {ID: ram+'MeasurementMethodCode', MIN: 0, MAX: 1},
    {ID: ram+'Value', MIN: 0, MAX: 99999},
    {ID: ram+'ValueCode', MIN: 0, MAX: 1},
    {ID: ram+'ValueDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'ValueIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'ContentTypeCode', MIN: 0, MAX: 1},
    {ID: ram+'ValueSpecifiedBinaryFile', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpecifiedBinaryFileType')},
    {ID: ram+'ApplicableProductCharacteristicCondition', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ProductCharacteristicConditionType')},
    {ID: ram+'ApplicableReferencedStandard', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedStandardType')},
]}

sequences[ram+'ProductClassificationType'] = {ID: ram+'ProductClassificationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'SystemID', MIN: 0, MAX: 1},
    {ID: ram+'SystemName', MIN: 0, MAX: 99999},
    {ID: ram+'ClassCode', MIN: 0, MAX: 1},
    {ID: ram+'ClassName', MIN: 0, MAX: 99999},
    {ID: ram+'SubClassCode', MIN: 0, MAX: 1},
    {ID: ram+'ClassProductCharacteristic', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ProductCharacteristicType')},
    {ID: ram+'ApplicableReferencedStandard', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedStandardType')},
]}

sequences[ram+'TradeProductInstanceType'] = {ID: ram+'TradeProductInstanceType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'GlobalSerialID', MIN: 0, MAX: 1},
    {ID: ram+'BatchID', MIN: 0, MAX: 1},
    {ID: ram+'KanbanID', MIN: 0, MAX: 1},
    {ID: ram+'SupplierAssignedSerialID', MIN: 0, MAX: 1},
    {ID: ram+'BestBeforeDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'ExpiryDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'SellByDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'SerialID', MIN: 0, MAX: 99999},
    {ID: ram+'RegistrationID', MIN: 0, MAX: 99999},
    {ID: ram+'ProductionSupplyChainEvent', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'PackagingSupplyChainEvent', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'ApplicableMaterialGoodsCharacteristic', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'MaterialGoodsCharacteristicType')},
    {ID: ram+'ApplicableProductCharacteristic', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ProductCharacteristicType')},
]}

sequences[ram+'TradeProductType'] = {ID: ram+'TradeProductType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'GlobalID', MIN: 0, MAX: 1},
    {ID: ram+'SellerAssignedID', MIN: 0, MAX: 1},
    {ID: ram+'BuyerAssignedID', MIN: 0, MAX: 1},
    {ID: ram+'ManufacturerAssignedID', MIN: 0, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 99999},
    {ID: ram+'TradeName', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'NetWeightMeasure', MIN: 0, MAX: 1},
    {ID: ram+'GrossWeightMeasure', MIN: 0, MAX: 1},
    {ID: ram+'ProductGroupID', MIN: 0, MAX: 99999},
    {ID: ram+'EndItemTypeCode', MIN: 0, MAX: 99999},
    {ID: ram+'EndItemName', MIN: 0, MAX: 99999},
    {ID: ram+'AreaDensityMeasure', MIN: 0, MAX: 1},
    {ID: ram+'UseDescription', MIN: 0, MAX: 99999},
    {ID: ram+'BrandName', MIN: 0, MAX: 1},
    {ID: ram+'SubBrandName', MIN: 0, MAX: 1},
    {ID: ram+'DrainedNetWeightMeasure', MIN: 0, MAX: 1},
    {ID: ram+'VariableMeasureIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'ColourCode', MIN: 0, MAX: 1},
    {ID: ram+'ColourDescription', MIN: 0, MAX: 99999},
    {ID: ram+'Designation', MIN: 0, MAX: 99999},
    {ID: ram+'FormattedCancellationAnnouncedLaunchDateTime', MIN: 0, MAX: 1, LEVEL: sequence(qdt+'FormattedDateTimeType')},
    {ID: ram+'FormattedLatestProductDataChangeDateTime', MIN: 0, MAX: 1, LEVEL: sequence(qdt+'FormattedDateTimeType')},
    {ID: ram+'ApplicableProductCharacteristic', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ProductCharacteristicType')},
    {ID: ram+'ApplicableMaterialGoodsCharacteristic', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'MaterialGoodsCharacteristicType')},
    {ID: ram+'DesignatedProductClassification', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ProductClassificationType')},
    {ID: ram+'IndividualTradeProductInstance', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeProductInstanceType')},
    {ID: ram+'CertificationEvidenceReferenceReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'InspectionReferenceReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'OriginTradeCountry', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeCountryType')},
    {ID: ram+'LinearSpatialDimension', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpatialDimensionType')},
    {ID: ram+'MinimumLinearSpatialDimension', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpatialDimensionType')},
    {ID: ram+'MaximumLinearSpatialDimension', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpatialDimensionType')},
    {ID: ram+'ManufacturerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'PresentationSpecifiedBinaryFile', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SpecifiedBinaryFileType')},
    {ID: ram+'MSDSReferenceReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'AdditionalReferenceReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'LegalRightsOwnerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'BrandOwnerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'IncludedReferencedProduct', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedProductType')},
    {ID: ram+'InformationNote', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'NoteType')},
]}

sequences[ram+'LineTradeSettlementType'] = {ID: ram+'LineTradeSettlementType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'PaymentReference', MIN: 0, MAX: 99999},
    {ID: ram+'InvoiceIssuerReference', MIN: 0, MAX: 1},
    {ID: ram+'TotalAdjustmentAmount', MIN: 0, MAX: 1},
    {ID: ram+'DiscountIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'ApplicableTradeTax', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeTaxType')},
    {ID: ram+'BillingSpecifiedPeriod', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpecifiedPeriodType')},
    {ID: ram+'SpecifiedTradeAllowanceCharge', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAllowanceChargeType')},
    {ID: ram+'SubtotalCalculatedTradeTax', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeTaxType')},
    {ID: ram+'SpecifiedLogisticsServiceCharge', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'LogisticsServiceChargeType')},
    {ID: ram+'SpecifiedTradePaymentTerms', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradePaymentTermsType')},
    {ID: ram+'SpecifiedTradeSettlementLineMonetarySummation', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeSettlementLineMonetarySummationType')},
    {ID: ram+'SpecifiedFinancialAdjustment', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'FinancialAdjustmentType')},
    {ID: ram+'InvoiceReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'AdditionalReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'PayableSpecifiedTradeAccountingAccount', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'ReceivableSpecifiedTradeAccountingAccount', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'PurchaseSpecifiedTradeAccountingAccount', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'SalesSpecifiedTradeAccountingAccount', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeAccountingAccountType')},
    {ID: ram+'SpecifiedTradeSettlementFinancialCard', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeSettlementFinancialCardType')},
]}

sequences[ram+'ReturnableAssetInstructionsType'] = {ID: ram+'ReturnableAssetInstructionsType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'MaterialID', MIN: 0, MAX: 99999},
    {ID: ram+'TermsAndConditionsDescription', MIN: 0, MAX: 99999},
    {ID: ram+'TermsAndConditionsDescriptionCode', MIN: 0, MAX: 1},
    {ID: ram+'DepositValueSpecifiedAmount', MIN: 0, MAX: 99999},
    {ID: ram+'DepositValueValiditySpecifiedPeriod', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpecifiedPeriodType')},
]}

sequences[ram+'SupplyChainPackagingType'] = {ID: ram+'SupplyChainPackagingType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'Type', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'ConditionCode', MIN: 0, MAX: 1},
    {ID: ram+'DisposalMethodCode', MIN: 0, MAX: 99999},
    {ID: ram+'WeightMeasure', MIN: 0, MAX: 99999},
    {ID: ram+'MaximumStackabilityQuantity', MIN: 0, MAX: 1},
    {ID: ram+'MaximumStackabilityWeightMeasure', MIN: 0, MAX: 1},
    {ID: ram+'CustomerFacingTotalUnitQuantity', MIN: 0, MAX: 1},
    {ID: ram+'LayerTotalUnitQuantity', MIN: 0, MAX: 1},
    {ID: ram+'ContentLayerQuantity', MIN: 0, MAX: 1},
    {ID: ram+'LinearSpatialDimension', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpatialDimensionType')},
    {ID: ram+'MinimumLinearSpatialDimension', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpatialDimensionType')},
    {ID: ram+'MaximumLinearSpatialDimension', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpatialDimensionType')},
    {ID: ram+'SpecifiedPackagingMarking', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'PackagingMarkingType')},
    {ID: ram+'ApplicableMaterialGoodsCharacteristic', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'MaterialGoodsCharacteristicType')},
    {ID: ram+'ApplicableDisposalInstructions', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'DisposalInstructionsType')},
    {ID: ram+'ApplicableReturnableAssetInstructions', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReturnableAssetInstructionsType')},
]}

sequences[ram+'SubordinateLineTradeDeliveryType'] = {ID: ram+'SubordinateLineTradeDeliveryType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'PackageQuantity', MIN: 0, MAX: 1},
    {ID: ram+'ProductUnitQuantity', MIN: 0, MAX: 1},
    {ID: ram+'PerPackageUnitQuantity', MIN: 0, MAX: 1},
    {ID: ram+'IncludedSupplyChainPackaging', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SupplyChainPackagingType')},
]}

sequences[ram+'SubordinateLineTradeSettlementType'] = {ID: ram+'SubordinateLineTradeSettlementType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ApplicableTradeTax', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeTaxType')},
]}

sequences[ram+'SubordinateTradeLineItemType'] = {ID: ram+'SubordinateTradeLineItemType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 99999},
    {ID: ram+'SpecifiedReferencedProduct', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedProductType')},
    {ID: ram+'ApplicableTradeProduct', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'TradeProductType')},
    {ID: ram+'SpecifiedSubordinateLineTradeAgreement', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SubordinateLineTradeAgreementType')},
    {ID: ram+'SpecifiedSubordinateLineTradeDelivery', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SubordinateLineTradeDeliveryType')},
    {ID: ram+'SpecifiedSubordinateLineTradeSettlement', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SubordinateLineTradeSettlementType')},
]}

sequences[ram+'LineTradeDeliveryType'] = {ID: ram+'LineTradeDeliveryType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'RequestedQuantity', MIN: 0, MAX: 1},
    {ID: ram+'ReceivedQuantity', MIN: 0, MAX: 1},
    {ID: ram+'BilledQuantity', MIN: 0, MAX: 1},
    {ID: ram+'ChargeFreeQuantity', MIN: 0, MAX: 1},
    {ID: ram+'PackageQuantity', MIN: 0, MAX: 1},
    {ID: ram+'ProductUnitQuantity', MIN: 0, MAX: 1},
    {ID: ram+'PerPackageUnitQuantity', MIN: 0, MAX: 1},
    {ID: ram+'NetWeightMeasure', MIN: 0, MAX: 1},
    {ID: ram+'GrossWeightMeasure', MIN: 0, MAX: 1},
    {ID: ram+'TheoreticalWeightMeasure', MIN: 0, MAX: 1},
    {ID: ram+'DespatchedQuantity', MIN: 0, MAX: 1},
    {ID: ram+'SpecifiedDeliveryAdjustment', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'DeliveryAdjustmentType')},
    {ID: ram+'IncludedSupplyChainPackaging', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SupplyChainPackagingType')},
    {ID: ram+'RelatedSupplyChainConsignment', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainConsignmentType')},
    {ID: ram+'ShipToTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'UltimateShipToTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'ShipFromTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
    {ID: ram+'ActualDespatchSupplyChainEvent', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'ActualPickUpSupplyChainEvent', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'RequestedDeliverySupplyChainEvent', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'ActualDeliverySupplyChainEvent', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'ActualReceiptSupplyChainEvent', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SupplyChainEventType')},
    {ID: ram+'AdditionalReferencedDocument', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'DespatchAdviceReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'ReceivingAdviceReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'DeliveryNoteReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'ConsumptionReportReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
    {ID: ram+'PackingListReferencedDocument', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ReferencedDocumentType')},
]}

sequences[ram+'SupplyChainTradeLineItemType'] = {ID: ram+'SupplyChainTradeLineItemType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'DescriptionCode', MIN: 0, MAX: 1},
    {ID: ram+'AssociatedDocumentLineDocument', MIN: 1, MAX: 1, LEVEL: sequence(ram+'DocumentLineDocumentType')},
    {ID: ram+'SpecifiedTradeProduct', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradeProductType')},
    {ID: ram+'SpecifiedLineTradeAgreement', MIN: 0, MAX: 1, LEVEL: sequence(ram+'LineTradeAgreementType')},
    {ID: ram+'SpecifiedLineTradeDelivery', MIN: 0, MAX: 1, LEVEL: sequence(ram+'LineTradeDeliveryType')},
    {ID: ram+'SpecifiedLineTradeSettlement', MIN: 1, MAX: 1, LEVEL: sequence(ram+'LineTradeSettlementType')},
    {ID: ram+'IncludedSubordinateTradeLineItem', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SubordinateTradeLineItemType')},
]}

sequences[ram+'SupplyChainTradeTransactionType'] = {ID: ram+'SupplyChainTradeTransactionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'IncludedSupplyChainTradeLineItem', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SupplyChainTradeLineItemType')},
    {ID: ram+'ApplicableHeaderTradeAgreement', MIN: 1, MAX: 1, LEVEL: sequence(ram+'HeaderTradeAgreementType')},
    {ID: ram+'ApplicableHeaderTradeDelivery', MIN: 1, MAX: 1, LEVEL: sequence(ram+'HeaderTradeDeliveryType')},
    {ID: ram+'ApplicableHeaderTradeSettlement', MIN: 1, MAX: 1, LEVEL: sequence(ram+'HeaderTradeSettlementType')},
]}

sequences[ram+'AppliedAllowanceChargeType'] = {ID: ram+'AppliedAllowanceChargeType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ActualAmount', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 1},
    {ID: ram+'ReasonCode', MIN: 0, MAX: 1},
    {ID: ram+'CalculationPercent', MIN: 0, MAX: 1},
    {ID: ram+'BasisAmount', MIN: 0, MAX: 1},
    {ID: ram+'ChargeIndicator', MIN: 1, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'CategoryAppliedTax', MIN: 0, MAX: 1, LEVEL: sequence(ram+'AppliedTaxType')},
]}

sequences[ram+'CalculatedPriceType'] = {ID: ram+'CalculatedPriceType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'TypeCode', MIN: 0, MAX: 99999},
    {ID: ram+'ChargeAmount', MIN: 0, MAX: 99999},
    {ID: ram+'RelatedAppliedAllowanceCharge', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'AppliedAllowanceChargeType')},
]}

sequences[ram+'WorkItemDimensionType'] = {ID: ram+'WorkItemDimensionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'ValueMeasure', MIN: 1, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 1, MAX: 1},
    {ID: ram+'ContractualLanguageCode', MIN: 0, MAX: 1},
    {ID: ram+'ComponentWorkItemDimension', MIN: 0, MAX: 99999},
]}

sequences[ram+'WorkItemQuantityAnalysisType'] = {ID: ram+'WorkItemQuantityAnalysisType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 1, MAX: 1},
    {ID: ram+'ActualQuantity', MIN: 0, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 1},
    {ID: ram+'ActualQuantityPercent', MIN: 0, MAX: 1},
    {ID: ram+'StatusCode', MIN: 0, MAX: 1},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'PrimaryClassificationCode', MIN: 0, MAX: 99999},
    {ID: ram+'AlternativeClassificationCode', MIN: 0, MAX: 99999},
    {ID: ram+'ContractualLanguageCode', MIN: 0, MAX: 1},
    {ID: ram+'ActualQuantityWorkItemDimension', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'WorkItemDimensionType')},
    {ID: ram+'BreakdownWorkItemQuantityAnalysis', MIN: 0, MAX: 99999},
    {ID: ram+'ChangedRecordedStatus', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'RecordedStatusType')},
]}

sequences[ram+'BasicWorkItemType'] = {ID: ram+'BasicWorkItemType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 1, MAX: 1},
    {ID: ram+'ReferenceID', MIN: 0, MAX: 1},
    {ID: ram+'PrimaryClassificationCode', MIN: 0, MAX: 99999},
    {ID: ram+'AlternativeClassificationCode', MIN: 0, MAX: 99999},
    {ID: ram+'TypeCode', MIN: 0, MAX: 99999},
    {ID: ram+'Comment', MIN: 0, MAX: 99999},
    {ID: ram+'TotalQuantity', MIN: 0, MAX: 1},
    {ID: ram+'TotalQuantityClassificationCode', MIN: 0, MAX: 1},
    {ID: ram+'IndexValue', MIN: 0, MAX: 1},
    {ID: ram+'StatusCode', MIN: 0, MAX: 99999},
    {ID: ram+'ReferenceFileBinaryObject', MIN: 0, MAX: 99999},
    {ID: ram+'Index', MIN: 0, MAX: 1},
    {ID: ram+'RequestedActionCode', MIN: 0, MAX: 99999},
    {ID: ram+'PriceListItemID', MIN: 0, MAX: 1},
    {ID: ram+'ContractualLanguageCode', MIN: 0, MAX: 1},
    {ID: ram+'ActualWorkItemComplexDescription', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'WorkItemComplexDescriptionType')},
    {ID: ram+'TotalQuantityWorkItemQuantityAnalysis', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'WorkItemQuantityAnalysisType')},
    {ID: ram+'UnitCalculatedPrice', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'CalculatedPriceType')},
    {ID: ram+'TotalCalculatedPrice', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'CalculatedPriceType')},
    {ID: ram+'SubordinateBasicWorkItem', MIN: 0, MAX: 99999},
    {ID: ram+'ChangedRecordedStatus', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'RecordedStatusType')},
    {ID: ram+'ItemBasicWorkItem', MIN: 0, MAX: 99999},
    {ID: ram+'ReferencedSpecifiedBinaryFile', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SpecifiedBinaryFileType')},
]}

sequences[ram+'GroupedWorkItemType'] = {ID: ram+'GroupedWorkItemType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 1, MAX: 1},
    {ID: ram+'PrimaryClassificationCode', MIN: 0, MAX: 99999},
    {ID: ram+'AlternativeClassificationCode', MIN: 0, MAX: 99999},
    {ID: ram+'TypeCode', MIN: 0, MAX: 99999},
    {ID: ram+'Comment', MIN: 0, MAX: 99999},
    {ID: ram+'TotalQuantity', MIN: 0, MAX: 1},
    {ID: ram+'Index', MIN: 0, MAX: 1},
    {ID: ram+'RequestedActionCode', MIN: 0, MAX: 99999},
    {ID: ram+'PriceListItemID', MIN: 0, MAX: 1},
    {ID: ram+'ContractualLanguageCode', MIN: 0, MAX: 1},
    {ID: ram+'TotalCalculatedPrice', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'CalculatedPriceType')},
    {ID: ram+'ItemGroupedWorkItem', MIN: 0, MAX: 99999},
    {ID: ram+'ItemBasicWorkItem', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'BasicWorkItemType')},
    {ID: ram+'ChangedRecordedStatus', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'RecordedStatusType')},
    {ID: ram+'ActualWorkItemComplexDescription', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'WorkItemComplexDescriptionType')},
    {ID: ram+'ReferencedSpecifiedBinaryFile', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SpecifiedBinaryFileType')},
]}

sequences[ram+'ValuationBreakdownStatementType'] = {ID: ram+'ValuationBreakdownStatementType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 1, MAX: 1},
    {ID: ram+'Name', MIN: 1, MAX: 1},
    {ID: ram+'Description', MIN: 0, MAX: 99999},
    {ID: ram+'MeasurementMethodID', MIN: 0, MAX: 99999},
    {ID: ram+'CreationDateTime', MIN: 1, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'DefaultCurrencyCode', MIN: 1, MAX: 1},
    {ID: ram+'DefaultLanguageCode', MIN: 1, MAX: 1},
    {ID: ram+'Comment', MIN: 0, MAX: 99999},
    {ID: ram+'TypeCode', MIN: 0, MAX: 99999},
    {ID: ram+'RequestedActionCode', MIN: 0, MAX: 99999},
    {ID: ram+'PriceListID', MIN: 0, MAX: 1},
    {ID: ram+'ContractualLanguageCode', MIN: 0, MAX: 1},
    {ID: ram+'ItemGroupedWorkItem', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'GroupedWorkItemType')},
    {ID: ram+'ItemBasicWorkItem', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'BasicWorkItemType')},
    {ID: ram+'TotalCalculatedPrice', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'CalculatedPriceType')},
    {ID: ram+'ChangedRecordedStatus', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'RecordedStatusType')},
    {ID: ram+'CreationSpecifiedBinaryFile', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SpecifiedBinaryFileType')},
    {ID: ram+'ReaderSpecifiedBinaryFile', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SpecifiedBinaryFileType')},
    {ID: ram+'ReferencedSpecifiedBinaryFile', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'SpecifiedBinaryFileType')},
]}

sequences[ram+'ExchangedDocumentType'] = {ID: ram+'ExchangedDocumentType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 1, MAX: 1},
    {ID: ram+'Name', MIN: 0, MAX: 99999},
    {ID: ram+'TypeCode', MIN: 0, MAX: 1},
    {ID: ram+'IssueDateTime', MIN: 1, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'CopyIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'Purpose', MIN: 0, MAX: 1},
    {ID: ram+'ControlRequirementIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'LanguageID', MIN: 0, MAX: 99999},
    {ID: ram+'PurposeCode', MIN: 0, MAX: 1},
    {ID: ram+'RevisionDateTime', MIN: 0, MAX: 1, LEVEL: sequence(udt+'DateTimeType')},
    {ID: ram+'VersionID', MIN: 0, MAX: 1},
    {ID: ram+'GlobalID', MIN: 0, MAX: 1},
    {ID: ram+'RevisionID', MIN: 0, MAX: 1},
    {ID: ram+'PreviousRevisionID', MIN: 0, MAX: 1},
    {ID: ram+'CategoryCode', MIN: 0, MAX: 1},
    {ID: ram+'IncludedNote', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'NoteType')},
    {ID: ram+'EffectiveSpecifiedPeriod', MIN: 0, MAX: 1, LEVEL: sequence(ram+'SpecifiedPeriodType')},
    {ID: ram+'IssuerTradeParty', MIN: 0, MAX: 1, LEVEL: sequence(ram+'TradePartyType')},
]}

sequences[ram+'DocumentContextParameterType'] = {ID: ram+'DocumentContextParameterType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'ID', MIN: 0, MAX: 1},
    {ID: ram+'Value', MIN: 0, MAX: 1},
    {ID: ram+'SpecifiedDocumentVersion', MIN: 0, MAX: 1, LEVEL: sequence(ram+'DocumentVersionType')},
]}

sequences[ram+'ExchangedDocumentContextType'] = {ID: ram+'ExchangedDocumentContextType', MIN: 1, MAX: 1, LEVEL: [
    {ID: ram+'SpecifiedTransactionID', MIN: 0, MAX: 1},
    {ID: ram+'TestIndicator', MIN: 0, MAX: 1, LEVEL: sequence(udt+'IndicatorType')},
    {ID: ram+'BusinessProcessSpecifiedDocumentContextParameter', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'DocumentContextParameterType')},
    {ID: ram+'BIMSpecifiedDocumentContextParameter', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'DocumentContextParameterType')},
    {ID: ram+'ScenarioSpecifiedDocumentContextParameter', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'DocumentContextParameterType')},
    {ID: ram+'ApplicationSpecifiedDocumentContextParameter', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'DocumentContextParameterType')},
    {ID: ram+'GuidelineSpecifiedDocumentContextParameter', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'DocumentContextParameterType')},
    {ID: ram+'SubsetSpecifiedDocumentContextParameter', MIN: 0, MAX: 99999, LEVEL: sequence(ram+'DocumentContextParameterType')},
    {ID: ram+'MessageStandardSpecifiedDocumentContextParameter', MIN: 0, MAX: 1, LEVEL: sequence(ram+'DocumentContextParameterType')},
]}

sequences[rsm+'CrossIndustryInvoiceType'] = {ID: rsm+'CrossIndustryInvoiceType', MIN: 1, MAX: 1, LEVEL: [
    {ID: rsm+'ExchangedDocumentContext', MIN: 1, MAX: 1, LEVEL: sequence(ram+'ExchangedDocumentContextType')},
    {ID: rsm+'ExchangedDocument', MIN: 1, MAX: 1, LEVEL: sequence(ram+'ExchangedDocumentType')},
    {ID: rsm+'SupplyChainTradeTransaction', MIN: 1, MAX: 1, LEVEL: sequence(ram+'SupplyChainTradeTransactionType')},
    {ID: rsm+'ValuationBreakdownStatement', MIN: 0, MAX: 1, LEVEL: sequence(ram+'ValuationBreakdownStatementType')},
]}
