# -*- coding: utf-8 -*-

from copy import deepcopy
from bots.botsconfig import ID, MIN, MAX, LEVEL

from .UBL21records import (xmlns, ext, cbc, cac, ccts)


sequences = {}


def sequence(seq):
    return deepcopy(sequences[seq][LEVEL])


sequences[cac+'AddressLineType'] = {ID: cac+'AddressLineType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'Line', MIN: 1, MAX: 1},
]}

sequences[cac+'AirTransportType'] = {ID: cac+'AirTransportType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'AircraftID', MIN: 1, MAX: 1},
]}

sequences[cac+'CardAccountType'] = {ID: cac+'CardAccountType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'PrimaryAccountNumberID', MIN: 1, MAX: 1},
    {ID: cbc+'NetworkID', MIN: 1, MAX: 1},
    {ID: cbc+'CardTypeCode', MIN: 0, MAX: 1},
    {ID: cbc+'ValidityStartDate', MIN: 0, MAX: 1},
    {ID: cbc+'ExpiryDate', MIN: 0, MAX: 1},
    {ID: cbc+'IssuerID', MIN: 0, MAX: 1},
    {ID: cbc+'IssueNumberID', MIN: 0, MAX: 1},
    {ID: cbc+'CV2ID', MIN: 0, MAX: 1},
    {ID: cbc+'CardChipCode', MIN: 0, MAX: 1},
    {ID: cbc+'ChipApplicationID', MIN: 0, MAX: 1},
    {ID: cbc+'HolderName', MIN: 0, MAX: 1},
]}

sequences[cac+'ClauseType'] = {ID: cac+'ClauseType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'ID', MIN: 0, MAX: 1},
    {ID: cbc+'Content', MIN: 0, MAX: 99999},
]}

sequences[cac+'CommodityClassificationType'] = {ID: cac+'CommodityClassificationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'NatureCode', MIN: 0, MAX: 1},
    {ID: cbc+'CargoTypeCode', MIN: 0, MAX: 1},
    {ID: cbc+'CommodityCode', MIN: 0, MAX: 1},
    {ID: cbc+'ItemClassificationCode', MIN: 0, MAX: 1},
]}

sequences[cac+'CommunicationType'] = {ID: cac+'CommunicationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'ChannelCode', MIN: 0, MAX: 1},
    {ID: cbc+'Channel', MIN: 0, MAX: 1},
    {ID: cbc+'Value', MIN: 0, MAX: 1},
]}

sequences[cac+'ConditionType'] = {ID: cac+'ConditionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'AttributeID', MIN: 1, MAX: 1},
    {ID: cbc+'Measure', MIN: 0, MAX: 1},
    {ID: cbc+'Description', MIN: 0, MAX: 99999},
    {ID: cbc+'MinimumMeasure', MIN: 0, MAX: 1},
    {ID: cbc+'MaximumMeasure', MIN: 0, MAX: 1},
]}

sequences[cac+'CountryType'] = {ID: cac+'CountryType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'IdentificationCode', MIN: 0, MAX: 1},
    {ID: cbc+'Name', MIN: 0, MAX: 1},
]}

sequences[cac+'CreditAccountType'] = {ID: cac+'CreditAccountType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'AccountID', MIN: 1, MAX: 1},
]}

sequences[cac+'DeliveryUnitType'] = {ID: cac+'DeliveryUnitType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'BatchQuantity', MIN: 1, MAX: 1},
    {ID: cbc+'ConsumerUnitQuantity', MIN: 0, MAX: 1},
    {ID: cbc+'HazardousRiskIndicator', MIN: 0, MAX: 1},
]}

sequences[cac+'DimensionType'] = {ID: cac+'DimensionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'AttributeID', MIN: 1, MAX: 1},
    {ID: cbc+'Measure', MIN: 0, MAX: 1},
    {ID: cbc+'Description', MIN: 0, MAX: 99999},
    {ID: cbc+'MinimumMeasure', MIN: 0, MAX: 1},
    {ID: cbc+'MaximumMeasure', MIN: 0, MAX: 1},
]}

sequences[cac+'ExternalReferenceType'] = {ID: cac+'ExternalReferenceType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'URI', MIN: 0, MAX: 1},
    {ID: cbc+'DocumentHash', MIN: 0, MAX: 1},
    {ID: cbc+'HashAlgorithmMethod', MIN: 0, MAX: 1},
    {ID: cbc+'ExpiryDate', MIN: 0, MAX: 1},
    {ID: cbc+'ExpiryTime', MIN: 0, MAX: 1},
    {ID: cbc+'MimeCode', MIN: 0, MAX: 1},
    {ID: cbc+'FormatCode', MIN: 0, MAX: 1},
    {ID: cbc+'EncodingCode', MIN: 0, MAX: 1},
    {ID: cbc+'CharacterSetCode', MIN: 0, MAX: 1},
    {ID: cbc+'FileName', MIN: 0, MAX: 1},
    {ID: cbc+'Description', MIN: 0, MAX: 99999},
]}

sequences[cac+'ItemPropertyGroupType'] = {ID: cac+'ItemPropertyGroupType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'ID', MIN: 1, MAX: 1},
    {ID: cbc+'Name', MIN: 0, MAX: 1},
    {ID: cbc+'ImportanceCode', MIN: 0, MAX: 1},
]}

sequences[cac+'ItemPropertyRangeType'] = {ID: cac+'ItemPropertyRangeType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'MinimumValue', MIN: 0, MAX: 1},
    {ID: cbc+'MaximumValue', MIN: 0, MAX: 1},
]}

sequences[cac+'LanguageType'] = {ID: cac+'LanguageType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'ID', MIN: 0, MAX: 1},
    {ID: cbc+'Name', MIN: 0, MAX: 1},
    {ID: cbc+'LocaleCode', MIN: 0, MAX: 1},
]}

sequences[cac+'LocationCoordinateType'] = {ID: cac+'LocationCoordinateType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'CoordinateSystemCode', MIN: 0, MAX: 1},
    {ID: cbc+'LatitudeDegreesMeasure', MIN: 0, MAX: 1},
    {ID: cbc+'LatitudeMinutesMeasure', MIN: 0, MAX: 1},
    {ID: cbc+'LatitudeDirectionCode', MIN: 0, MAX: 1},
    {ID: cbc+'LongitudeDegreesMeasure', MIN: 0, MAX: 1},
    {ID: cbc+'LongitudeMinutesMeasure', MIN: 0, MAX: 1},
    {ID: cbc+'LongitudeDirectionCode', MIN: 0, MAX: 1},
    {ID: cbc+'AltitudeMeasure', MIN: 0, MAX: 1},
]}

sequences[cac+'MonetaryTotalType'] = {ID: cac+'MonetaryTotalType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'LineExtensionAmount', MIN: 0, MAX: 1},
    {ID: cbc+'TaxExclusiveAmount', MIN: 0, MAX: 1},
    {ID: cbc+'TaxInclusiveAmount', MIN: 0, MAX: 1},
    {ID: cbc+'AllowanceTotalAmount', MIN: 0, MAX: 1},
    {ID: cbc+'ChargeTotalAmount', MIN: 0, MAX: 1},
    {ID: cbc+'PrepaidAmount', MIN: 0, MAX: 1},
    {ID: cbc+'PayableRoundingAmount', MIN: 0, MAX: 1},
    {ID: cbc+'PayableAmount', MIN: 1, MAX: 1},
    {ID: cbc+'PayableAlternativeAmount', MIN: 0, MAX: 1},
]}

sequences[cac+'PartyIdentificationType'] = {ID: cac+'PartyIdentificationType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'ID', MIN: 1, MAX: 1},
]}

sequences[cac+'PartyNameType'] = {ID: cac+'PartyNameType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'Name', MIN: 1, MAX: 1},
]}

sequences[cac+'PaymentType'] = {ID: cac+'PaymentType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'ID', MIN: 0, MAX: 1},
    {ID: cbc+'PaidAmount', MIN: 0, MAX: 1},
    {ID: cbc+'ReceivedDate', MIN: 0, MAX: 1},
    {ID: cbc+'PaidDate', MIN: 0, MAX: 1},
    {ID: cbc+'PaidTime', MIN: 0, MAX: 1},
    {ID: cbc+'InstructionID', MIN: 0, MAX: 1},
]}

sequences[cac+'PeriodType'] = {ID: cac+'PeriodType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'StartDate', MIN: 0, MAX: 1},
    {ID: cbc+'StartTime', MIN: 0, MAX: 1},
    {ID: cbc+'EndDate', MIN: 0, MAX: 1},
    {ID: cbc+'EndTime', MIN: 0, MAX: 1},
    {ID: cbc+'DurationMeasure', MIN: 0, MAX: 1},
    {ID: cbc+'DescriptionCode', MIN: 0, MAX: 99999},
    {ID: cbc+'Description', MIN: 0, MAX: 99999},
]}

sequences[cac+'PhysicalAttributeType'] = {ID: cac+'PhysicalAttributeType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'AttributeID', MIN: 1, MAX: 1},
    {ID: cbc+'PositionCode', MIN: 0, MAX: 1},
    {ID: cbc+'DescriptionCode', MIN: 0, MAX: 1},
    {ID: cbc+'Description', MIN: 0, MAX: 99999},
]}

sequences[cac+'RailTransportType'] = {ID: cac+'RailTransportType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'TrainID', MIN: 1, MAX: 1},
    {ID: cbc+'RailCarID', MIN: 0, MAX: 1},
]}

sequences[cac+'RoadTransportType'] = {ID: cac+'RoadTransportType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'LicensePlateID', MIN: 1, MAX: 1},
]}

sequences[cac+'SecondaryHazardType'] = {ID: cac+'SecondaryHazardType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'ID', MIN: 0, MAX: 1},
    {ID: cbc+'PlacardNotation', MIN: 0, MAX: 1},
    {ID: cbc+'PlacardEndorsement', MIN: 0, MAX: 1},
    {ID: cbc+'EmergencyProceduresCode', MIN: 0, MAX: 1},
    {ID: cbc+'Extension', MIN: 0, MAX: 99999},
]}

sequences[cac+'ServiceFrequencyType'] = {ID: cac+'ServiceFrequencyType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'WeekDayCode', MIN: 1, MAX: 1},
]}

sequences[cac+'TemperatureType'] = {ID: cac+'TemperatureType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'AttributeID', MIN: 1, MAX: 1},
    {ID: cbc+'Measure', MIN: 1, MAX: 1},
    {ID: cbc+'Description', MIN: 0, MAX: 99999},
]}

sequences[cac+'TransportEquipmentSealType'] = {ID: cac+'TransportEquipmentSealType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'ID', MIN: 1, MAX: 1},
    {ID: cbc+'SealIssuerTypeCode', MIN: 0, MAX: 1},
    {ID: cbc+'Condition', MIN: 0, MAX: 1},
    {ID: cbc+'SealStatusCode', MIN: 0, MAX: 1},
    {ID: cbc+'SealingPartyType', MIN: 0, MAX: 1},
]}

sequences[ext+'UBLExtensionType'] = {ID: ext+'UBLExtensionType', MIN: 1, MAX: 1, LEVEL: [
    {ID: cbc+'ID', MIN: 0, MAX: 1},
    {ID: cbc+'Name', MIN: 0, MAX: 1},
    {ID: ext+'ExtensionAgencyID', MIN: 0, MAX: 1},
    {ID: ext+'ExtensionAgencyName', MIN: 0, MAX: 1},
    {ID: ext+'ExtensionVersionID', MIN: 0, MAX: 1},
    {ID: ext+'ExtensionAgencyURI', MIN: 0, MAX: 1},
    {ID: ext+'ExtensionURI', MIN: 0, MAX: 1},
    {ID: ext+'ExtensionReasonCode', MIN: 0, MAX: 1},
    {ID: ext+'ExtensionReason', MIN: 0, MAX: 1},
    {ID: ext+'ExtensionContent', MIN: 1, MAX: 1},
]}

sequences[cac+'Despatch'] = {ID: cac+'Despatch', MIN: 0, MAX: 1, LEVEL: [
    {ID: cbc+'ID', MIN: 0, MAX: 1},
    {ID: cbc+'RequestedDespatchDate', MIN: 0, MAX: 1},
    {ID: cbc+'RequestedDespatchTime', MIN: 0, MAX: 1},
    {ID: cbc+'EstimatedDespatchDate', MIN: 0, MAX: 1},
    {ID: cbc+'EstimatedDespatchTime', MIN: 0, MAX: 1},
    {ID: cbc+'ActualDespatchDate', MIN: 0, MAX: 1},
    {ID: cbc+'ActualDespatchTime', MIN: 0, MAX: 1},
    {ID: cbc+'GuaranteedDespatchDate', MIN: 0, MAX: 1},
    {ID: cbc+'GuaranteedDespatchTime', MIN: 0, MAX: 1},
    {ID: cbc+'ReleaseID', MIN: 0, MAX: 1},
    {ID: cbc+'Instructions', MIN: 0, MAX: 99999},
    {ID: cac+'DespatchAddress', MIN: 0, MAX: 1, LEVEL: [
        {ID: cbc+'ID', MIN: 0, MAX: 1},
        {ID: cbc+'AddressTypeCode', MIN: 0, MAX: 1},
        {ID: cbc+'AddressFormatCode', MIN: 0, MAX: 1},
        {ID: cbc+'Postbox', MIN: 0, MAX: 1},
        {ID: cbc+'Floor', MIN: 0, MAX: 1},
        {ID: cbc+'Room', MIN: 0, MAX: 1},
        {ID: cbc+'StreetName', MIN: 0, MAX: 1},
        {ID: cbc+'AdditionalStreetName', MIN: 0, MAX: 1},
        {ID: cbc+'BlockName', MIN: 0, MAX: 1},
        {ID: cbc+'BuildingName', MIN: 0, MAX: 1},
        {ID: cbc+'BuildingNumber', MIN: 0, MAX: 1},
        {ID: cbc+'InhouseMail', MIN: 0, MAX: 1},
        {ID: cbc+'Department', MIN: 0, MAX: 1},
        {ID: cbc+'MarkAttention', MIN: 0, MAX: 1},
        {ID: cbc+'MarkCare', MIN: 0, MAX: 1},
        {ID: cbc+'PlotIdentification', MIN: 0, MAX: 1},
        {ID: cbc+'CitySubdivisionName', MIN: 0, MAX: 1},
        {ID: cbc+'CityName', MIN: 0, MAX: 1},
        {ID: cbc+'PostalZone', MIN: 0, MAX: 1},
        {ID: cbc+'CountrySubentity', MIN: 0, MAX: 1},
        {ID: cbc+'CountrySubentityCode', MIN: 0, MAX: 1},
        {ID: cbc+'Region', MIN: 0, MAX: 1},
        {ID: cbc+'District', MIN: 0, MAX: 1},
        {ID: cbc+'TimezoneOffset', MIN: 0, MAX: 1},
        {ID: cac+'AddressLine', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'Line', MIN: 1, MAX: 1},
        ]},
        {ID: cac+'Country', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'IdentificationCode', MIN: 0, MAX: 1},
            {ID: cbc+'Name', MIN: 0, MAX: 1},
        ]},
        {ID: cac+'LocationCoordinate', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'CoordinateSystemCode', MIN: 0, MAX: 1},
            {ID: cbc+'LatitudeDegreesMeasure', MIN: 0, MAX: 1},
            {ID: cbc+'LatitudeMinutesMeasure', MIN: 0, MAX: 1},
            {ID: cbc+'LatitudeDirectionCode', MIN: 0, MAX: 1},
            {ID: cbc+'LongitudeDegreesMeasure', MIN: 0, MAX: 1},
            {ID: cbc+'LongitudeMinutesMeasure', MIN: 0, MAX: 1},
            {ID: cbc+'LongitudeDirectionCode', MIN: 0, MAX: 1},
            {ID: cbc+'AltitudeMeasure', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: cac+'DespatchLocation', MIN: 0, MAX: 1, LEVEL: [
        {ID: cbc+'ID', MIN: 0, MAX: 1},
        {ID: cbc+'Description', MIN: 0, MAX: 99999},
        {ID: cbc+'Conditions', MIN: 0, MAX: 99999},
        {ID: cbc+'CountrySubentity', MIN: 0, MAX: 1},
        {ID: cbc+'CountrySubentityCode', MIN: 0, MAX: 1},
        {ID: cbc+'LocationTypeCode', MIN: 0, MAX: 1},
        {ID: cbc+'InformationURI', MIN: 0, MAX: 1},
        {ID: cbc+'Name', MIN: 0, MAX: 1},
        {ID: cac+'ValidityPeriod', MIN: 0, MAX: 99999, LEVEL: sequence(cac+'PeriodType')},
        {ID: cac+'Address', MIN: 0, MAX: 1},
        {ID: cac+'SubsidiaryLocation', MIN: 0, MAX: 99999},
        {ID: cac+'LocationCoordinate', MIN: 0, MAX: 99999, LEVEL: sequence(cac+'LocationCoordinateType')},
    ]},
    {ID: cac+'DespatchParty', MIN: 0, MAX: 1, LEVEL: [
        {ID: cbc+'MarkCareIndicator', MIN: 0, MAX: 1},
        {ID: cbc+'MarkAttentionIndicator', MIN: 0, MAX: 1},
        {ID: cbc+'WebsiteURI', MIN: 0, MAX: 1},
        {ID: cbc+'LogoReferenceID', MIN: 0, MAX: 1},
        {ID: cbc+'EndpointID', MIN: 0, MAX: 1},
        {ID: cbc+'IndustryClassificationCode', MIN: 0, MAX: 1},
        {ID: cac+'PartyIdentification', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 1, MAX: 1},
        ]},
        {ID: cac+'PartyName', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'Name', MIN: 1, MAX: 1},
        ]},
        {ID: cac+'Language', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'Name', MIN: 0, MAX: 1},
            {ID: cbc+'LocaleCode', MIN: 0, MAX: 1},
        ]},
        {ID: cac+'PostalAddress', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'AddressTypeCode', MIN: 0, MAX: 1},
            {ID: cbc+'AddressFormatCode', MIN: 0, MAX: 1},
            {ID: cbc+'Postbox', MIN: 0, MAX: 1},
            {ID: cbc+'Floor', MIN: 0, MAX: 1},
            {ID: cbc+'Room', MIN: 0, MAX: 1},
            {ID: cbc+'StreetName', MIN: 0, MAX: 1},
            {ID: cbc+'AdditionalStreetName', MIN: 0, MAX: 1},
            {ID: cbc+'BlockName', MIN: 0, MAX: 1},
            {ID: cbc+'BuildingName', MIN: 0, MAX: 1},
            {ID: cbc+'BuildingNumber', MIN: 0, MAX: 1},
            {ID: cbc+'InhouseMail', MIN: 0, MAX: 1},
            {ID: cbc+'Department', MIN: 0, MAX: 1},
            {ID: cbc+'MarkAttention', MIN: 0, MAX: 1},
            {ID: cbc+'MarkCare', MIN: 0, MAX: 1},
            {ID: cbc+'PlotIdentification', MIN: 0, MAX: 1},
            {ID: cbc+'CitySubdivisionName', MIN: 0, MAX: 1},
            {ID: cbc+'CityName', MIN: 0, MAX: 1},
            {ID: cbc+'PostalZone', MIN: 0, MAX: 1},
            {ID: cbc+'CountrySubentity', MIN: 0, MAX: 1},
            {ID: cbc+'CountrySubentityCode', MIN: 0, MAX: 1},
            {ID: cbc+'Region', MIN: 0, MAX: 1},
            {ID: cbc+'District', MIN: 0, MAX: 1},
            {ID: cbc+'TimezoneOffset', MIN: 0, MAX: 1},
            {ID: cac+'AddressLine', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'Line', MIN: 1, MAX: 1},
            ]},
            {ID: cac+'Country', MIN: 0, MAX: 1, LEVEL: [
                {ID: cbc+'IdentificationCode', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
            ]},
            {ID: cac+'LocationCoordinate', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'CoordinateSystemCode', MIN: 0, MAX: 1},
                {ID: cbc+'LatitudeDegreesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LatitudeMinutesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LatitudeDirectionCode', MIN: 0, MAX: 1},
                {ID: cbc+'LongitudeDegreesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LongitudeMinutesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LongitudeDirectionCode', MIN: 0, MAX: 1},
                {ID: cbc+'AltitudeMeasure', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: cac+'PhysicalLocation', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'Description', MIN: 0, MAX: 99999},
            {ID: cbc+'Conditions', MIN: 0, MAX: 99999},
            {ID: cbc+'CountrySubentity', MIN: 0, MAX: 1},
            {ID: cbc+'CountrySubentityCode', MIN: 0, MAX: 1},
            {ID: cbc+'LocationTypeCode', MIN: 0, MAX: 1},
            {ID: cbc+'InformationURI', MIN: 0, MAX: 1},
            {ID: cbc+'Name', MIN: 0, MAX: 1},
            {ID: cac+'ValidityPeriod', MIN: 0, MAX: 99999, LEVEL: sequence(cac+'PeriodType')},
            {ID: cac+'Address', MIN: 0, MAX: 1},
            {ID: cac+'SubsidiaryLocation', MIN: 0, MAX: 99999},
            {ID: cac+'LocationCoordinate', MIN: 0, MAX: 99999, LEVEL: sequence(cac+'LocationCoordinateType')},
        ]},
        {ID: cac+'PartyTaxScheme', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'RegistrationName', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyID', MIN: 0, MAX: 1},
            {ID: cbc+'TaxLevelCode', MIN: 0, MAX: 1},
            {ID: cbc+'ExemptionReasonCode', MIN: 0, MAX: 1},
            {ID: cbc+'ExemptionReason', MIN: 0, MAX: 99999},
            {ID: cac+'RegistrationAddress', MIN: 0, MAX: 1},
            {ID: cac+'TaxScheme', MIN: 1, MAX: 1, LEVEL: [
                {ID: cbc+'ID', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
                {ID: cbc+'TaxTypeCode', MIN: 0, MAX: 1},
                {ID: cbc+'CurrencyCode', MIN: 0, MAX: 1},
                {ID: cac+'JurisdictionRegionAddress', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: cac+'PartyLegalEntity', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'RegistrationName', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyID', MIN: 0, MAX: 1},
            {ID: cbc+'RegistrationDate', MIN: 0, MAX: 1},
            {ID: cbc+'RegistrationExpirationDate', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyLegalFormCode', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyLegalForm', MIN: 0, MAX: 1},
            {ID: cbc+'SoleProprietorshipIndicator', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyLiquidationStatusCode', MIN: 0, MAX: 1},
            {ID: cbc+'CorporateStockAmount', MIN: 0, MAX: 1},
            {ID: cbc+'FullyPaidSharesIndicator', MIN: 0, MAX: 1},
            {ID: cac+'RegistrationAddress', MIN: 0, MAX: 1},
            {ID: cac+'CorporateRegistrationScheme', MIN: 0, MAX: 1, LEVEL: [
                {ID: cbc+'ID', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
                {ID: cbc+'CorporateRegistrationTypeCode', MIN: 0, MAX: 1},
                {ID: cac+'JurisdictionRegionAddress', MIN: 0, MAX: 99999},
            ]},
            {ID: cac+'HeadOfficeParty', MIN: 0, MAX: 1},
            {ID: cac+'ShareholderParty', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'PartecipationPercent', MIN: 0, MAX: 1},
                {ID: cac+'Party', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: cac+'Contact', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'Name', MIN: 0, MAX: 1},
            {ID: cbc+'Telephone', MIN: 0, MAX: 1},
            {ID: cbc+'Telefax', MIN: 0, MAX: 1},
            {ID: cbc+'ElectronicMail', MIN: 0, MAX: 1},
            {ID: cbc+'Note', MIN: 0, MAX: 99999},
            {ID: cac+'OtherCommunication', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'ChannelCode', MIN: 0, MAX: 1},
                {ID: cbc+'Channel', MIN: 0, MAX: 1},
                {ID: cbc+'Value', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: cac+'Person', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'FirstName', MIN: 0, MAX: 1},
            {ID: cbc+'FamilyName', MIN: 0, MAX: 1},
            {ID: cbc+'Title', MIN: 0, MAX: 1},
            {ID: cbc+'MiddleName', MIN: 0, MAX: 1},
            {ID: cbc+'OtherName', MIN: 0, MAX: 1},
            {ID: cbc+'NameSuffix', MIN: 0, MAX: 1},
            {ID: cbc+'JobTitle', MIN: 0, MAX: 1},
            {ID: cbc+'NationalityID', MIN: 0, MAX: 1},
            {ID: cbc+'GenderCode', MIN: 0, MAX: 1},
            {ID: cbc+'BirthDate', MIN: 0, MAX: 1},
            {ID: cbc+'BirthplaceName', MIN: 0, MAX: 1},
            {ID: cbc+'OrganizationDepartment', MIN: 0, MAX: 1},
            {ID: cac+'Contact', MIN: 0, MAX: 1},
            {ID: cac+'FinancialAccount', MIN: 0, MAX: 1, LEVEL: [
                {ID: cbc+'ID', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
                {ID: cbc+'AliasName', MIN: 0, MAX: 1},
                {ID: cbc+'AccountTypeCode', MIN: 0, MAX: 1},
                {ID: cbc+'AccountFormatCode', MIN: 0, MAX: 1},
                {ID: cbc+'CurrencyCode', MIN: 0, MAX: 1},
                {ID: cbc+'PaymentNote', MIN: 0, MAX: 99999},
                {ID: cac+'FinancialInstitutionBranch', MIN: 0, MAX: 1, LEVEL: [
                    {ID: cbc+'ID', MIN: 0, MAX: 1},
                    {ID: cbc+'Name', MIN: 0, MAX: 1},
                    {ID: cac+'FinancialInstitution', MIN: 0, MAX: 1, LEVEL: [
                        {ID: cbc+'ID', MIN: 0, MAX: 1},
                        {ID: cbc+'Name', MIN: 0, MAX: 1},
                        {ID: cac+'Address', MIN: 0, MAX: 1},
                    ]},
                    {ID: cac+'Address', MIN: 0, MAX: 1},
                ]},
                {ID: cac+'Country', MIN: 0, MAX: 1, LEVEL: sequence(cac+'CountryType')},
            ]},
            {ID: cac+'IdentityDocumentReference', MIN: 0, MAX: 99999},
            {ID: cac+'ResidenceAddress', MIN: 0, MAX: 1},
        ]},
        {ID: cac+'AgentParty', MIN: 0, MAX: 1},
        {ID: cac+'ServiceProviderParty', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'ServiceTypeCode', MIN: 0, MAX: 1},
            {ID: cbc+'ServiceType', MIN: 0, MAX: 99999},
            {ID: cac+'Party', MIN: 1, MAX: 1},
            {ID: cac+'SellerContact', MIN: 0, MAX: 1},
        ]},
        {ID: cac+'PowerOfAttorney', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'IssueDate', MIN: 0, MAX: 1},
            {ID: cbc+'IssueTime', MIN: 0, MAX: 1},
            {ID: cbc+'Description', MIN: 0, MAX: 99999},
            {ID: cac+'NotaryParty', MIN: 0, MAX: 1},
            {ID: cac+'AgentParty', MIN: 1, MAX: 1},
            {ID: cac+'WitnessParty', MIN: 0, MAX: 99999},
            {ID: cac+'MandateDocumentReference', MIN: 0, MAX: 99999},
        ]},
        {ID: cac+'FinancialAccount', MIN: 0, MAX: 1},
    ]},
    {ID: cac+'CarrierParty', MIN: 0, MAX: 1, LEVEL: [
        {ID: cbc+'MarkCareIndicator', MIN: 0, MAX: 1},
        {ID: cbc+'MarkAttentionIndicator', MIN: 0, MAX: 1},
        {ID: cbc+'WebsiteURI', MIN: 0, MAX: 1},
        {ID: cbc+'LogoReferenceID', MIN: 0, MAX: 1},
        {ID: cbc+'EndpointID', MIN: 0, MAX: 1},
        {ID: cbc+'IndustryClassificationCode', MIN: 0, MAX: 1},
        {ID: cac+'PartyIdentification', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 1, MAX: 1},
        ]},
        {ID: cac+'PartyName', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'Name', MIN: 1, MAX: 1},
        ]},
        {ID: cac+'Language', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'Name', MIN: 0, MAX: 1},
            {ID: cbc+'LocaleCode', MIN: 0, MAX: 1},
        ]},
        {ID: cac+'PostalAddress', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'AddressTypeCode', MIN: 0, MAX: 1},
            {ID: cbc+'AddressFormatCode', MIN: 0, MAX: 1},
            {ID: cbc+'Postbox', MIN: 0, MAX: 1},
            {ID: cbc+'Floor', MIN: 0, MAX: 1},
            {ID: cbc+'Room', MIN: 0, MAX: 1},
            {ID: cbc+'StreetName', MIN: 0, MAX: 1},
            {ID: cbc+'AdditionalStreetName', MIN: 0, MAX: 1},
            {ID: cbc+'BlockName', MIN: 0, MAX: 1},
            {ID: cbc+'BuildingName', MIN: 0, MAX: 1},
            {ID: cbc+'BuildingNumber', MIN: 0, MAX: 1},
            {ID: cbc+'InhouseMail', MIN: 0, MAX: 1},
            {ID: cbc+'Department', MIN: 0, MAX: 1},
            {ID: cbc+'MarkAttention', MIN: 0, MAX: 1},
            {ID: cbc+'MarkCare', MIN: 0, MAX: 1},
            {ID: cbc+'PlotIdentification', MIN: 0, MAX: 1},
            {ID: cbc+'CitySubdivisionName', MIN: 0, MAX: 1},
            {ID: cbc+'CityName', MIN: 0, MAX: 1},
            {ID: cbc+'PostalZone', MIN: 0, MAX: 1},
            {ID: cbc+'CountrySubentity', MIN: 0, MAX: 1},
            {ID: cbc+'CountrySubentityCode', MIN: 0, MAX: 1},
            {ID: cbc+'Region', MIN: 0, MAX: 1},
            {ID: cbc+'District', MIN: 0, MAX: 1},
            {ID: cbc+'TimezoneOffset', MIN: 0, MAX: 1},
            {ID: cac+'AddressLine', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'Line', MIN: 1, MAX: 1},
            ]},
            {ID: cac+'Country', MIN: 0, MAX: 1, LEVEL: [
                {ID: cbc+'IdentificationCode', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
            ]},
            {ID: cac+'LocationCoordinate', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'CoordinateSystemCode', MIN: 0, MAX: 1},
                {ID: cbc+'LatitudeDegreesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LatitudeMinutesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LatitudeDirectionCode', MIN: 0, MAX: 1},
                {ID: cbc+'LongitudeDegreesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LongitudeMinutesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LongitudeDirectionCode', MIN: 0, MAX: 1},
                {ID: cbc+'AltitudeMeasure', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: cac+'PhysicalLocation', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'Description', MIN: 0, MAX: 99999},
            {ID: cbc+'Conditions', MIN: 0, MAX: 99999},
            {ID: cbc+'CountrySubentity', MIN: 0, MAX: 1},
            {ID: cbc+'CountrySubentityCode', MIN: 0, MAX: 1},
            {ID: cbc+'LocationTypeCode', MIN: 0, MAX: 1},
            {ID: cbc+'InformationURI', MIN: 0, MAX: 1},
            {ID: cbc+'Name', MIN: 0, MAX: 1},
            {ID: cac+'ValidityPeriod', MIN: 0, MAX: 99999, LEVEL: sequence(cac+'PeriodType')},
            {ID: cac+'Address', MIN: 0, MAX: 1},
            {ID: cac+'SubsidiaryLocation', MIN: 0, MAX: 99999},
            {ID: cac+'LocationCoordinate', MIN: 0, MAX: 99999, LEVEL: sequence(cac+'LocationCoordinateType')},
        ]},
        {ID: cac+'PartyTaxScheme', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'RegistrationName', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyID', MIN: 0, MAX: 1},
            {ID: cbc+'TaxLevelCode', MIN: 0, MAX: 1},
            {ID: cbc+'ExemptionReasonCode', MIN: 0, MAX: 1},
            {ID: cbc+'ExemptionReason', MIN: 0, MAX: 99999},
            {ID: cac+'RegistrationAddress', MIN: 0, MAX: 1},
            {ID: cac+'TaxScheme', MIN: 1, MAX: 1, LEVEL: [
                {ID: cbc+'ID', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
                {ID: cbc+'TaxTypeCode', MIN: 0, MAX: 1},
                {ID: cbc+'CurrencyCode', MIN: 0, MAX: 1},
                {ID: cac+'JurisdictionRegionAddress', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: cac+'PartyLegalEntity', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'RegistrationName', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyID', MIN: 0, MAX: 1},
            {ID: cbc+'RegistrationDate', MIN: 0, MAX: 1},
            {ID: cbc+'RegistrationExpirationDate', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyLegalFormCode', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyLegalForm', MIN: 0, MAX: 1},
            {ID: cbc+'SoleProprietorshipIndicator', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyLiquidationStatusCode', MIN: 0, MAX: 1},
            {ID: cbc+'CorporateStockAmount', MIN: 0, MAX: 1},
            {ID: cbc+'FullyPaidSharesIndicator', MIN: 0, MAX: 1},
            {ID: cac+'RegistrationAddress', MIN: 0, MAX: 1},
            {ID: cac+'CorporateRegistrationScheme', MIN: 0, MAX: 1, LEVEL: [
                {ID: cbc+'ID', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
                {ID: cbc+'CorporateRegistrationTypeCode', MIN: 0, MAX: 1},
                {ID: cac+'JurisdictionRegionAddress', MIN: 0, MAX: 99999},
            ]},
            {ID: cac+'HeadOfficeParty', MIN: 0, MAX: 1},
            {ID: cac+'ShareholderParty', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'PartecipationPercent', MIN: 0, MAX: 1},
                {ID: cac+'Party', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: cac+'Contact', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'Name', MIN: 0, MAX: 1},
            {ID: cbc+'Telephone', MIN: 0, MAX: 1},
            {ID: cbc+'Telefax', MIN: 0, MAX: 1},
            {ID: cbc+'ElectronicMail', MIN: 0, MAX: 1},
            {ID: cbc+'Note', MIN: 0, MAX: 99999},
            {ID: cac+'OtherCommunication', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'ChannelCode', MIN: 0, MAX: 1},
                {ID: cbc+'Channel', MIN: 0, MAX: 1},
                {ID: cbc+'Value', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: cac+'Person', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'FirstName', MIN: 0, MAX: 1},
            {ID: cbc+'FamilyName', MIN: 0, MAX: 1},
            {ID: cbc+'Title', MIN: 0, MAX: 1},
            {ID: cbc+'MiddleName', MIN: 0, MAX: 1},
            {ID: cbc+'OtherName', MIN: 0, MAX: 1},
            {ID: cbc+'NameSuffix', MIN: 0, MAX: 1},
            {ID: cbc+'JobTitle', MIN: 0, MAX: 1},
            {ID: cbc+'NationalityID', MIN: 0, MAX: 1},
            {ID: cbc+'GenderCode', MIN: 0, MAX: 1},
            {ID: cbc+'BirthDate', MIN: 0, MAX: 1},
            {ID: cbc+'BirthplaceName', MIN: 0, MAX: 1},
            {ID: cbc+'OrganizationDepartment', MIN: 0, MAX: 1},
            {ID: cac+'Contact', MIN: 0, MAX: 1},
            {ID: cac+'FinancialAccount', MIN: 0, MAX: 1, LEVEL: [
                {ID: cbc+'ID', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
                {ID: cbc+'AliasName', MIN: 0, MAX: 1},
                {ID: cbc+'AccountTypeCode', MIN: 0, MAX: 1},
                {ID: cbc+'AccountFormatCode', MIN: 0, MAX: 1},
                {ID: cbc+'CurrencyCode', MIN: 0, MAX: 1},
                {ID: cbc+'PaymentNote', MIN: 0, MAX: 99999},
                {ID: cac+'FinancialInstitutionBranch', MIN: 0, MAX: 1, LEVEL: [
                    {ID: cbc+'ID', MIN: 0, MAX: 1},
                    {ID: cbc+'Name', MIN: 0, MAX: 1},
                    {ID: cac+'FinancialInstitution', MIN: 0, MAX: 1, LEVEL: [
                        {ID: cbc+'ID', MIN: 0, MAX: 1},
                        {ID: cbc+'Name', MIN: 0, MAX: 1},
                        {ID: cac+'Address', MIN: 0, MAX: 1},
                    ]},
                    {ID: cac+'Address', MIN: 0, MAX: 1},
                ]},
                {ID: cac+'Country', MIN: 0, MAX: 1, LEVEL: sequence(cac+'CountryType')},
            ]},
            {ID: cac+'IdentityDocumentReference', MIN: 0, MAX: 99999},
            {ID: cac+'ResidenceAddress', MIN: 0, MAX: 1},
        ]},
        {ID: cac+'AgentParty', MIN: 0, MAX: 1},
        {ID: cac+'ServiceProviderParty', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'ServiceTypeCode', MIN: 0, MAX: 1},
            {ID: cbc+'ServiceType', MIN: 0, MAX: 99999},
            {ID: cac+'Party', MIN: 1, MAX: 1},
            {ID: cac+'SellerContact', MIN: 0, MAX: 1},
        ]},
        {ID: cac+'PowerOfAttorney', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'IssueDate', MIN: 0, MAX: 1},
            {ID: cbc+'IssueTime', MIN: 0, MAX: 1},
            {ID: cbc+'Description', MIN: 0, MAX: 99999},
            {ID: cac+'NotaryParty', MIN: 0, MAX: 1},
            {ID: cac+'AgentParty', MIN: 1, MAX: 1},
            {ID: cac+'WitnessParty', MIN: 0, MAX: 99999},
            {ID: cac+'MandateDocumentReference', MIN: 0, MAX: 99999},
        ]},
        {ID: cac+'FinancialAccount', MIN: 0, MAX: 1},
    ]},
    {ID: cac+'NotifyParty', MIN: 0, MAX: 99999, LEVEL: [
        {ID: cbc+'MarkCareIndicator', MIN: 0, MAX: 1},
        {ID: cbc+'MarkAttentionIndicator', MIN: 0, MAX: 1},
        {ID: cbc+'WebsiteURI', MIN: 0, MAX: 1},
        {ID: cbc+'LogoReferenceID', MIN: 0, MAX: 1},
        {ID: cbc+'EndpointID', MIN: 0, MAX: 1},
        {ID: cbc+'IndustryClassificationCode', MIN: 0, MAX: 1},
        {ID: cac+'PartyIdentification', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 1, MAX: 1},
        ]},
        {ID: cac+'PartyName', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'Name', MIN: 1, MAX: 1},
        ]},
        {ID: cac+'Language', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'Name', MIN: 0, MAX: 1},
            {ID: cbc+'LocaleCode', MIN: 0, MAX: 1},
        ]},
        {ID: cac+'PostalAddress', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'AddressTypeCode', MIN: 0, MAX: 1},
            {ID: cbc+'AddressFormatCode', MIN: 0, MAX: 1},
            {ID: cbc+'Postbox', MIN: 0, MAX: 1},
            {ID: cbc+'Floor', MIN: 0, MAX: 1},
            {ID: cbc+'Room', MIN: 0, MAX: 1},
            {ID: cbc+'StreetName', MIN: 0, MAX: 1},
            {ID: cbc+'AdditionalStreetName', MIN: 0, MAX: 1},
            {ID: cbc+'BlockName', MIN: 0, MAX: 1},
            {ID: cbc+'BuildingName', MIN: 0, MAX: 1},
            {ID: cbc+'BuildingNumber', MIN: 0, MAX: 1},
            {ID: cbc+'InhouseMail', MIN: 0, MAX: 1},
            {ID: cbc+'Department', MIN: 0, MAX: 1},
            {ID: cbc+'MarkAttention', MIN: 0, MAX: 1},
            {ID: cbc+'MarkCare', MIN: 0, MAX: 1},
            {ID: cbc+'PlotIdentification', MIN: 0, MAX: 1},
            {ID: cbc+'CitySubdivisionName', MIN: 0, MAX: 1},
            {ID: cbc+'CityName', MIN: 0, MAX: 1},
            {ID: cbc+'PostalZone', MIN: 0, MAX: 1},
            {ID: cbc+'CountrySubentity', MIN: 0, MAX: 1},
            {ID: cbc+'CountrySubentityCode', MIN: 0, MAX: 1},
            {ID: cbc+'Region', MIN: 0, MAX: 1},
            {ID: cbc+'District', MIN: 0, MAX: 1},
            {ID: cbc+'TimezoneOffset', MIN: 0, MAX: 1},
            {ID: cac+'AddressLine', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'Line', MIN: 1, MAX: 1},
            ]},
            {ID: cac+'Country', MIN: 0, MAX: 1, LEVEL: [
                {ID: cbc+'IdentificationCode', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
            ]},
            {ID: cac+'LocationCoordinate', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'CoordinateSystemCode', MIN: 0, MAX: 1},
                {ID: cbc+'LatitudeDegreesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LatitudeMinutesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LatitudeDirectionCode', MIN: 0, MAX: 1},
                {ID: cbc+'LongitudeDegreesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LongitudeMinutesMeasure', MIN: 0, MAX: 1},
                {ID: cbc+'LongitudeDirectionCode', MIN: 0, MAX: 1},
                {ID: cbc+'AltitudeMeasure', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: cac+'PhysicalLocation', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'Description', MIN: 0, MAX: 99999},
            {ID: cbc+'Conditions', MIN: 0, MAX: 99999},
            {ID: cbc+'CountrySubentity', MIN: 0, MAX: 1},
            {ID: cbc+'CountrySubentityCode', MIN: 0, MAX: 1},
            {ID: cbc+'LocationTypeCode', MIN: 0, MAX: 1},
            {ID: cbc+'InformationURI', MIN: 0, MAX: 1},
            {ID: cbc+'Name', MIN: 0, MAX: 1},
            {ID: cac+'ValidityPeriod', MIN: 0, MAX: 99999, LEVEL: sequence(cac+'PeriodType')},
            {ID: cac+'Address', MIN: 0, MAX: 1},
            {ID: cac+'SubsidiaryLocation', MIN: 0, MAX: 99999},
            {ID: cac+'LocationCoordinate', MIN: 0, MAX: 99999, LEVEL: sequence(cac+'LocationCoordinateType')},
        ]},
        {ID: cac+'PartyTaxScheme', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'RegistrationName', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyID', MIN: 0, MAX: 1},
            {ID: cbc+'TaxLevelCode', MIN: 0, MAX: 1},
            {ID: cbc+'ExemptionReasonCode', MIN: 0, MAX: 1},
            {ID: cbc+'ExemptionReason', MIN: 0, MAX: 99999},
            {ID: cac+'RegistrationAddress', MIN: 0, MAX: 1},
            {ID: cac+'TaxScheme', MIN: 1, MAX: 1, LEVEL: [
                {ID: cbc+'ID', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
                {ID: cbc+'TaxTypeCode', MIN: 0, MAX: 1},
                {ID: cbc+'CurrencyCode', MIN: 0, MAX: 1},
                {ID: cac+'JurisdictionRegionAddress', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: cac+'PartyLegalEntity', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'RegistrationName', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyID', MIN: 0, MAX: 1},
            {ID: cbc+'RegistrationDate', MIN: 0, MAX: 1},
            {ID: cbc+'RegistrationExpirationDate', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyLegalFormCode', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyLegalForm', MIN: 0, MAX: 1},
            {ID: cbc+'SoleProprietorshipIndicator', MIN: 0, MAX: 1},
            {ID: cbc+'CompanyLiquidationStatusCode', MIN: 0, MAX: 1},
            {ID: cbc+'CorporateStockAmount', MIN: 0, MAX: 1},
            {ID: cbc+'FullyPaidSharesIndicator', MIN: 0, MAX: 1},
            {ID: cac+'RegistrationAddress', MIN: 0, MAX: 1},
            {ID: cac+'CorporateRegistrationScheme', MIN: 0, MAX: 1, LEVEL: [
                {ID: cbc+'ID', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
                {ID: cbc+'CorporateRegistrationTypeCode', MIN: 0, MAX: 1},
                {ID: cac+'JurisdictionRegionAddress', MIN: 0, MAX: 99999},
            ]},
            {ID: cac+'HeadOfficeParty', MIN: 0, MAX: 1},
            {ID: cac+'ShareholderParty', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'PartecipationPercent', MIN: 0, MAX: 1},
                {ID: cac+'Party', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: cac+'Contact', MIN: 0, MAX: 1, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'Name', MIN: 0, MAX: 1},
            {ID: cbc+'Telephone', MIN: 0, MAX: 1},
            {ID: cbc+'Telefax', MIN: 0, MAX: 1},
            {ID: cbc+'ElectronicMail', MIN: 0, MAX: 1},
            {ID: cbc+'Note', MIN: 0, MAX: 99999},
            {ID: cac+'OtherCommunication', MIN: 0, MAX: 99999, LEVEL: [
                {ID: cbc+'ChannelCode', MIN: 0, MAX: 1},
                {ID: cbc+'Channel', MIN: 0, MAX: 1},
                {ID: cbc+'Value', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: cac+'Person', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'FirstName', MIN: 0, MAX: 1},
            {ID: cbc+'FamilyName', MIN: 0, MAX: 1},
            {ID: cbc+'Title', MIN: 0, MAX: 1},
            {ID: cbc+'MiddleName', MIN: 0, MAX: 1},
            {ID: cbc+'OtherName', MIN: 0, MAX: 1},
            {ID: cbc+'NameSuffix', MIN: 0, MAX: 1},
            {ID: cbc+'JobTitle', MIN: 0, MAX: 1},
            {ID: cbc+'NationalityID', MIN: 0, MAX: 1},
            {ID: cbc+'GenderCode', MIN: 0, MAX: 1},
            {ID: cbc+'BirthDate', MIN: 0, MAX: 1},
            {ID: cbc+'BirthplaceName', MIN: 0, MAX: 1},
            {ID: cbc+'OrganizationDepartment', MIN: 0, MAX: 1},
            {ID: cac+'Contact', MIN: 0, MAX: 1},
            {ID: cac+'FinancialAccount', MIN: 0, MAX: 1, LEVEL: [
                {ID: cbc+'ID', MIN: 0, MAX: 1},
                {ID: cbc+'Name', MIN: 0, MAX: 1},
                {ID: cbc+'AliasName', MIN: 0, MAX: 1},
                {ID: cbc+'AccountTypeCode', MIN: 0, MAX: 1},
                {ID: cbc+'AccountFormatCode', MIN: 0, MAX: 1},
                {ID: cbc+'CurrencyCode', MIN: 0, MAX: 1},
                {ID: cbc+'PaymentNote', MIN: 0, MAX: 99999},
                {ID: cac+'FinancialInstitutionBranch', MIN: 0, MAX: 1, LEVEL: [
                    {ID: cbc+'ID', MIN: 0, MAX: 1},
                    {ID: cbc+'Name', MIN: 0, MAX: 1},
                    {ID: cac+'FinancialInstitution', MIN: 0, MAX: 1, LEVEL: [
                        {ID: cbc+'ID', MIN: 0, MAX: 1},
                        {ID: cbc+'Name', MIN: 0, MAX: 1},
                        {ID: cac+'Address', MIN: 0, MAX: 1},
                    ]},
                    {ID: cac+'Address', MIN: 0, MAX: 1},
                ]},
                {ID: cac+'Country', MIN: 0, MAX: 1, LEVEL: sequence(cac+'CountryType')},
            ]},
            {ID: cac+'IdentityDocumentReference', MIN: 0, MAX: 99999},
            {ID: cac+'ResidenceAddress', MIN: 0, MAX: 1},
        ]},
        {ID: cac+'AgentParty', MIN: 0, MAX: 1},
        {ID: cac+'ServiceProviderParty', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'ServiceTypeCode', MIN: 0, MAX: 1},
            {ID: cbc+'ServiceType', MIN: 0, MAX: 99999},
            {ID: cac+'Party', MIN: 1, MAX: 1},
            {ID: cac+'SellerContact', MIN: 0, MAX: 1},
        ]},
        {ID: cac+'PowerOfAttorney', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ID', MIN: 0, MAX: 1},
            {ID: cbc+'IssueDate', MIN: 0, MAX: 1},
            {ID: cbc+'IssueTime', MIN: 0, MAX: 1},
            {ID: cbc+'Description', MIN: 0, MAX: 99999},
            {ID: cac+'NotaryParty', MIN: 0, MAX: 1},
            {ID: cac+'AgentParty', MIN: 1, MAX: 1},
            {ID: cac+'WitnessParty', MIN: 0, MAX: 99999},
            {ID: cac+'MandateDocumentReference', MIN: 0, MAX: 99999},
        ]},
        {ID: cac+'FinancialAccount', MIN: 0, MAX: 1},
    ]},
    {ID: cac+'Contact', MIN: 0, MAX: 1, LEVEL: [
        {ID: cbc+'ID', MIN: 0, MAX: 1},
        {ID: cbc+'Name', MIN: 0, MAX: 1},
        {ID: cbc+'Telephone', MIN: 0, MAX: 1},
        {ID: cbc+'Telefax', MIN: 0, MAX: 1},
        {ID: cbc+'ElectronicMail', MIN: 0, MAX: 1},
        {ID: cbc+'Note', MIN: 0, MAX: 99999},
        {ID: cac+'OtherCommunication', MIN: 0, MAX: 99999, LEVEL: [
            {ID: cbc+'ChannelCode', MIN: 0, MAX: 1},
            {ID: cbc+'Channel', MIN: 0, MAX: 1},
            {ID: cbc+'Value', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: cac+'EstimatedDespatchPeriod', MIN: 0, MAX: 1, LEVEL: sequence(cac+'PeriodType')},
    {ID: cac+'RequestedDespatchPeriod', MIN: 0, MAX: 1, LEVEL: sequence(cac+'PeriodType')},
]}
