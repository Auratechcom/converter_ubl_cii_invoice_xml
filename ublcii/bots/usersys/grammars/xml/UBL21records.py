# -*- coding: utf-8 -*-

version = '2.1'

xmlns = '{urn:oasis:names:specification:ubl:schema:xsd:Invoice-2}'
ext = '{urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}'
cbc = '{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}'
cac = '{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}'
ccts = '{urn:un:unece:uncefact:documentation:2}'


recorddefs = {
cac+'AcceptanceTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AccountingContact':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AccountingCustomerParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AccountingSupplierParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ActualArrivalTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ActualDepartureTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ActualPackage':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ActualPickupTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ActualWaypointTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AdditionalDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AdditionalItemIdentification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AdditionalItemProperty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AdditionalTemperature':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Address':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AddressLine':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AgentParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AirTransport':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AllowanceCharge':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AlternativeConditionPrice':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AlternativeDeliveryLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ApplicableAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ApplicableTaxCategory':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ApplicableTerritoryAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ApplicableTransportMeans':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AttachedTransportEquipment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Attachment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'AvailabilityTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'BillOfLadingHolderParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'BillingReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'BillingReferenceLine':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'BuyerContact':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'BuyerCustomerParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'BuyersItemIdentification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CardAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CarrierParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CatalogueDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CatalogueItemIdentification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Certificate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ChildConsignment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ClassifiedTaxCategory':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Clause':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CollectPaymentTerms':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CommodityClassification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Condition':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ConsigneeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Consignment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ConsignorParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ConsolidatedShipment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Contact':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ContactParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ContainedGoodsItem':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ContainedInTransportEquipment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ContainedPackage':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ContainingPackage':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ContainingTransportEquipment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ContractDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ContractualDelivery':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CorporateRegistrationScheme':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Country':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CreditAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CreditNoteDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CrewMemberPerson':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CurrentStatus':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CustomsAgentParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'CustomsDeclaration':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DebitNoteDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Delivery':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DeliveryAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DeliveryContact':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DeliveryLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DeliveryParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DeliveryTerms':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DeliveryTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DeliveryUnit':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DependentLineReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DependentPriceReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Despatch':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DespatchAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DespatchContact':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DespatchDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DespatchLineReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DespatchLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DespatchParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DetentionTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DigitalSignatureAttachment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Dimension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DisbursementPaymentTerms':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DischargeTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DriverPerson':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'DropoffTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'EmergencyTemperature':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'EmissionCalculationMethod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'EnvironmentalEmission':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'EstimatedArrivalTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'EstimatedDeliveryPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'EstimatedDepartureTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'EstimatedDespatchPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'EstimatedDurationPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'EstimatedTransitPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ExaminationTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ExchangeRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ExportCountry':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ExportationTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ExporterParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ExternalReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ExtraAllowanceCharge':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FinalDeliveryParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FinalDeliveryTransportationService':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FinalDestinationCountry':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FinancialAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FinancialInstitution':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FinancialInstitutionBranch':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FinancingFinancialAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FinancingParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FirstArrivalPortLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FlashpointTemperature':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FloorSpaceMeasurementDimension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ForeignExchangeContract':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FreightAllowanceCharge':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FreightChargeLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'FreightForwarderParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'GoodsItem':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'GoodsItemContainer':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'HandlingTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'HandlingUnitDespatchLine':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'HaulageTradingTerms':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'HazardousGoodsTransit':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'HazardousItem':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'HazardousItemNotificationParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'HeadOfficeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'IdentityDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ImporterParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'InformationContentProviderParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'InsuranceParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'InvoiceDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'InvoiceLine':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'InvoicePeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'IssuerParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Item':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ItemInstance':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ItemPriceExtension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ItemPropertyGroup':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ItemPropertyRange':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ItemSpecificationDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'JurisdictionRegionAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Language':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'LastExitPortLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'LegalMonetaryTotal':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'LoadingLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'LoadingPortLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'LoadingProofParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'LoadingTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Location':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'LocationAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'LocationCoordinate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'LogisticsOperatorParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'LotIdentification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MainCarriageShipmentStage':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MandateDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ManufacturerParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ManufacturersItemIdentification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MaritimeTransport':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MasterPerson':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MaximumDeliveryUnit':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MaximumTemperature':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MeasurementDimension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MeasurementFromLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MeasurementToLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MinimumDeliveryUnit':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MinimumTemperature':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'MortgageHolderParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'NominationPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'NotaryParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'NotifyParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OnCarriageShipmentStage':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OperatingParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OptionalTakeoverTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OrderLineReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OrderReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OriginAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OriginCountry':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OriginalDepartureCountry':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OriginalDespatchParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OriginalDespatchTransportationService':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OriginalDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OriginalItemLocationQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OriginatorDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OriginatorParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OtherCommunication':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'OwnerParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Package':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PackagedTransportHandlingUnit':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PalletSpaceMeasurementDimension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Party':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PartyIdentification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PartyLegalEntity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PartyName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PartyTaxScheme':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PassengerPerson':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PayeeFinancialAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PayeeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PayerFinancialAccount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PayerParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PaymentAlternativeExchangeRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PaymentExchangeRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PaymentMandate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PaymentMeans':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PaymentReversalPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PaymentTerms':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PenaltyPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PerformingCarrierParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Period':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Person':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PhysicalAttribute':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PhysicalLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Pickup':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PickupLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PickupParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PickupTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PlannedArrivalTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PlannedDeliveryTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PlannedDepartureTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PlannedPickupTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PlannedWaypointTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PositioningTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PostalAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PowerOfAttorney':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PreCarriageShipmentStage':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PrepaidPayment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PrepaidPaymentTerms':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PreviousPriceList':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Price':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PriceList':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PricingExchangeRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PricingReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ProjectReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'PromisedDeliveryPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ProviderParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'QuarantineTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RailTransport':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RangeDimension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ReceiptDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ReceiptLineReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ReceiptTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ReceivedHandlingUnitReceiptLine':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ReferencedShipment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RegistrationAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RegistryCertificateDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RegistryPortLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ReminderDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ReportedShipment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ReportingPerson':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RequestedArrivalTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RequestedDeliveryPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RequestedDeliveryTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RequestedDepartureTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RequestedDespatchPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RequestedPickupTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RequestedWaypointTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ResidenceAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ResponsibleTransportServiceProviderParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ResultOfVerification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ReturnAddress':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'RoadTransport':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ScheduledServiceFrequency':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SecondaryHazard':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SecurityOfficerPerson':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SelfBilledCreditNoteDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SelfBilledInvoiceDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SellerContact':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SellerSupplierParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SellersItemIdentification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ServiceAllowanceCharge':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ServiceProviderParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SettlementPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ShareholderParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Shipment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ShipmentDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ShipmentStage':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ShipsSurgeonPerson':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SignatoryParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Signature':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'StandardItemIdentification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'StatementDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Status':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'StorageLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'StorageTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Stowage':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SubInvoiceLine':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SubsidiaryLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SubstituteCarrierParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SupplierParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SupportedCommodityClassification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'SupportedTransportEquipment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TakeoverTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TaxCategory':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TaxExchangeRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TaxRepresentativeParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TaxScheme':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TaxSubtotal':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TaxTotal':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'Temperature':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TerminalOperatorParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TotalCapacityDimension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TradeFinancing':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TransactionConditions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TransitCountry':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TransitPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TransportAdvisorParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TransportContract':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TransportEquipment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TransportEquipmentSeal':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TransportHandlingUnit':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TransportMeans':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'TransshipPortLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'UnloadingLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'UnloadingPortLocation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'UnsupportedCommodityClassification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'UnsupportedTransportEquipment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'UsabilityPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'ValidityPeriod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'WarehousingTransportEvent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'WithholdingTaxTotal':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'WitnessParty':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'WorkOrderDocumentReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cac+'WorkPhaseReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
cbc+'AccountFormatCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AccountFormatCode__listName', 'C', 256, 'AN'],
    [cbc+'AccountFormatCode__name', 'C', 256, 'AN'],
    [cbc+'AccountFormatCode__languageID', 'C', 256, 'AN'],
    [cbc+'AccountFormatCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'AccountFormatCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'AccountFormatCode__listID', 'C', 256, 'AN'],
    [cbc+'AccountFormatCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'AccountFormatCode__listURI', 'C', 256, 'AN'],
    [cbc+'AccountFormatCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'AccountID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AccountID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'AccountID__schemeID', 'C', 256, 'AN'],
    [cbc+'AccountID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'AccountID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'AccountID__schemeName', 'C', 256, 'AN'],
    [cbc+'AccountID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'AccountID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'AccountTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AccountTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'AccountTypeCode__name', 'C', 256, 'AN'],
    [cbc+'AccountTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'AccountTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'AccountTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'AccountTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'AccountTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'AccountTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'AccountTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'AccountingCost':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AccountingCost__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'AccountingCost__languageID', 'C', 256, 'AN'],
    ],
cbc+'AccountingCostCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AccountingCostCode__listName', 'C', 256, 'AN'],
    [cbc+'AccountingCostCode__name', 'C', 256, 'AN'],
    [cbc+'AccountingCostCode__languageID', 'C', 256, 'AN'],
    [cbc+'AccountingCostCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'AccountingCostCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'AccountingCostCode__listID', 'C', 256, 'AN'],
    [cbc+'AccountingCostCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'AccountingCostCode__listURI', 'C', 256, 'AN'],
    [cbc+'AccountingCostCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'ActionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ActionCode__listName', 'C', 256, 'AN'],
    [cbc+'ActionCode__name', 'C', 256, 'AN'],
    [cbc+'ActionCode__languageID', 'C', 256, 'AN'],
    [cbc+'ActionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ActionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ActionCode__listID', 'C', 256, 'AN'],
    [cbc+'ActionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ActionCode__listURI', 'C', 256, 'AN'],
    [cbc+'ActionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'ActualDeliveryDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ActualDeliveryTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'ActualDespatchDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ActualDespatchTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'ActualPickupDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ActualPickupTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'AdditionalAccountID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AdditionalAccountID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'AdditionalAccountID__schemeID', 'C', 256, 'AN'],
    [cbc+'AdditionalAccountID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'AdditionalAccountID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'AdditionalAccountID__schemeName', 'C', 256, 'AN'],
    [cbc+'AdditionalAccountID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'AdditionalAccountID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'AdditionalInformation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AdditionalInformation__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'AdditionalInformation__languageID', 'C', 256, 'AN'],
    ],
cbc+'AdditionalStreetName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AdditionalStreetName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'AdditionalStreetName__languageID', 'C', 256, 'AN'],
    ],
cbc+'AddressFormatCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AddressFormatCode__listName', 'C', 256, 'AN'],
    [cbc+'AddressFormatCode__name', 'C', 256, 'AN'],
    [cbc+'AddressFormatCode__languageID', 'C', 256, 'AN'],
    [cbc+'AddressFormatCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'AddressFormatCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'AddressFormatCode__listID', 'C', 256, 'AN'],
    [cbc+'AddressFormatCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'AddressFormatCode__listURI', 'C', 256, 'AN'],
    [cbc+'AddressFormatCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'AddressTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AddressTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'AddressTypeCode__name', 'C', 256, 'AN'],
    [cbc+'AddressTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'AddressTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'AddressTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'AddressTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'AddressTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'AddressTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'AddressTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'AirFlowPercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'AirFlowPercent__format', 'C', 256, 'AN'],
    ],
cbc+'AircraftID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AircraftID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'AircraftID__schemeID', 'C', 256, 'AN'],
    [cbc+'AircraftID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'AircraftID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'AircraftID__schemeName', 'C', 256, 'AN'],
    [cbc+'AircraftID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'AircraftID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'AliasName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AliasName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'AliasName__languageID', 'C', 256, 'AN'],
    ],
cbc+'AllowanceChargeReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AllowanceChargeReason__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'AllowanceChargeReason__languageID', 'C', 256, 'AN'],
    ],
cbc+'AllowanceChargeReasonCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AllowanceChargeReasonCode__listName', 'C', 256, 'AN'],
    [cbc+'AllowanceChargeReasonCode__name', 'C', 256, 'AN'],
    [cbc+'AllowanceChargeReasonCode__languageID', 'C', 256, 'AN'],
    [cbc+'AllowanceChargeReasonCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'AllowanceChargeReasonCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'AllowanceChargeReasonCode__listID', 'C', 256, 'AN'],
    [cbc+'AllowanceChargeReasonCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'AllowanceChargeReasonCode__listURI', 'C', 256, 'AN'],
    [cbc+'AllowanceChargeReasonCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'AllowanceTotalAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AllowanceTotalAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'AllowanceTotalAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'AltitudeMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AltitudeMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'AltitudeMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'Amount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Amount__currencyID', 'C', 256, 'AN'],
    [cbc+'Amount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'AnimalFoodApprovedIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'AnimalFoodIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'AttributeID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'AttributeID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'AttributeID__schemeID', 'C', 256, 'AN'],
    [cbc+'AttributeID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'AttributeID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'AttributeID__schemeName', 'C', 256, 'AN'],
    [cbc+'AttributeID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'AttributeID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'BackorderQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'BackorderQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'BackorderQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'BackorderQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'BackorderQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'BackorderReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'BackorderReason__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'BackorderReason__languageID', 'C', 256, 'AN'],
    ],
cbc+'BarcodeSymbologyID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'BarcodeSymbologyID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'BarcodeSymbologyID__schemeID', 'C', 256, 'AN'],
    [cbc+'BarcodeSymbologyID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'BarcodeSymbologyID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'BarcodeSymbologyID__schemeName', 'C', 256, 'AN'],
    [cbc+'BarcodeSymbologyID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'BarcodeSymbologyID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'BaseAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'BaseAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'BaseAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'BaseQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'BaseQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'BaseQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'BaseQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'BaseQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'BaseUnitMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'BaseUnitMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'BaseUnitMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'BatchQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'BatchQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'BatchQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'BatchQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'BatchQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'BestBeforeDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'BirthDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'BirthplaceName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'BirthplaceName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'BirthplaceName__languageID', 'C', 256, 'AN'],
    ],
cbc+'BlockName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'BlockName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'BlockName__languageID', 'C', 256, 'AN'],
    ],
cbc+'BrandName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'BrandName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'BrandName__languageID', 'C', 256, 'AN'],
    ],
cbc+'BrokerAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'BrokerAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'BrokerAssignedID__schemeID', 'C', 256, 'AN'],
    [cbc+'BrokerAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'BrokerAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'BrokerAssignedID__schemeName', 'C', 256, 'AN'],
    [cbc+'BrokerAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'BrokerAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'BuildingName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'BuildingName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'BuildingName__languageID', 'C', 256, 'AN'],
    ],
cbc+'BuildingNumber':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'BuildingNumber__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'BuildingNumber__languageID', 'C', 256, 'AN'],
    ],
cbc+'BulkCargoIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'BuyerReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'BuyerReference__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'BuyerReference__languageID', 'C', 256, 'AN'],
    ],
cbc+'CV2ID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CV2ID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'CV2ID__schemeID', 'C', 256, 'AN'],
    [cbc+'CV2ID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'CV2ID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'CV2ID__schemeName', 'C', 256, 'AN'],
    [cbc+'CV2ID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'CV2ID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'CalculationMethodCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CalculationMethodCode__listName', 'C', 256, 'AN'],
    [cbc+'CalculationMethodCode__name', 'C', 256, 'AN'],
    [cbc+'CalculationMethodCode__languageID', 'C', 256, 'AN'],
    [cbc+'CalculationMethodCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CalculationMethodCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CalculationMethodCode__listID', 'C', 256, 'AN'],
    [cbc+'CalculationMethodCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CalculationMethodCode__listURI', 'C', 256, 'AN'],
    [cbc+'CalculationMethodCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CalculationRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'CalculationRate__format', 'C', 256, 'AN'],
    ],
cbc+'CalculationSequenceNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'CalculationSequenceNumeric__format', 'C', 256, 'AN'],
    ],
cbc+'CanonicalizationMethod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CanonicalizationMethod__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'CanonicalizationMethod__languageID', 'C', 256, 'AN'],
    ],
cbc+'CardChipCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CardChipCode__listName', 'C', 256, 'AN'],
    [cbc+'CardChipCode__name', 'C', 256, 'AN'],
    [cbc+'CardChipCode__languageID', 'C', 256, 'AN'],
    [cbc+'CardChipCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CardChipCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CardChipCode__listID', 'C', 256, 'AN'],
    [cbc+'CardChipCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CardChipCode__listURI', 'C', 256, 'AN'],
    [cbc+'CardChipCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CardTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CardTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'CardTypeCode__name', 'C', 256, 'AN'],
    [cbc+'CardTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'CardTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CardTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CardTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'CardTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CardTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'CardTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CargoTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CargoTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'CargoTypeCode__name', 'C', 256, 'AN'],
    [cbc+'CargoTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'CargoTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CargoTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CargoTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'CargoTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CargoTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'CargoTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CarrierAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CarrierAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'CarrierAssignedID__schemeID', 'C', 256, 'AN'],
    [cbc+'CarrierAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'CarrierAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'CarrierAssignedID__schemeName', 'C', 256, 'AN'],
    [cbc+'CarrierAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'CarrierAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'CarrierServiceInstructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CarrierServiceInstructions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'CarrierServiceInstructions__languageID', 'C', 256, 'AN'],
    ],
cbc+'CatalogueIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'CategoryName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CategoryName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'CategoryName__languageID', 'C', 256, 'AN'],
    ],
cbc+'CertificateType':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CertificateType__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'CertificateType__languageID', 'C', 256, 'AN'],
    ],
cbc+'CertificateTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CertificateTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'CertificateTypeCode__name', 'C', 256, 'AN'],
    [cbc+'CertificateTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'CertificateTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CertificateTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CertificateTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'CertificateTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CertificateTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'CertificateTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'Channel':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Channel__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Channel__languageID', 'C', 256, 'AN'],
    ],
cbc+'ChannelCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ChannelCode__listName', 'C', 256, 'AN'],
    [cbc+'ChannelCode__name', 'C', 256, 'AN'],
    [cbc+'ChannelCode__languageID', 'C', 256, 'AN'],
    [cbc+'ChannelCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ChannelCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ChannelCode__listID', 'C', 256, 'AN'],
    [cbc+'ChannelCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ChannelCode__listURI', 'C', 256, 'AN'],
    [cbc+'ChannelCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CharacterSetCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CharacterSetCode__listName', 'C', 256, 'AN'],
    [cbc+'CharacterSetCode__name', 'C', 256, 'AN'],
    [cbc+'CharacterSetCode__languageID', 'C', 256, 'AN'],
    [cbc+'CharacterSetCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CharacterSetCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CharacterSetCode__listID', 'C', 256, 'AN'],
    [cbc+'CharacterSetCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CharacterSetCode__listURI', 'C', 256, 'AN'],
    [cbc+'CharacterSetCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'Characteristics':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Characteristics__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Characteristics__languageID', 'C', 256, 'AN'],
    ],
cbc+'ChargeIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ChargeTotalAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ChargeTotalAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'ChargeTotalAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'ChargeableQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'ChargeableQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'ChargeableQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'ChargeableQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'ChargeableQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'ChargeableWeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ChargeableWeightMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'ChargeableWeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'ChildConsignmentQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'ChildConsignmentQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'ChildConsignmentQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'ChildConsignmentQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'ChildConsignmentQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'ChipApplicationID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ChipApplicationID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ChipApplicationID__schemeID', 'C', 256, 'AN'],
    [cbc+'ChipApplicationID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ChipApplicationID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ChipApplicationID__schemeName', 'C', 256, 'AN'],
    [cbc+'ChipApplicationID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ChipApplicationID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'CityName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CityName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'CityName__languageID', 'C', 256, 'AN'],
    ],
cbc+'CitySubdivisionName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CitySubdivisionName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'CitySubdivisionName__languageID', 'C', 256, 'AN'],
    ],
cbc+'CommodityCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CommodityCode__listName', 'C', 256, 'AN'],
    [cbc+'CommodityCode__name', 'C', 256, 'AN'],
    [cbc+'CommodityCode__languageID', 'C', 256, 'AN'],
    [cbc+'CommodityCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CommodityCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CommodityCode__listID', 'C', 256, 'AN'],
    [cbc+'CommodityCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CommodityCode__listURI', 'C', 256, 'AN'],
    [cbc+'CommodityCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CompanyID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CompanyID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'CompanyID__schemeID', 'C', 256, 'AN'],
    [cbc+'CompanyID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'CompanyID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'CompanyID__schemeName', 'C', 256, 'AN'],
    [cbc+'CompanyID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'CompanyID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'CompanyLegalForm':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CompanyLegalForm__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'CompanyLegalForm__languageID', 'C', 256, 'AN'],
    ],
cbc+'CompanyLegalFormCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CompanyLegalFormCode__listName', 'C', 256, 'AN'],
    [cbc+'CompanyLegalFormCode__name', 'C', 256, 'AN'],
    [cbc+'CompanyLegalFormCode__languageID', 'C', 256, 'AN'],
    [cbc+'CompanyLegalFormCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CompanyLegalFormCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CompanyLegalFormCode__listID', 'C', 256, 'AN'],
    [cbc+'CompanyLegalFormCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CompanyLegalFormCode__listURI', 'C', 256, 'AN'],
    [cbc+'CompanyLegalFormCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CompanyLiquidationStatusCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CompanyLiquidationStatusCode__listName', 'C', 256, 'AN'],
    [cbc+'CompanyLiquidationStatusCode__name', 'C', 256, 'AN'],
    [cbc+'CompanyLiquidationStatusCode__languageID', 'C', 256, 'AN'],
    [cbc+'CompanyLiquidationStatusCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CompanyLiquidationStatusCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CompanyLiquidationStatusCode__listID', 'C', 256, 'AN'],
    [cbc+'CompanyLiquidationStatusCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CompanyLiquidationStatusCode__listURI', 'C', 256, 'AN'],
    [cbc+'CompanyLiquidationStatusCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CompletionIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'Condition':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Condition__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Condition__languageID', 'C', 256, 'AN'],
    ],
cbc+'ConditionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ConditionCode__listName', 'C', 256, 'AN'],
    [cbc+'ConditionCode__name', 'C', 256, 'AN'],
    [cbc+'ConditionCode__languageID', 'C', 256, 'AN'],
    [cbc+'ConditionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ConditionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ConditionCode__listID', 'C', 256, 'AN'],
    [cbc+'ConditionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ConditionCode__listURI', 'C', 256, 'AN'],
    [cbc+'ConditionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'Conditions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Conditions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Conditions__languageID', 'C', 256, 'AN'],
    ],
cbc+'ConsigneeAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ConsigneeAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ConsigneeAssignedID__schemeID', 'C', 256, 'AN'],
    [cbc+'ConsigneeAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ConsigneeAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ConsigneeAssignedID__schemeName', 'C', 256, 'AN'],
    [cbc+'ConsigneeAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ConsigneeAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ConsignmentQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'ConsignmentQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'ConsignmentQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'ConsignmentQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'ConsignmentQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'ConsignorAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ConsignorAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ConsignorAssignedID__schemeID', 'C', 256, 'AN'],
    [cbc+'ConsignorAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ConsignorAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ConsignorAssignedID__schemeName', 'C', 256, 'AN'],
    [cbc+'ConsignorAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ConsignorAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ConsolidatableIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ConsumerUnitQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'ConsumerUnitQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'ConsumerUnitQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'ConsumerUnitQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'ConsumerUnitQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'ContainerizedIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'Content':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Content__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Content__languageID', 'C', 256, 'AN'],
    ],
cbc+'ContractType':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ContractType__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ContractType__languageID', 'C', 256, 'AN'],
    ],
cbc+'ContractTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ContractTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'ContractTypeCode__name', 'C', 256, 'AN'],
    [cbc+'ContractTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'ContractTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ContractTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ContractTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'ContractTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ContractTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'ContractTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'ContractedCarrierAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ContractedCarrierAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ContractedCarrierAssignedID__schemeID', 'C', 256, 'AN'],
    [cbc+'ContractedCarrierAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ContractedCarrierAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ContractedCarrierAssignedID__schemeName', 'C', 256, 'AN'],
    [cbc+'ContractedCarrierAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ContractedCarrierAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'CoordinateSystemCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CoordinateSystemCode__listName', 'C', 256, 'AN'],
    [cbc+'CoordinateSystemCode__name', 'C', 256, 'AN'],
    [cbc+'CoordinateSystemCode__languageID', 'C', 256, 'AN'],
    [cbc+'CoordinateSystemCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CoordinateSystemCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CoordinateSystemCode__listID', 'C', 256, 'AN'],
    [cbc+'CoordinateSystemCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CoordinateSystemCode__listURI', 'C', 256, 'AN'],
    [cbc+'CoordinateSystemCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CopyIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'CorporateRegistrationTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CorporateRegistrationTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'CorporateRegistrationTypeCode__name', 'C', 256, 'AN'],
    [cbc+'CorporateRegistrationTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'CorporateRegistrationTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CorporateRegistrationTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CorporateRegistrationTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'CorporateRegistrationTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CorporateRegistrationTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'CorporateRegistrationTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CorporateStockAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CorporateStockAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'CorporateStockAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'CountrySubentity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CountrySubentity__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'CountrySubentity__languageID', 'C', 256, 'AN'],
    ],
cbc+'CountrySubentityCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CountrySubentityCode__listName', 'C', 256, 'AN'],
    [cbc+'CountrySubentityCode__name', 'C', 256, 'AN'],
    [cbc+'CountrySubentityCode__languageID', 'C', 256, 'AN'],
    [cbc+'CountrySubentityCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CountrySubentityCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CountrySubentityCode__listID', 'C', 256, 'AN'],
    [cbc+'CountrySubentityCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CountrySubentityCode__listURI', 'C', 256, 'AN'],
    [cbc+'CountrySubentityCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CrewQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'CrewQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'CrewQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'CrewQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'CrewQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'CurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CurrencyCode__listName', 'C', 256, 'AN'],
    [cbc+'CurrencyCode__name', 'C', 256, 'AN'],
    [cbc+'CurrencyCode__languageID', 'C', 256, 'AN'],
    [cbc+'CurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CurrencyCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CurrencyCode__listID', 'C', 256, 'AN'],
    [cbc+'CurrencyCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CurrencyCode__listURI', 'C', 256, 'AN'],
    [cbc+'CurrencyCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CustomerAssignedAccountID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CustomerAssignedAccountID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'CustomerAssignedAccountID__schemeID', 'C', 256, 'AN'],
    [cbc+'CustomerAssignedAccountID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'CustomerAssignedAccountID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'CustomerAssignedAccountID__schemeName', 'C', 256, 'AN'],
    [cbc+'CustomerAssignedAccountID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'CustomerAssignedAccountID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'CustomerReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CustomerReference__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'CustomerReference__languageID', 'C', 256, 'AN'],
    ],
cbc+'CustomizationID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CustomizationID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'CustomizationID__schemeID', 'C', 256, 'AN'],
    [cbc+'CustomizationID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'CustomizationID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'CustomizationID__schemeName', 'C', 256, 'AN'],
    [cbc+'CustomizationID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'CustomizationID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'CustomsClearanceServiceInstructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CustomsClearanceServiceInstructions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'CustomsClearanceServiceInstructions__languageID', 'C', 256, 'AN'],
    ],
cbc+'CustomsImportClassifiedIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'CustomsStatusCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'CustomsStatusCode__listName', 'C', 256, 'AN'],
    [cbc+'CustomsStatusCode__name', 'C', 256, 'AN'],
    [cbc+'CustomsStatusCode__languageID', 'C', 256, 'AN'],
    [cbc+'CustomsStatusCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'CustomsStatusCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'CustomsStatusCode__listID', 'C', 256, 'AN'],
    [cbc+'CustomsStatusCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'CustomsStatusCode__listURI', 'C', 256, 'AN'],
    [cbc+'CustomsStatusCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'CustomsTariffQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'CustomsTariffQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'CustomsTariffQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'CustomsTariffQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'CustomsTariffQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'DamageRemarks':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DamageRemarks__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'DamageRemarks__languageID', 'C', 256, 'AN'],
    ],
cbc+'DangerousGoodsApprovedIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'DataSendingCapability':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DataSendingCapability__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'DataSendingCapability__languageID', 'C', 256, 'AN'],
    ],
cbc+'Date':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'DeclaredCustomsValueAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DeclaredCustomsValueAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'DeclaredCustomsValueAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'DeclaredForCarriageValueAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DeclaredForCarriageValueAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'DeclaredForCarriageValueAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'DeclaredStatisticsValueAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DeclaredStatisticsValueAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'DeclaredStatisticsValueAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'DeliveredQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'DeliveredQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'DeliveredQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'DeliveredQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'DeliveredQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'DeliveryInstructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DeliveryInstructions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'DeliveryInstructions__languageID', 'C', 256, 'AN'],
    ],
cbc+'DemurrageInstructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DemurrageInstructions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'DemurrageInstructions__languageID', 'C', 256, 'AN'],
    ],
cbc+'Department':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Department__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Department__languageID', 'C', 256, 'AN'],
    ],
cbc+'Description':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'C', 256, 'AN'],
    [cbc+'Description__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Description__languageID', 'C', 256, 'AN'],
    ],
cbc+'DescriptionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DescriptionCode__listName', 'C', 256, 'AN'],
    [cbc+'DescriptionCode__name', 'C', 256, 'AN'],
    [cbc+'DescriptionCode__languageID', 'C', 256, 'AN'],
    [cbc+'DescriptionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'DescriptionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'DescriptionCode__listID', 'C', 256, 'AN'],
    [cbc+'DescriptionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'DescriptionCode__listURI', 'C', 256, 'AN'],
    [cbc+'DescriptionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'DirectionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DirectionCode__listName', 'C', 256, 'AN'],
    [cbc+'DirectionCode__name', 'C', 256, 'AN'],
    [cbc+'DirectionCode__languageID', 'C', 256, 'AN'],
    [cbc+'DirectionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'DirectionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'DirectionCode__listID', 'C', 256, 'AN'],
    [cbc+'DirectionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'DirectionCode__listURI', 'C', 256, 'AN'],
    [cbc+'DirectionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'DispositionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DispositionCode__listName', 'C', 256, 'AN'],
    [cbc+'DispositionCode__name', 'C', 256, 'AN'],
    [cbc+'DispositionCode__languageID', 'C', 256, 'AN'],
    [cbc+'DispositionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'DispositionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'DispositionCode__listID', 'C', 256, 'AN'],
    [cbc+'DispositionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'DispositionCode__listURI', 'C', 256, 'AN'],
    [cbc+'DispositionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'District':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'District__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'District__languageID', 'C', 256, 'AN'],
    ],
cbc+'DocumentCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DocumentCurrencyCode__listName', 'C', 256, 'AN'],
    [cbc+'DocumentCurrencyCode__name', 'C', 256, 'AN'],
    [cbc+'DocumentCurrencyCode__languageID', 'C', 256, 'AN'],
    [cbc+'DocumentCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'DocumentCurrencyCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'DocumentCurrencyCode__listID', 'C', 256, 'AN'],
    [cbc+'DocumentCurrencyCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'DocumentCurrencyCode__listURI', 'C', 256, 'AN'],
    [cbc+'DocumentCurrencyCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'DocumentDescription':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DocumentDescription__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'DocumentDescription__languageID', 'C', 256, 'AN'],
    ],
cbc+'DocumentHash':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DocumentHash__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'DocumentHash__languageID', 'C', 256, 'AN'],
    ],
cbc+'DocumentStatusCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DocumentStatusCode__listName', 'C', 256, 'AN'],
    [cbc+'DocumentStatusCode__name', 'C', 256, 'AN'],
    [cbc+'DocumentStatusCode__languageID', 'C', 256, 'AN'],
    [cbc+'DocumentStatusCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'DocumentStatusCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'DocumentStatusCode__listID', 'C', 256, 'AN'],
    [cbc+'DocumentStatusCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'DocumentStatusCode__listURI', 'C', 256, 'AN'],
    [cbc+'DocumentStatusCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'DocumentType':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DocumentType__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'DocumentType__languageID', 'C', 256, 'AN'],
    ],
cbc+'DocumentTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DocumentTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'DocumentTypeCode__name', 'C', 256, 'AN'],
    [cbc+'DocumentTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'DocumentTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'DocumentTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'DocumentTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'DocumentTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'DocumentTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'DocumentTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'DueDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'DurationMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'DurationMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'DurationMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'EarliestPickupDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'EarliestPickupTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'ElectronicMail':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ElectronicMail__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ElectronicMail__languageID', 'C', 256, 'AN'],
    ],
cbc+'EmbeddedDocumentBinaryObject':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 999999, 'AN'],
    [cbc+'EmbeddedDocumentBinaryObject__format', 'C', 256, 'AN'],
    [cbc+'EmbeddedDocumentBinaryObject__encodingCode', 'C', 256, 'AN'],
    [cbc+'EmbeddedDocumentBinaryObject__uri', 'C', 256, 'AN'],
    [cbc+'EmbeddedDocumentBinaryObject__filename', 'C', 256, 'AN'],
    [cbc+'EmbeddedDocumentBinaryObject__characterSetCode', 'C', 256, 'AN'],
    [cbc+'EmbeddedDocumentBinaryObject__mimeCode', 'C', 256, 'AN'],
    ],
cbc+'EmergencyProceduresCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'EmergencyProceduresCode__listName', 'C', 256, 'AN'],
    [cbc+'EmergencyProceduresCode__name', 'C', 256, 'AN'],
    [cbc+'EmergencyProceduresCode__languageID', 'C', 256, 'AN'],
    [cbc+'EmergencyProceduresCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'EmergencyProceduresCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'EmergencyProceduresCode__listID', 'C', 256, 'AN'],
    [cbc+'EmergencyProceduresCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'EmergencyProceduresCode__listURI', 'C', 256, 'AN'],
    [cbc+'EmergencyProceduresCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'EncodingCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'EncodingCode__listName', 'C', 256, 'AN'],
    [cbc+'EncodingCode__name', 'C', 256, 'AN'],
    [cbc+'EncodingCode__languageID', 'C', 256, 'AN'],
    [cbc+'EncodingCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'EncodingCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'EncodingCode__listID', 'C', 256, 'AN'],
    [cbc+'EncodingCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'EncodingCode__listURI', 'C', 256, 'AN'],
    [cbc+'EncodingCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'EndDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'EndTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'EndpointID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'EndpointID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'EndpointID__schemeID', 'C', 256, 'AN'],
    [cbc+'EndpointID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'EndpointID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'EndpointID__schemeName', 'C', 256, 'AN'],
    [cbc+'EndpointID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'EndpointID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'EnvironmentalEmissionTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'EnvironmentalEmissionTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'EnvironmentalEmissionTypeCode__name', 'C', 256, 'AN'],
    [cbc+'EnvironmentalEmissionTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'EnvironmentalEmissionTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'EnvironmentalEmissionTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'EnvironmentalEmissionTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'EnvironmentalEmissionTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'EnvironmentalEmissionTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'EnvironmentalEmissionTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'EstimatedDeliveryDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'EstimatedDeliveryTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'EstimatedDespatchDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'EstimatedDespatchTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'ExchangeMarketID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ExchangeMarketID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ExchangeMarketID__schemeID', 'C', 256, 'AN'],
    [cbc+'ExchangeMarketID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ExchangeMarketID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ExchangeMarketID__schemeName', 'C', 256, 'AN'],
    [cbc+'ExchangeMarketID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ExchangeMarketID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ExemptionReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ExemptionReason__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ExemptionReason__languageID', 'C', 256, 'AN'],
    ],
cbc+'ExemptionReasonCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ExemptionReasonCode__listName', 'C', 256, 'AN'],
    [cbc+'ExemptionReasonCode__name', 'C', 256, 'AN'],
    [cbc+'ExemptionReasonCode__languageID', 'C', 256, 'AN'],
    [cbc+'ExemptionReasonCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ExemptionReasonCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ExemptionReasonCode__listID', 'C', 256, 'AN'],
    [cbc+'ExemptionReasonCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ExemptionReasonCode__listURI', 'C', 256, 'AN'],
    [cbc+'ExemptionReasonCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'ExpiryDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ExpiryTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'ExtendedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ExtendedID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ExtendedID__schemeID', 'C', 256, 'AN'],
    [cbc+'ExtendedID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ExtendedID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ExtendedID__schemeName', 'C', 256, 'AN'],
    [cbc+'ExtendedID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ExtendedID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'Extension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Extension__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Extension__languageID', 'C', 256, 'AN'],
    ],
cbc+'FamilyName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'FamilyName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'FamilyName__languageID', 'C', 256, 'AN'],
    ],
cbc+'FileName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'FileName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'FileName__languageID', 'C', 256, 'AN'],
    ],
cbc+'FinancingInstrumentCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'FinancingInstrumentCode__listName', 'C', 256, 'AN'],
    [cbc+'FinancingInstrumentCode__name', 'C', 256, 'AN'],
    [cbc+'FinancingInstrumentCode__languageID', 'C', 256, 'AN'],
    [cbc+'FinancingInstrumentCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'FinancingInstrumentCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'FinancingInstrumentCode__listID', 'C', 256, 'AN'],
    [cbc+'FinancingInstrumentCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'FinancingInstrumentCode__listURI', 'C', 256, 'AN'],
    [cbc+'FinancingInstrumentCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'FirstName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'FirstName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'FirstName__languageID', 'C', 256, 'AN'],
    ],
cbc+'Floor':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Floor__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Floor__languageID', 'C', 256, 'AN'],
    ],
cbc+'FormatCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'FormatCode__listName', 'C', 256, 'AN'],
    [cbc+'FormatCode__name', 'C', 256, 'AN'],
    [cbc+'FormatCode__languageID', 'C', 256, 'AN'],
    [cbc+'FormatCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'FormatCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'FormatCode__listID', 'C', 256, 'AN'],
    [cbc+'FormatCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'FormatCode__listURI', 'C', 256, 'AN'],
    [cbc+'FormatCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'ForwarderServiceInstructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ForwarderServiceInstructions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ForwarderServiceInstructions__languageID', 'C', 256, 'AN'],
    ],
cbc+'FreeOfChargeIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'FreeOnBoardValueAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'FreeOnBoardValueAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'FreeOnBoardValueAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'FreightForwarderAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'FreightForwarderAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'FreightForwarderAssignedID__schemeID', 'C', 256, 'AN'],
    [cbc+'FreightForwarderAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'FreightForwarderAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'FreightForwarderAssignedID__schemeName', 'C', 256, 'AN'],
    [cbc+'FreightForwarderAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'FreightForwarderAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'FreightRateClassCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'FreightRateClassCode__listName', 'C', 256, 'AN'],
    [cbc+'FreightRateClassCode__name', 'C', 256, 'AN'],
    [cbc+'FreightRateClassCode__languageID', 'C', 256, 'AN'],
    [cbc+'FreightRateClassCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'FreightRateClassCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'FreightRateClassCode__listID', 'C', 256, 'AN'],
    [cbc+'FreightRateClassCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'FreightRateClassCode__listURI', 'C', 256, 'AN'],
    [cbc+'FreightRateClassCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'FullnessIndicationCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'FullnessIndicationCode__listName', 'C', 256, 'AN'],
    [cbc+'FullnessIndicationCode__name', 'C', 256, 'AN'],
    [cbc+'FullnessIndicationCode__languageID', 'C', 256, 'AN'],
    [cbc+'FullnessIndicationCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'FullnessIndicationCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'FullnessIndicationCode__listID', 'C', 256, 'AN'],
    [cbc+'FullnessIndicationCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'FullnessIndicationCode__listURI', 'C', 256, 'AN'],
    [cbc+'FullnessIndicationCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'FullyPaidSharesIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'GenderCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'GenderCode__listName', 'C', 256, 'AN'],
    [cbc+'GenderCode__name', 'C', 256, 'AN'],
    [cbc+'GenderCode__languageID', 'C', 256, 'AN'],
    [cbc+'GenderCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'GenderCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'GenderCode__listID', 'C', 256, 'AN'],
    [cbc+'GenderCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'GenderCode__listURI', 'C', 256, 'AN'],
    [cbc+'GenderCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'GeneralCargoIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'GrossTonnageMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'GrossTonnageMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'GrossTonnageMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'GrossVolumeMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'GrossVolumeMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'GrossVolumeMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'GrossWeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'GrossWeightMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'GrossWeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'GuaranteedDespatchDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'GuaranteedDespatchTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'HandlingCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'HandlingCode__listName', 'C', 256, 'AN'],
    [cbc+'HandlingCode__name', 'C', 256, 'AN'],
    [cbc+'HandlingCode__languageID', 'C', 256, 'AN'],
    [cbc+'HandlingCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'HandlingCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'HandlingCode__listID', 'C', 256, 'AN'],
    [cbc+'HandlingCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'HandlingCode__listURI', 'C', 256, 'AN'],
    [cbc+'HandlingCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'HandlingInstructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'HandlingInstructions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'HandlingInstructions__languageID', 'C', 256, 'AN'],
    ],
cbc+'HashAlgorithmMethod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'HashAlgorithmMethod__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'HashAlgorithmMethod__languageID', 'C', 256, 'AN'],
    ],
cbc+'HaulageInstructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'HaulageInstructions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'HaulageInstructions__languageID', 'C', 256, 'AN'],
    ],
cbc+'HazardClassID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'HazardClassID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'HazardClassID__schemeID', 'C', 256, 'AN'],
    [cbc+'HazardClassID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'HazardClassID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'HazardClassID__schemeName', 'C', 256, 'AN'],
    [cbc+'HazardClassID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'HazardClassID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'HazardousCategoryCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'HazardousCategoryCode__listName', 'C', 256, 'AN'],
    [cbc+'HazardousCategoryCode__name', 'C', 256, 'AN'],
    [cbc+'HazardousCategoryCode__languageID', 'C', 256, 'AN'],
    [cbc+'HazardousCategoryCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'HazardousCategoryCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'HazardousCategoryCode__listID', 'C', 256, 'AN'],
    [cbc+'HazardousCategoryCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'HazardousCategoryCode__listURI', 'C', 256, 'AN'],
    [cbc+'HazardousCategoryCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'HazardousRegulationCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'HazardousRegulationCode__listName', 'C', 256, 'AN'],
    [cbc+'HazardousRegulationCode__name', 'C', 256, 'AN'],
    [cbc+'HazardousRegulationCode__languageID', 'C', 256, 'AN'],
    [cbc+'HazardousRegulationCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'HazardousRegulationCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'HazardousRegulationCode__listID', 'C', 256, 'AN'],
    [cbc+'HazardousRegulationCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'HazardousRegulationCode__listURI', 'C', 256, 'AN'],
    [cbc+'HazardousRegulationCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'HazardousRiskIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'HolderName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'HolderName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'HolderName__languageID', 'C', 256, 'AN'],
    ],
cbc+'HumanFoodApprovedIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'HumanFoodIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'HumidityPercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'HumidityPercent__format', 'C', 256, 'AN'],
    ],
cbc+'ID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ID__schemeID', 'C', 256, 'AN'],
    [cbc+'ID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ID__schemeName', 'C', 256, 'AN'],
    [cbc+'ID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'IdentificationCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'IdentificationCode__listName', 'C', 256, 'AN'],
    [cbc+'IdentificationCode__name', 'C', 256, 'AN'],
    [cbc+'IdentificationCode__languageID', 'C', 256, 'AN'],
    [cbc+'IdentificationCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'IdentificationCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'IdentificationCode__listID', 'C', 256, 'AN'],
    [cbc+'IdentificationCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'IdentificationCode__listURI', 'C', 256, 'AN'],
    [cbc+'IdentificationCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'IdentificationID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'IdentificationID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'IdentificationID__schemeID', 'C', 256, 'AN'],
    [cbc+'IdentificationID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'IdentificationID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'IdentificationID__schemeName', 'C', 256, 'AN'],
    [cbc+'IdentificationID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'IdentificationID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ImportanceCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ImportanceCode__listName', 'C', 256, 'AN'],
    [cbc+'ImportanceCode__name', 'C', 256, 'AN'],
    [cbc+'ImportanceCode__languageID', 'C', 256, 'AN'],
    [cbc+'ImportanceCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ImportanceCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ImportanceCode__listID', 'C', 256, 'AN'],
    [cbc+'ImportanceCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ImportanceCode__listURI', 'C', 256, 'AN'],
    [cbc+'ImportanceCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'IndicationIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'IndustryClassificationCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'IndustryClassificationCode__listName', 'C', 256, 'AN'],
    [cbc+'IndustryClassificationCode__name', 'C', 256, 'AN'],
    [cbc+'IndustryClassificationCode__languageID', 'C', 256, 'AN'],
    [cbc+'IndustryClassificationCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'IndustryClassificationCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'IndustryClassificationCode__listID', 'C', 256, 'AN'],
    [cbc+'IndustryClassificationCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'IndustryClassificationCode__listURI', 'C', 256, 'AN'],
    [cbc+'IndustryClassificationCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'Information':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Information__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Information__languageID', 'C', 256, 'AN'],
    ],
cbc+'InformationURI':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'InformationURI__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'InformationURI__schemeID', 'C', 256, 'AN'],
    [cbc+'InformationURI__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'InformationURI__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'InformationURI__schemeName', 'C', 256, 'AN'],
    [cbc+'InformationURI__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'InformationURI__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'InhalationToxicityZoneCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'InhalationToxicityZoneCode__listName', 'C', 256, 'AN'],
    [cbc+'InhalationToxicityZoneCode__name', 'C', 256, 'AN'],
    [cbc+'InhalationToxicityZoneCode__languageID', 'C', 256, 'AN'],
    [cbc+'InhalationToxicityZoneCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'InhalationToxicityZoneCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'InhalationToxicityZoneCode__listID', 'C', 256, 'AN'],
    [cbc+'InhalationToxicityZoneCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'InhalationToxicityZoneCode__listURI', 'C', 256, 'AN'],
    [cbc+'InhalationToxicityZoneCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'InhouseMail':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'InhouseMail__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'InhouseMail__languageID', 'C', 256, 'AN'],
    ],
cbc+'InstallmentDueDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'InstructionID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'InstructionID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'InstructionID__schemeID', 'C', 256, 'AN'],
    [cbc+'InstructionID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'InstructionID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'InstructionID__schemeName', 'C', 256, 'AN'],
    [cbc+'InstructionID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'InstructionID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'InstructionNote':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'InstructionNote__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'InstructionNote__languageID', 'C', 256, 'AN'],
    ],
cbc+'Instructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Instructions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Instructions__languageID', 'C', 256, 'AN'],
    ],
cbc+'InsurancePremiumAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'InsurancePremiumAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'InsurancePremiumAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'InsuranceValueAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'InsuranceValueAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'InsuranceValueAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'InvoiceTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'InvoiceTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'InvoiceTypeCode__name', 'C', 256, 'AN'],
    [cbc+'InvoiceTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'InvoiceTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'InvoiceTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'InvoiceTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'InvoiceTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'InvoiceTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'InvoiceTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'InvoicedQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'InvoicedQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'InvoicedQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'InvoicedQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'InvoicedQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'InvoicingPartyReference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'InvoicingPartyReference__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'InvoicingPartyReference__languageID', 'C', 256, 'AN'],
    ],
cbc+'IssueDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'IssueNumberID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'IssueNumberID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'IssueNumberID__schemeID', 'C', 256, 'AN'],
    [cbc+'IssueNumberID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'IssueNumberID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'IssueNumberID__schemeName', 'C', 256, 'AN'],
    [cbc+'IssueNumberID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'IssueNumberID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'IssueTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'IssuerID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'IssuerID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'IssuerID__schemeID', 'C', 256, 'AN'],
    [cbc+'IssuerID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'IssuerID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'IssuerID__schemeName', 'C', 256, 'AN'],
    [cbc+'IssuerID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'IssuerID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ItemClassificationCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ItemClassificationCode__listName', 'C', 256, 'AN'],
    [cbc+'ItemClassificationCode__name', 'C', 256, 'AN'],
    [cbc+'ItemClassificationCode__languageID', 'C', 256, 'AN'],
    [cbc+'ItemClassificationCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ItemClassificationCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ItemClassificationCode__listID', 'C', 256, 'AN'],
    [cbc+'ItemClassificationCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ItemClassificationCode__listURI', 'C', 256, 'AN'],
    [cbc+'ItemClassificationCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'JobTitle':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'JobTitle__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'JobTitle__languageID', 'C', 256, 'AN'],
    ],
cbc+'JourneyID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'JourneyID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'JourneyID__schemeID', 'C', 256, 'AN'],
    [cbc+'JourneyID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'JourneyID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'JourneyID__schemeName', 'C', 256, 'AN'],
    [cbc+'JourneyID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'JourneyID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'Keyword':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Keyword__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Keyword__languageID', 'C', 256, 'AN'],
    ],
cbc+'LanguageID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LanguageID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'LanguageID__schemeID', 'C', 256, 'AN'],
    [cbc+'LanguageID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'LanguageID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'LanguageID__schemeName', 'C', 256, 'AN'],
    [cbc+'LanguageID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'LanguageID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'LatestDeliveryDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'LatestDeliveryTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'LatestPickupDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'LatestPickupTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'LatitudeDegreesMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LatitudeDegreesMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'LatitudeDegreesMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'LatitudeDirectionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LatitudeDirectionCode__listName', 'C', 256, 'AN'],
    [cbc+'LatitudeDirectionCode__name', 'C', 256, 'AN'],
    [cbc+'LatitudeDirectionCode__languageID', 'C', 256, 'AN'],
    [cbc+'LatitudeDirectionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'LatitudeDirectionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'LatitudeDirectionCode__listID', 'C', 256, 'AN'],
    [cbc+'LatitudeDirectionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'LatitudeDirectionCode__listURI', 'C', 256, 'AN'],
    [cbc+'LatitudeDirectionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'LatitudeMinutesMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LatitudeMinutesMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'LatitudeMinutesMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'LeadTimeMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LeadTimeMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'LeadTimeMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'LegalStatusIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'LicensePlateID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LicensePlateID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'LicensePlateID__schemeID', 'C', 256, 'AN'],
    [cbc+'LicensePlateID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'LicensePlateID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'LicensePlateID__schemeName', 'C', 256, 'AN'],
    [cbc+'LicensePlateID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'LicensePlateID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'Line':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Line__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Line__languageID', 'C', 256, 'AN'],
    ],
cbc+'LineCountNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'LineCountNumeric__format', 'C', 256, 'AN'],
    ],
cbc+'LineExtensionAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LineExtensionAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'LineExtensionAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'LineID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LineID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'LineID__schemeID', 'C', 256, 'AN'],
    [cbc+'LineID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'LineID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'LineID__schemeName', 'C', 256, 'AN'],
    [cbc+'LineID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'LineID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'LineStatusCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LineStatusCode__listName', 'C', 256, 'AN'],
    [cbc+'LineStatusCode__name', 'C', 256, 'AN'],
    [cbc+'LineStatusCode__languageID', 'C', 256, 'AN'],
    [cbc+'LineStatusCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'LineStatusCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'LineStatusCode__listID', 'C', 256, 'AN'],
    [cbc+'LineStatusCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'LineStatusCode__listURI', 'C', 256, 'AN'],
    [cbc+'LineStatusCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'ListValue':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ListValue__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ListValue__languageID', 'C', 256, 'AN'],
    ],
cbc+'LivestockIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'LoadingLengthMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LoadingLengthMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'LoadingLengthMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'LoadingSequenceID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LoadingSequenceID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'LoadingSequenceID__schemeID', 'C', 256, 'AN'],
    [cbc+'LoadingSequenceID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'LoadingSequenceID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'LoadingSequenceID__schemeName', 'C', 256, 'AN'],
    [cbc+'LoadingSequenceID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'LoadingSequenceID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'LocaleCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LocaleCode__listName', 'C', 256, 'AN'],
    [cbc+'LocaleCode__name', 'C', 256, 'AN'],
    [cbc+'LocaleCode__languageID', 'C', 256, 'AN'],
    [cbc+'LocaleCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'LocaleCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'LocaleCode__listID', 'C', 256, 'AN'],
    [cbc+'LocaleCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'LocaleCode__listURI', 'C', 256, 'AN'],
    [cbc+'LocaleCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'Location':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Location__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Location__languageID', 'C', 256, 'AN'],
    ],
cbc+'LocationID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LocationID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'LocationID__schemeID', 'C', 256, 'AN'],
    [cbc+'LocationID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'LocationID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'LocationID__schemeName', 'C', 256, 'AN'],
    [cbc+'LocationID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'LocationID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'LocationTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LocationTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'LocationTypeCode__name', 'C', 256, 'AN'],
    [cbc+'LocationTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'LocationTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'LocationTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'LocationTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'LocationTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'LocationTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'LocationTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'LogoReferenceID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LogoReferenceID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'LogoReferenceID__schemeID', 'C', 256, 'AN'],
    [cbc+'LogoReferenceID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'LogoReferenceID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'LogoReferenceID__schemeName', 'C', 256, 'AN'],
    [cbc+'LogoReferenceID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'LogoReferenceID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'LongitudeDegreesMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LongitudeDegreesMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'LongitudeDegreesMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'LongitudeDirectionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LongitudeDirectionCode__listName', 'C', 256, 'AN'],
    [cbc+'LongitudeDirectionCode__name', 'C', 256, 'AN'],
    [cbc+'LongitudeDirectionCode__languageID', 'C', 256, 'AN'],
    [cbc+'LongitudeDirectionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'LongitudeDirectionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'LongitudeDirectionCode__listID', 'C', 256, 'AN'],
    [cbc+'LongitudeDirectionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'LongitudeDirectionCode__listURI', 'C', 256, 'AN'],
    [cbc+'LongitudeDirectionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'LongitudeMinutesMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LongitudeMinutesMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'LongitudeMinutesMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'LossRisk':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LossRisk__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'LossRisk__languageID', 'C', 256, 'AN'],
    ],
cbc+'LossRiskResponsibilityCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LossRiskResponsibilityCode__listName', 'C', 256, 'AN'],
    [cbc+'LossRiskResponsibilityCode__name', 'C', 256, 'AN'],
    [cbc+'LossRiskResponsibilityCode__languageID', 'C', 256, 'AN'],
    [cbc+'LossRiskResponsibilityCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'LossRiskResponsibilityCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'LossRiskResponsibilityCode__listID', 'C', 256, 'AN'],
    [cbc+'LossRiskResponsibilityCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'LossRiskResponsibilityCode__listURI', 'C', 256, 'AN'],
    [cbc+'LossRiskResponsibilityCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'LotNumberID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LotNumberID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'LotNumberID__schemeID', 'C', 256, 'AN'],
    [cbc+'LotNumberID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'LotNumberID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'LotNumberID__schemeName', 'C', 256, 'AN'],
    [cbc+'LotNumberID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'LotNumberID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'LowerOrangeHazardPlacardID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'LowerOrangeHazardPlacardID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'LowerOrangeHazardPlacardID__schemeID', 'C', 256, 'AN'],
    [cbc+'LowerOrangeHazardPlacardID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'LowerOrangeHazardPlacardID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'LowerOrangeHazardPlacardID__schemeName', 'C', 256, 'AN'],
    [cbc+'LowerOrangeHazardPlacardID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'LowerOrangeHazardPlacardID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'MandateTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MandateTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'MandateTypeCode__name', 'C', 256, 'AN'],
    [cbc+'MandateTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'MandateTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'MandateTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'MandateTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'MandateTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'MandateTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'MandateTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'ManufactureDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ManufactureTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'MarkAttention':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MarkAttention__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'MarkAttention__languageID', 'C', 256, 'AN'],
    ],
cbc+'MarkAttentionIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'MarkCare':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MarkCare__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'MarkCare__languageID', 'C', 256, 'AN'],
    ],
cbc+'MarkCareIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'MarkingID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MarkingID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'MarkingID__schemeID', 'C', 256, 'AN'],
    [cbc+'MarkingID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'MarkingID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'MarkingID__schemeName', 'C', 256, 'AN'],
    [cbc+'MarkingID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'MarkingID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'MathematicOperatorCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MathematicOperatorCode__listName', 'C', 256, 'AN'],
    [cbc+'MathematicOperatorCode__name', 'C', 256, 'AN'],
    [cbc+'MathematicOperatorCode__languageID', 'C', 256, 'AN'],
    [cbc+'MathematicOperatorCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'MathematicOperatorCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'MathematicOperatorCode__listID', 'C', 256, 'AN'],
    [cbc+'MathematicOperatorCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'MathematicOperatorCode__listURI', 'C', 256, 'AN'],
    [cbc+'MathematicOperatorCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'MaximumMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MaximumMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'MaximumMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'MaximumPaidAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MaximumPaidAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'MaximumPaidAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'MaximumPaymentInstructionsNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'MaximumPaymentInstructionsNumeric__format', 'C', 256, 'AN'],
    ],
cbc+'MaximumQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'MaximumQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'MaximumQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'MaximumQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'MaximumQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'MaximumValue':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MaximumValue__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'MaximumValue__languageID', 'C', 256, 'AN'],
    ],
cbc+'Measure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Measure__unitCode', 'C', 256, 'AN'],
    [cbc+'Measure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'MedicalFirstAidGuideCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MedicalFirstAidGuideCode__listName', 'C', 256, 'AN'],
    [cbc+'MedicalFirstAidGuideCode__name', 'C', 256, 'AN'],
    [cbc+'MedicalFirstAidGuideCode__languageID', 'C', 256, 'AN'],
    [cbc+'MedicalFirstAidGuideCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'MedicalFirstAidGuideCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'MedicalFirstAidGuideCode__listID', 'C', 256, 'AN'],
    [cbc+'MedicalFirstAidGuideCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'MedicalFirstAidGuideCode__listURI', 'C', 256, 'AN'],
    [cbc+'MedicalFirstAidGuideCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'MiddleName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MiddleName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'MiddleName__languageID', 'C', 256, 'AN'],
    ],
cbc+'MimeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MimeCode__listName', 'C', 256, 'AN'],
    [cbc+'MimeCode__name', 'C', 256, 'AN'],
    [cbc+'MimeCode__languageID', 'C', 256, 'AN'],
    [cbc+'MimeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'MimeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'MimeCode__listID', 'C', 256, 'AN'],
    [cbc+'MimeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'MimeCode__listURI', 'C', 256, 'AN'],
    [cbc+'MimeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'MinimumMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MinimumMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'MinimumMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'MinimumQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'MinimumQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'MinimumQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'MinimumQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'MinimumQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'MinimumValue':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'MinimumValue__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'MinimumValue__languageID', 'C', 256, 'AN'],
    ],
cbc+'ModelName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ModelName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ModelName__languageID', 'C', 256, 'AN'],
    ],
cbc+'MultiplierFactorNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'MultiplierFactorNumeric__format', 'C', 256, 'AN'],
    ],
cbc+'Name':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Name__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Name__languageID', 'C', 256, 'AN'],
    ],
cbc+'NameCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'NameCode__listName', 'C', 256, 'AN'],
    [cbc+'NameCode__name', 'C', 256, 'AN'],
    [cbc+'NameCode__languageID', 'C', 256, 'AN'],
    [cbc+'NameCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'NameCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'NameCode__listID', 'C', 256, 'AN'],
    [cbc+'NameCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'NameCode__listURI', 'C', 256, 'AN'],
    [cbc+'NameCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'NameSuffix':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'NameSuffix__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'NameSuffix__languageID', 'C', 256, 'AN'],
    ],
cbc+'NationalityID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'NationalityID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'NationalityID__schemeID', 'C', 256, 'AN'],
    [cbc+'NationalityID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'NationalityID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'NationalityID__schemeName', 'C', 256, 'AN'],
    [cbc+'NationalityID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'NationalityID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'NatureCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'NatureCode__listName', 'C', 256, 'AN'],
    [cbc+'NatureCode__name', 'C', 256, 'AN'],
    [cbc+'NatureCode__languageID', 'C', 256, 'AN'],
    [cbc+'NatureCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'NatureCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'NatureCode__listID', 'C', 256, 'AN'],
    [cbc+'NatureCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'NatureCode__listURI', 'C', 256, 'AN'],
    [cbc+'NatureCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'NetNetWeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'NetNetWeightMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'NetNetWeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'NetTonnageMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'NetTonnageMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'NetTonnageMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'NetVolumeMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'NetVolumeMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'NetVolumeMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'NetWeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'NetWeightMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'NetWeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'NetworkID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'NetworkID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'NetworkID__schemeID', 'C', 256, 'AN'],
    [cbc+'NetworkID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'NetworkID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'NetworkID__schemeName', 'C', 256, 'AN'],
    [cbc+'NetworkID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'NetworkID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'NominationDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'NominationTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'Note':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 9999, 'AN'],
    [cbc+'Note__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Note__languageID', 'C', 256, 'AN'],
    ],
cbc+'OccurrenceDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'OccurrenceTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'OnCarriageIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'OrderTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'OrderTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'OrderTypeCode__name', 'C', 256, 'AN'],
    [cbc+'OrderTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'OrderTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'OrderTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'OrderTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'OrderTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'OrderTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'OrderTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'OrderableUnitFactorRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'OrderableUnitFactorRate__format', 'C', 256, 'AN'],
    ],
cbc+'OrganizationDepartment':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'OrganizationDepartment__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'OrganizationDepartment__languageID', 'C', 256, 'AN'],
    ],
cbc+'OtherName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'OtherName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'OtherName__languageID', 'C', 256, 'AN'],
    ],
cbc+'OutstandingQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'OutstandingQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'OutstandingQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'OutstandingQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'OutstandingQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'OutstandingReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'OutstandingReason__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'OutstandingReason__languageID', 'C', 256, 'AN'],
    ],
cbc+'OversupplyQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'OversupplyQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'OversupplyQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'OversupplyQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'OversupplyQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'OwnerTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'OwnerTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'OwnerTypeCode__name', 'C', 256, 'AN'],
    [cbc+'OwnerTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'OwnerTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'OwnerTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'OwnerTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'OwnerTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'OwnerTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'OwnerTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PackQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'PackQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'PackQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'PackQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'PackQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'PackSizeNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'PackSizeNumeric__format', 'C', 256, 'AN'],
    ],
cbc+'PackageLevelCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PackageLevelCode__listName', 'C', 256, 'AN'],
    [cbc+'PackageLevelCode__name', 'C', 256, 'AN'],
    [cbc+'PackageLevelCode__languageID', 'C', 256, 'AN'],
    [cbc+'PackageLevelCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PackageLevelCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PackageLevelCode__listID', 'C', 256, 'AN'],
    [cbc+'PackageLevelCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PackageLevelCode__listURI', 'C', 256, 'AN'],
    [cbc+'PackageLevelCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PackagingTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PackagingTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'PackagingTypeCode__name', 'C', 256, 'AN'],
    [cbc+'PackagingTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'PackagingTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PackagingTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PackagingTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'PackagingTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PackagingTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'PackagingTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PackingCriteriaCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PackingCriteriaCode__listName', 'C', 256, 'AN'],
    [cbc+'PackingCriteriaCode__name', 'C', 256, 'AN'],
    [cbc+'PackingCriteriaCode__languageID', 'C', 256, 'AN'],
    [cbc+'PackingCriteriaCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PackingCriteriaCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PackingCriteriaCode__listID', 'C', 256, 'AN'],
    [cbc+'PackingCriteriaCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PackingCriteriaCode__listURI', 'C', 256, 'AN'],
    [cbc+'PackingCriteriaCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PackingMaterial':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PackingMaterial__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'PackingMaterial__languageID', 'C', 256, 'AN'],
    ],
cbc+'PaidAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PaidAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'PaidAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'PaidDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'PaidTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'PartecipationPercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'PartecipationPercent__format', 'C', 256, 'AN'],
    ],
cbc+'PassengerQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'PassengerQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'PassengerQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'PassengerQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'PassengerQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'PayableAlternativeAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PayableAlternativeAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'PayableAlternativeAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'PayableAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PayableAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'PayableAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'PayableRoundingAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PayableRoundingAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'PayableRoundingAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'PaymentAlternativeCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PaymentAlternativeCurrencyCode__listName', 'C', 256, 'AN'],
    [cbc+'PaymentAlternativeCurrencyCode__name', 'C', 256, 'AN'],
    [cbc+'PaymentAlternativeCurrencyCode__languageID', 'C', 256, 'AN'],
    [cbc+'PaymentAlternativeCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PaymentAlternativeCurrencyCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PaymentAlternativeCurrencyCode__listID', 'C', 256, 'AN'],
    [cbc+'PaymentAlternativeCurrencyCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PaymentAlternativeCurrencyCode__listURI', 'C', 256, 'AN'],
    [cbc+'PaymentAlternativeCurrencyCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PaymentChannelCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PaymentChannelCode__listName', 'C', 256, 'AN'],
    [cbc+'PaymentChannelCode__name', 'C', 256, 'AN'],
    [cbc+'PaymentChannelCode__languageID', 'C', 256, 'AN'],
    [cbc+'PaymentChannelCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PaymentChannelCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PaymentChannelCode__listID', 'C', 256, 'AN'],
    [cbc+'PaymentChannelCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PaymentChannelCode__listURI', 'C', 256, 'AN'],
    [cbc+'PaymentChannelCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PaymentCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PaymentCurrencyCode__listName', 'C', 256, 'AN'],
    [cbc+'PaymentCurrencyCode__name', 'C', 256, 'AN'],
    [cbc+'PaymentCurrencyCode__languageID', 'C', 256, 'AN'],
    [cbc+'PaymentCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PaymentCurrencyCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PaymentCurrencyCode__listID', 'C', 256, 'AN'],
    [cbc+'PaymentCurrencyCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PaymentCurrencyCode__listURI', 'C', 256, 'AN'],
    [cbc+'PaymentCurrencyCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PaymentDueDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'PaymentID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PaymentID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'PaymentID__schemeID', 'C', 256, 'AN'],
    [cbc+'PaymentID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'PaymentID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'PaymentID__schemeName', 'C', 256, 'AN'],
    [cbc+'PaymentID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'PaymentID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'PaymentMeansCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PaymentMeansCode__listName', 'C', 256, 'AN'],
    [cbc+'PaymentMeansCode__name', 'C', 256, 'AN'],
    [cbc+'PaymentMeansCode__languageID', 'C', 256, 'AN'],
    [cbc+'PaymentMeansCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PaymentMeansCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PaymentMeansCode__listID', 'C', 256, 'AN'],
    [cbc+'PaymentMeansCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PaymentMeansCode__listURI', 'C', 256, 'AN'],
    [cbc+'PaymentMeansCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PaymentMeansID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PaymentMeansID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'PaymentMeansID__schemeID', 'C', 256, 'AN'],
    [cbc+'PaymentMeansID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'PaymentMeansID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'PaymentMeansID__schemeName', 'C', 256, 'AN'],
    [cbc+'PaymentMeansID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'PaymentMeansID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'PaymentNote':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PaymentNote__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'PaymentNote__languageID', 'C', 256, 'AN'],
    ],
cbc+'PaymentPercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'PaymentPercent__format', 'C', 256, 'AN'],
    ],
cbc+'PaymentPurposeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PaymentPurposeCode__listName', 'C', 256, 'AN'],
    [cbc+'PaymentPurposeCode__name', 'C', 256, 'AN'],
    [cbc+'PaymentPurposeCode__languageID', 'C', 256, 'AN'],
    [cbc+'PaymentPurposeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PaymentPurposeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PaymentPurposeCode__listID', 'C', 256, 'AN'],
    [cbc+'PaymentPurposeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PaymentPurposeCode__listURI', 'C', 256, 'AN'],
    [cbc+'PaymentPurposeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PaymentTermsDetailsURI':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PaymentTermsDetailsURI__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'PaymentTermsDetailsURI__schemeID', 'C', 256, 'AN'],
    [cbc+'PaymentTermsDetailsURI__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'PaymentTermsDetailsURI__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'PaymentTermsDetailsURI__schemeName', 'C', 256, 'AN'],
    [cbc+'PaymentTermsDetailsURI__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'PaymentTermsDetailsURI__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'PenaltyAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PenaltyAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'PenaltyAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'PenaltySurchargePercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'PenaltySurchargePercent__format', 'C', 256, 'AN'],
    ],
cbc+'PerUnitAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PerUnitAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'PerUnitAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'Percent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'Percent__format', 'C', 256, 'AN'],
    ],
cbc+'PerformingCarrierAssignedID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PerformingCarrierAssignedID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'PerformingCarrierAssignedID__schemeID', 'C', 256, 'AN'],
    [cbc+'PerformingCarrierAssignedID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'PerformingCarrierAssignedID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'PerformingCarrierAssignedID__schemeName', 'C', 256, 'AN'],
    [cbc+'PerformingCarrierAssignedID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'PerformingCarrierAssignedID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'PlacardEndorsement':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PlacardEndorsement__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'PlacardEndorsement__languageID', 'C', 256, 'AN'],
    ],
cbc+'PlacardNotation':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PlacardNotation__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'PlacardNotation__languageID', 'C', 256, 'AN'],
    ],
cbc+'PlotIdentification':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PlotIdentification__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'PlotIdentification__languageID', 'C', 256, 'AN'],
    ],
cbc+'PositionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PositionCode__listName', 'C', 256, 'AN'],
    [cbc+'PositionCode__name', 'C', 256, 'AN'],
    [cbc+'PositionCode__languageID', 'C', 256, 'AN'],
    [cbc+'PositionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PositionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PositionCode__listID', 'C', 256, 'AN'],
    [cbc+'PositionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PositionCode__listURI', 'C', 256, 'AN'],
    [cbc+'PositionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PostalZone':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PostalZone__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'PostalZone__languageID', 'C', 256, 'AN'],
    ],
cbc+'Postbox':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Postbox__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Postbox__languageID', 'C', 256, 'AN'],
    ],
cbc+'PowerIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'PreCarriageIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'PreferenceCriterionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PreferenceCriterionCode__listName', 'C', 256, 'AN'],
    [cbc+'PreferenceCriterionCode__name', 'C', 256, 'AN'],
    [cbc+'PreferenceCriterionCode__languageID', 'C', 256, 'AN'],
    [cbc+'PreferenceCriterionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PreferenceCriterionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PreferenceCriterionCode__listID', 'C', 256, 'AN'],
    [cbc+'PreferenceCriterionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PreferenceCriterionCode__listURI', 'C', 256, 'AN'],
    [cbc+'PreferenceCriterionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PrepaidAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PrepaidAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'PrepaidAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'PrepaidIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'PrepaidPaymentReferenceID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PrepaidPaymentReferenceID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'PrepaidPaymentReferenceID__schemeID', 'C', 256, 'AN'],
    [cbc+'PrepaidPaymentReferenceID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'PrepaidPaymentReferenceID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'PrepaidPaymentReferenceID__schemeName', 'C', 256, 'AN'],
    [cbc+'PrepaidPaymentReferenceID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'PrepaidPaymentReferenceID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'PriceAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PriceAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'PriceAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'PriceChangeReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PriceChangeReason__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'PriceChangeReason__languageID', 'C', 256, 'AN'],
    ],
cbc+'PriceType':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PriceType__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'PriceType__languageID', 'C', 256, 'AN'],
    ],
cbc+'PriceTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PriceTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'PriceTypeCode__name', 'C', 256, 'AN'],
    [cbc+'PriceTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'PriceTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PriceTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PriceTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'PriceTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PriceTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'PriceTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PricingCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PricingCurrencyCode__listName', 'C', 256, 'AN'],
    [cbc+'PricingCurrencyCode__name', 'C', 256, 'AN'],
    [cbc+'PricingCurrencyCode__languageID', 'C', 256, 'AN'],
    [cbc+'PricingCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'PricingCurrencyCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'PricingCurrencyCode__listID', 'C', 256, 'AN'],
    [cbc+'PricingCurrencyCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'PricingCurrencyCode__listURI', 'C', 256, 'AN'],
    [cbc+'PricingCurrencyCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'PrimaryAccountNumberID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'PrimaryAccountNumberID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'PrimaryAccountNumberID__schemeID', 'C', 256, 'AN'],
    [cbc+'PrimaryAccountNumberID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'PrimaryAccountNumberID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'PrimaryAccountNumberID__schemeName', 'C', 256, 'AN'],
    [cbc+'PrimaryAccountNumberID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'PrimaryAccountNumberID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'Priority':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Priority__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Priority__languageID', 'C', 256, 'AN'],
    ],
cbc+'ProductTraceID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ProductTraceID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ProductTraceID__schemeID', 'C', 256, 'AN'],
    [cbc+'ProductTraceID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ProductTraceID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ProductTraceID__schemeName', 'C', 256, 'AN'],
    [cbc+'ProductTraceID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ProductTraceID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ProfileExecutionID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ProfileExecutionID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ProfileExecutionID__schemeID', 'C', 256, 'AN'],
    [cbc+'ProfileExecutionID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ProfileExecutionID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ProfileExecutionID__schemeName', 'C', 256, 'AN'],
    [cbc+'ProfileExecutionID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ProfileExecutionID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ProfileID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ProfileID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ProfileID__schemeID', 'C', 256, 'AN'],
    [cbc+'ProfileID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ProfileID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ProfileID__schemeName', 'C', 256, 'AN'],
    [cbc+'ProfileID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ProfileID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ProgressPercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'ProgressPercent__format', 'C', 256, 'AN'],
    ],
cbc+'ProviderTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ProviderTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'ProviderTypeCode__name', 'C', 256, 'AN'],
    [cbc+'ProviderTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'ProviderTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ProviderTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ProviderTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'ProviderTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ProviderTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'ProviderTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'Quantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'Quantity__unitCode', 'C', 256, 'AN'],
    [cbc+'Quantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'Quantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'Quantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'QuantityDiscrepancyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'QuantityDiscrepancyCode__listName', 'C', 256, 'AN'],
    [cbc+'QuantityDiscrepancyCode__name', 'C', 256, 'AN'],
    [cbc+'QuantityDiscrepancyCode__languageID', 'C', 256, 'AN'],
    [cbc+'QuantityDiscrepancyCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'QuantityDiscrepancyCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'QuantityDiscrepancyCode__listID', 'C', 256, 'AN'],
    [cbc+'QuantityDiscrepancyCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'QuantityDiscrepancyCode__listURI', 'C', 256, 'AN'],
    [cbc+'QuantityDiscrepancyCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'RadioCallSignID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'RadioCallSignID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'RadioCallSignID__schemeID', 'C', 256, 'AN'],
    [cbc+'RadioCallSignID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'RadioCallSignID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'RadioCallSignID__schemeName', 'C', 256, 'AN'],
    [cbc+'RadioCallSignID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'RadioCallSignID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'RailCarID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'RailCarID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'RailCarID__schemeID', 'C', 256, 'AN'],
    [cbc+'RailCarID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'RailCarID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'RailCarID__schemeName', 'C', 256, 'AN'],
    [cbc+'RailCarID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'RailCarID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ReceivedDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ReceivedQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'ReceivedQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'ReceivedQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'ReceivedQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'ReceivedQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'Reference':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Reference__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Reference__languageID', 'C', 256, 'AN'],
    ],
cbc+'ReferenceDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ReferenceEventCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ReferenceEventCode__listName', 'C', 256, 'AN'],
    [cbc+'ReferenceEventCode__name', 'C', 256, 'AN'],
    [cbc+'ReferenceEventCode__languageID', 'C', 256, 'AN'],
    [cbc+'ReferenceEventCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ReferenceEventCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ReferenceEventCode__listID', 'C', 256, 'AN'],
    [cbc+'ReferenceEventCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ReferenceEventCode__listURI', 'C', 256, 'AN'],
    [cbc+'ReferenceEventCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'ReferenceTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'ReferencedConsignmentID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ReferencedConsignmentID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ReferencedConsignmentID__schemeID', 'C', 256, 'AN'],
    [cbc+'ReferencedConsignmentID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ReferencedConsignmentID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ReferencedConsignmentID__schemeName', 'C', 256, 'AN'],
    [cbc+'ReferencedConsignmentID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ReferencedConsignmentID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'RefrigeratedIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'RefrigerationOnIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'Region':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Region__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Region__languageID', 'C', 256, 'AN'],
    ],
cbc+'RegistrationDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'RegistrationExpirationDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'RegistrationID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'RegistrationID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'RegistrationID__schemeID', 'C', 256, 'AN'],
    [cbc+'RegistrationID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'RegistrationID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'RegistrationID__schemeName', 'C', 256, 'AN'],
    [cbc+'RegistrationID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'RegistrationID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'RegistrationName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'RegistrationName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'RegistrationName__languageID', 'C', 256, 'AN'],
    ],
cbc+'RegistrationNationality':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'RegistrationNationality__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'RegistrationNationality__languageID', 'C', 256, 'AN'],
    ],
cbc+'RegistrationNationalityID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'RegistrationNationalityID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'RegistrationNationalityID__schemeID', 'C', 256, 'AN'],
    [cbc+'RegistrationNationalityID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'RegistrationNationalityID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'RegistrationNationalityID__schemeName', 'C', 256, 'AN'],
    [cbc+'RegistrationNationalityID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'RegistrationNationalityID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'RejectActionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'RejectActionCode__listName', 'C', 256, 'AN'],
    [cbc+'RejectActionCode__name', 'C', 256, 'AN'],
    [cbc+'RejectActionCode__languageID', 'C', 256, 'AN'],
    [cbc+'RejectActionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'RejectActionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'RejectActionCode__listID', 'C', 256, 'AN'],
    [cbc+'RejectActionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'RejectActionCode__listURI', 'C', 256, 'AN'],
    [cbc+'RejectActionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'RejectReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'RejectReason__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'RejectReason__languageID', 'C', 256, 'AN'],
    ],
cbc+'RejectReasonCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'RejectReasonCode__listName', 'C', 256, 'AN'],
    [cbc+'RejectReasonCode__name', 'C', 256, 'AN'],
    [cbc+'RejectReasonCode__languageID', 'C', 256, 'AN'],
    [cbc+'RejectReasonCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'RejectReasonCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'RejectReasonCode__listID', 'C', 256, 'AN'],
    [cbc+'RejectReasonCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'RejectReasonCode__listURI', 'C', 256, 'AN'],
    [cbc+'RejectReasonCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'RejectedQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'RejectedQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'RejectedQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'RejectedQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'RejectedQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'ReleaseID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ReleaseID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ReleaseID__schemeID', 'C', 256, 'AN'],
    [cbc+'ReleaseID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ReleaseID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ReleaseID__schemeName', 'C', 256, 'AN'],
    [cbc+'ReleaseID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ReleaseID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ReliabilityPercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'ReliabilityPercent__format', 'C', 256, 'AN'],
    ],
cbc+'Remarks':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Remarks__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Remarks__languageID', 'C', 256, 'AN'],
    ],
cbc+'RequestedDespatchDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'RequestedDespatchTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'RequiredCustomsID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'RequiredCustomsID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'RequiredCustomsID__schemeID', 'C', 256, 'AN'],
    [cbc+'RequiredCustomsID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'RequiredCustomsID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'RequiredCustomsID__schemeName', 'C', 256, 'AN'],
    [cbc+'RequiredCustomsID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'RequiredCustomsID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'RequiredDeliveryDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'RequiredDeliveryTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'ReturnabilityIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ReturnableMaterialIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ReturnableQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'ReturnableQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'ReturnableQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'ReturnableQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'ReturnableQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'Room':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Room__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Room__languageID', 'C', 256, 'AN'],
    ],
cbc+'RoundingAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'RoundingAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'RoundingAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'SalesOrderID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SalesOrderID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'SalesOrderID__schemeID', 'C', 256, 'AN'],
    [cbc+'SalesOrderID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'SalesOrderID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'SalesOrderID__schemeName', 'C', 256, 'AN'],
    [cbc+'SalesOrderID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'SalesOrderID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'SalesOrderLineID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SalesOrderLineID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'SalesOrderLineID__schemeID', 'C', 256, 'AN'],
    [cbc+'SalesOrderLineID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'SalesOrderLineID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'SalesOrderLineID__schemeName', 'C', 256, 'AN'],
    [cbc+'SalesOrderLineID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'SalesOrderLineID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'SealIssuerTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SealIssuerTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'SealIssuerTypeCode__name', 'C', 256, 'AN'],
    [cbc+'SealIssuerTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'SealIssuerTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'SealIssuerTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'SealIssuerTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'SealIssuerTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'SealIssuerTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'SealIssuerTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'SealStatusCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SealStatusCode__listName', 'C', 256, 'AN'],
    [cbc+'SealStatusCode__name', 'C', 256, 'AN'],
    [cbc+'SealStatusCode__languageID', 'C', 256, 'AN'],
    [cbc+'SealStatusCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'SealStatusCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'SealStatusCode__listID', 'C', 256, 'AN'],
    [cbc+'SealStatusCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'SealStatusCode__listURI', 'C', 256, 'AN'],
    [cbc+'SealStatusCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'SealingPartyType':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SealingPartyType__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'SealingPartyType__languageID', 'C', 256, 'AN'],
    ],
cbc+'SequenceID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SequenceID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'SequenceID__schemeID', 'C', 256, 'AN'],
    [cbc+'SequenceID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'SequenceID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'SequenceID__schemeName', 'C', 256, 'AN'],
    [cbc+'SequenceID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'SequenceID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'SequenceNumberID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SequenceNumberID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'SequenceNumberID__schemeID', 'C', 256, 'AN'],
    [cbc+'SequenceNumberID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'SequenceNumberID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'SequenceNumberID__schemeName', 'C', 256, 'AN'],
    [cbc+'SequenceNumberID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'SequenceNumberID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'SequenceNumeric':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'SequenceNumeric__format', 'C', 256, 'AN'],
    ],
cbc+'SerialID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SerialID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'SerialID__schemeID', 'C', 256, 'AN'],
    [cbc+'SerialID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'SerialID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'SerialID__schemeName', 'C', 256, 'AN'],
    [cbc+'SerialID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'SerialID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ServiceType':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ServiceType__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ServiceType__languageID', 'C', 256, 'AN'],
    ],
cbc+'ServiceTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ServiceTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'ServiceTypeCode__name', 'C', 256, 'AN'],
    [cbc+'ServiceTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'ServiceTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ServiceTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ServiceTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'ServiceTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ServiceTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'ServiceTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'SettlementDiscountAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SettlementDiscountAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'SettlementDiscountAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'SettlementDiscountPercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'SettlementDiscountPercent__format', 'C', 256, 'AN'],
    ],
cbc+'ShippingMarks':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ShippingMarks__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ShippingMarks__languageID', 'C', 256, 'AN'],
    ],
cbc+'ShippingPriorityLevelCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ShippingPriorityLevelCode__listName', 'C', 256, 'AN'],
    [cbc+'ShippingPriorityLevelCode__name', 'C', 256, 'AN'],
    [cbc+'ShippingPriorityLevelCode__languageID', 'C', 256, 'AN'],
    [cbc+'ShippingPriorityLevelCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ShippingPriorityLevelCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ShippingPriorityLevelCode__listID', 'C', 256, 'AN'],
    [cbc+'ShippingPriorityLevelCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ShippingPriorityLevelCode__listURI', 'C', 256, 'AN'],
    [cbc+'ShippingPriorityLevelCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'ShipsRequirements':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ShipsRequirements__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ShipsRequirements__languageID', 'C', 256, 'AN'],
    ],
cbc+'ShortQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'ShortQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'ShortQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'ShortQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'ShortQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'ShortageActionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ShortageActionCode__listName', 'C', 256, 'AN'],
    [cbc+'ShortageActionCode__name', 'C', 256, 'AN'],
    [cbc+'ShortageActionCode__languageID', 'C', 256, 'AN'],
    [cbc+'ShortageActionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ShortageActionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ShortageActionCode__listID', 'C', 256, 'AN'],
    [cbc+'ShortageActionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ShortageActionCode__listURI', 'C', 256, 'AN'],
    [cbc+'ShortageActionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'SignatureID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SignatureID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'SignatureID__schemeID', 'C', 256, 'AN'],
    [cbc+'SignatureID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'SignatureID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'SignatureID__schemeName', 'C', 256, 'AN'],
    [cbc+'SignatureID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'SignatureID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'SignatureMethod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SignatureMethod__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'SignatureMethod__languageID', 'C', 256, 'AN'],
    ],
cbc+'SizeTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SizeTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'SizeTypeCode__name', 'C', 256, 'AN'],
    [cbc+'SizeTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'SizeTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'SizeTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'SizeTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'SizeTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'SizeTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'SizeTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'SoleProprietorshipIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'SourceCurrencyBaseRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'SourceCurrencyBaseRate__format', 'C', 256, 'AN'],
    ],
cbc+'SourceCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SourceCurrencyCode__listName', 'C', 256, 'AN'],
    [cbc+'SourceCurrencyCode__name', 'C', 256, 'AN'],
    [cbc+'SourceCurrencyCode__languageID', 'C', 256, 'AN'],
    [cbc+'SourceCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'SourceCurrencyCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'SourceCurrencyCode__listID', 'C', 256, 'AN'],
    [cbc+'SourceCurrencyCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'SourceCurrencyCode__listURI', 'C', 256, 'AN'],
    [cbc+'SourceCurrencyCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'SpecialInstructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SpecialInstructions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'SpecialInstructions__languageID', 'C', 256, 'AN'],
    ],
cbc+'SpecialSecurityIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'SpecialServiceInstructions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SpecialServiceInstructions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'SpecialServiceInstructions__languageID', 'C', 256, 'AN'],
    ],
cbc+'SpecialTerms':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SpecialTerms__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'SpecialTerms__languageID', 'C', 256, 'AN'],
    ],
cbc+'SpecialTransportRequirements':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SpecialTransportRequirements__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'SpecialTransportRequirements__languageID', 'C', 256, 'AN'],
    ],
cbc+'SplitConsignmentIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'StartDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'StartTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'StatusCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'StatusCode__listName', 'C', 256, 'AN'],
    [cbc+'StatusCode__name', 'C', 256, 'AN'],
    [cbc+'StatusCode__languageID', 'C', 256, 'AN'],
    [cbc+'StatusCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'StatusCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'StatusCode__listID', 'C', 256, 'AN'],
    [cbc+'StatusCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'StatusCode__listURI', 'C', 256, 'AN'],
    [cbc+'StatusCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'StatusReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'StatusReason__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'StatusReason__languageID', 'C', 256, 'AN'],
    ],
cbc+'StatusReasonCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'StatusReasonCode__listName', 'C', 256, 'AN'],
    [cbc+'StatusReasonCode__name', 'C', 256, 'AN'],
    [cbc+'StatusReasonCode__languageID', 'C', 256, 'AN'],
    [cbc+'StatusReasonCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'StatusReasonCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'StatusReasonCode__listID', 'C', 256, 'AN'],
    [cbc+'StatusReasonCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'StatusReasonCode__listURI', 'C', 256, 'AN'],
    [cbc+'StatusReasonCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'StreetName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'StreetName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'StreetName__languageID', 'C', 256, 'AN'],
    ],
cbc+'SuccessiveSequenceID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SuccessiveSequenceID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'SuccessiveSequenceID__schemeID', 'C', 256, 'AN'],
    [cbc+'SuccessiveSequenceID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'SuccessiveSequenceID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'SuccessiveSequenceID__schemeName', 'C', 256, 'AN'],
    [cbc+'SuccessiveSequenceID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'SuccessiveSequenceID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'SummaryDescription':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SummaryDescription__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'SummaryDescription__languageID', 'C', 256, 'AN'],
    ],
cbc+'SupplierAssignedAccountID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'SupplierAssignedAccountID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'SupplierAssignedAccountID__schemeID', 'C', 256, 'AN'],
    [cbc+'SupplierAssignedAccountID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'SupplierAssignedAccountID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'SupplierAssignedAccountID__schemeName', 'C', 256, 'AN'],
    [cbc+'SupplierAssignedAccountID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'SupplierAssignedAccountID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'TareWeightMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TareWeightMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'TareWeightMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'TargetCurrencyBaseRate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'TargetCurrencyBaseRate__format', 'C', 256, 'AN'],
    ],
cbc+'TargetCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TargetCurrencyCode__listName', 'C', 256, 'AN'],
    [cbc+'TargetCurrencyCode__name', 'C', 256, 'AN'],
    [cbc+'TargetCurrencyCode__languageID', 'C', 256, 'AN'],
    [cbc+'TargetCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TargetCurrencyCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TargetCurrencyCode__listID', 'C', 256, 'AN'],
    [cbc+'TargetCurrencyCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TargetCurrencyCode__listURI', 'C', 256, 'AN'],
    [cbc+'TargetCurrencyCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TariffClassCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TariffClassCode__listName', 'C', 256, 'AN'],
    [cbc+'TariffClassCode__name', 'C', 256, 'AN'],
    [cbc+'TariffClassCode__languageID', 'C', 256, 'AN'],
    [cbc+'TariffClassCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TariffClassCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TariffClassCode__listID', 'C', 256, 'AN'],
    [cbc+'TariffClassCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TariffClassCode__listURI', 'C', 256, 'AN'],
    [cbc+'TariffClassCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TariffCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TariffCode__listName', 'C', 256, 'AN'],
    [cbc+'TariffCode__name', 'C', 256, 'AN'],
    [cbc+'TariffCode__languageID', 'C', 256, 'AN'],
    [cbc+'TariffCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TariffCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TariffCode__listID', 'C', 256, 'AN'],
    [cbc+'TariffCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TariffCode__listURI', 'C', 256, 'AN'],
    [cbc+'TariffCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TariffDescription':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TariffDescription__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'TariffDescription__languageID', 'C', 256, 'AN'],
    ],
cbc+'TaxAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TaxAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'TaxAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'TaxCurrencyCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TaxCurrencyCode__listName', 'C', 256, 'AN'],
    [cbc+'TaxCurrencyCode__name', 'C', 256, 'AN'],
    [cbc+'TaxCurrencyCode__languageID', 'C', 256, 'AN'],
    [cbc+'TaxCurrencyCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TaxCurrencyCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TaxCurrencyCode__listID', 'C', 256, 'AN'],
    [cbc+'TaxCurrencyCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TaxCurrencyCode__listURI', 'C', 256, 'AN'],
    [cbc+'TaxCurrencyCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TaxEvidenceIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'TaxExclusiveAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TaxExclusiveAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'TaxExclusiveAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'TaxExemptionReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TaxExemptionReason__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'TaxExemptionReason__languageID', 'C', 256, 'AN'],
    ],
cbc+'TaxExemptionReasonCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TaxExemptionReasonCode__listName', 'C', 256, 'AN'],
    [cbc+'TaxExemptionReasonCode__name', 'C', 256, 'AN'],
    [cbc+'TaxExemptionReasonCode__languageID', 'C', 256, 'AN'],
    [cbc+'TaxExemptionReasonCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TaxExemptionReasonCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TaxExemptionReasonCode__listID', 'C', 256, 'AN'],
    [cbc+'TaxExemptionReasonCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TaxExemptionReasonCode__listURI', 'C', 256, 'AN'],
    [cbc+'TaxExemptionReasonCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TaxIncludedIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'TaxInclusiveAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TaxInclusiveAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'TaxInclusiveAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'TaxLevelCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TaxLevelCode__listName', 'C', 256, 'AN'],
    [cbc+'TaxLevelCode__name', 'C', 256, 'AN'],
    [cbc+'TaxLevelCode__languageID', 'C', 256, 'AN'],
    [cbc+'TaxLevelCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TaxLevelCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TaxLevelCode__listID', 'C', 256, 'AN'],
    [cbc+'TaxLevelCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TaxLevelCode__listURI', 'C', 256, 'AN'],
    [cbc+'TaxLevelCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TaxPointDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'TaxTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TaxTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'TaxTypeCode__name', 'C', 256, 'AN'],
    [cbc+'TaxTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'TaxTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TaxTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TaxTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'TaxTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TaxTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'TaxTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TaxableAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TaxableAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'TaxableAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'TechnicalName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TechnicalName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'TechnicalName__languageID', 'C', 256, 'AN'],
    ],
cbc+'Telefax':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Telefax__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Telefax__languageID', 'C', 256, 'AN'],
    ],
cbc+'Telephone':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Telephone__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Telephone__languageID', 'C', 256, 'AN'],
    ],
cbc+'TestMethod':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TestMethod__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'TestMethod__languageID', 'C', 256, 'AN'],
    ],
cbc+'Text':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Text__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Text__languageID', 'C', 256, 'AN'],
    ],
cbc+'ThirdPartyPayerIndicator':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'TierRange':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TierRange__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'TierRange__languageID', 'C', 256, 'AN'],
    ],
cbc+'TierRatePercent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'TierRatePercent__format', 'C', 256, 'AN'],
    ],
cbc+'TimezoneOffset':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TimezoneOffset__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'TimezoneOffset__languageID', 'C', 256, 'AN'],
    ],
cbc+'TimingComplaint':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TimingComplaint__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'TimingComplaint__languageID', 'C', 256, 'AN'],
    ],
cbc+'TimingComplaintCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TimingComplaintCode__listName', 'C', 256, 'AN'],
    [cbc+'TimingComplaintCode__name', 'C', 256, 'AN'],
    [cbc+'TimingComplaintCode__languageID', 'C', 256, 'AN'],
    [cbc+'TimingComplaintCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TimingComplaintCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TimingComplaintCode__listID', 'C', 256, 'AN'],
    [cbc+'TimingComplaintCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TimingComplaintCode__listURI', 'C', 256, 'AN'],
    [cbc+'TimingComplaintCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'Title':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Title__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Title__languageID', 'C', 256, 'AN'],
    ],
cbc+'TotalGoodsItemQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'TotalGoodsItemQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'TotalGoodsItemQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'TotalGoodsItemQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'TotalGoodsItemQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'TotalInvoiceAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TotalInvoiceAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'TotalInvoiceAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'TotalPackageQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'TotalPackageQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'TotalPackageQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'TotalPackageQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'TotalPackageQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'TotalPackagesQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'TotalPackagesQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'TotalPackagesQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'TotalPackagesQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'TotalPackagesQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'TotalTransportHandlingUnitQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'TotalTransportHandlingUnitQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'TotalTransportHandlingUnitQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'TotalTransportHandlingUnitQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'TotalTransportHandlingUnitQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'TraceID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TraceID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'TraceID__schemeID', 'C', 256, 'AN'],
    [cbc+'TraceID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'TraceID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'TraceID__schemeName', 'C', 256, 'AN'],
    [cbc+'TraceID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'TraceID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'TrackingDeviceCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TrackingDeviceCode__listName', 'C', 256, 'AN'],
    [cbc+'TrackingDeviceCode__name', 'C', 256, 'AN'],
    [cbc+'TrackingDeviceCode__languageID', 'C', 256, 'AN'],
    [cbc+'TrackingDeviceCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TrackingDeviceCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TrackingDeviceCode__listID', 'C', 256, 'AN'],
    [cbc+'TrackingDeviceCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TrackingDeviceCode__listURI', 'C', 256, 'AN'],
    [cbc+'TrackingDeviceCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TrackingID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TrackingID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'TrackingID__schemeID', 'C', 256, 'AN'],
    [cbc+'TrackingID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'TrackingID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'TrackingID__schemeName', 'C', 256, 'AN'],
    [cbc+'TrackingID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'TrackingID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'TradeServiceCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TradeServiceCode__listName', 'C', 256, 'AN'],
    [cbc+'TradeServiceCode__name', 'C', 256, 'AN'],
    [cbc+'TradeServiceCode__languageID', 'C', 256, 'AN'],
    [cbc+'TradeServiceCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TradeServiceCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TradeServiceCode__listID', 'C', 256, 'AN'],
    [cbc+'TradeServiceCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TradeServiceCode__listURI', 'C', 256, 'AN'],
    [cbc+'TradeServiceCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TradingRestrictions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TradingRestrictions__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'TradingRestrictions__languageID', 'C', 256, 'AN'],
    ],
cbc+'TrainID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TrainID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'TrainID__schemeID', 'C', 256, 'AN'],
    [cbc+'TrainID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'TrainID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'TrainID__schemeName', 'C', 256, 'AN'],
    [cbc+'TrainID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'TrainID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'TransactionCurrencyTaxAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransactionCurrencyTaxAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'TransactionCurrencyTaxAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'TransitDirectionCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransitDirectionCode__listName', 'C', 256, 'AN'],
    [cbc+'TransitDirectionCode__name', 'C', 256, 'AN'],
    [cbc+'TransitDirectionCode__languageID', 'C', 256, 'AN'],
    [cbc+'TransitDirectionCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TransitDirectionCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TransitDirectionCode__listID', 'C', 256, 'AN'],
    [cbc+'TransitDirectionCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TransitDirectionCode__listURI', 'C', 256, 'AN'],
    [cbc+'TransitDirectionCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TransportAuthorizationCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransportAuthorizationCode__listName', 'C', 256, 'AN'],
    [cbc+'TransportAuthorizationCode__name', 'C', 256, 'AN'],
    [cbc+'TransportAuthorizationCode__languageID', 'C', 256, 'AN'],
    [cbc+'TransportAuthorizationCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TransportAuthorizationCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TransportAuthorizationCode__listID', 'C', 256, 'AN'],
    [cbc+'TransportAuthorizationCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TransportAuthorizationCode__listURI', 'C', 256, 'AN'],
    [cbc+'TransportAuthorizationCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TransportEmergencyCardCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransportEmergencyCardCode__listName', 'C', 256, 'AN'],
    [cbc+'TransportEmergencyCardCode__name', 'C', 256, 'AN'],
    [cbc+'TransportEmergencyCardCode__languageID', 'C', 256, 'AN'],
    [cbc+'TransportEmergencyCardCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TransportEmergencyCardCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TransportEmergencyCardCode__listID', 'C', 256, 'AN'],
    [cbc+'TransportEmergencyCardCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TransportEmergencyCardCode__listURI', 'C', 256, 'AN'],
    [cbc+'TransportEmergencyCardCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TransportEquipmentTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransportEquipmentTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'TransportEquipmentTypeCode__name', 'C', 256, 'AN'],
    [cbc+'TransportEquipmentTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'TransportEquipmentTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TransportEquipmentTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TransportEquipmentTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'TransportEquipmentTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TransportEquipmentTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'TransportEquipmentTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TransportEventTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransportEventTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'TransportEventTypeCode__name', 'C', 256, 'AN'],
    [cbc+'TransportEventTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'TransportEventTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TransportEventTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TransportEventTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'TransportEventTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TransportEventTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'TransportEventTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TransportHandlingUnitTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransportHandlingUnitTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'TransportHandlingUnitTypeCode__name', 'C', 256, 'AN'],
    [cbc+'TransportHandlingUnitTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'TransportHandlingUnitTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TransportHandlingUnitTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TransportHandlingUnitTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'TransportHandlingUnitTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TransportHandlingUnitTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'TransportHandlingUnitTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TransportMeansTypeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransportMeansTypeCode__listName', 'C', 256, 'AN'],
    [cbc+'TransportMeansTypeCode__name', 'C', 256, 'AN'],
    [cbc+'TransportMeansTypeCode__languageID', 'C', 256, 'AN'],
    [cbc+'TransportMeansTypeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TransportMeansTypeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TransportMeansTypeCode__listID', 'C', 256, 'AN'],
    [cbc+'TransportMeansTypeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TransportMeansTypeCode__listURI', 'C', 256, 'AN'],
    [cbc+'TransportMeansTypeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TransportModeCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransportModeCode__listName', 'C', 256, 'AN'],
    [cbc+'TransportModeCode__name', 'C', 256, 'AN'],
    [cbc+'TransportModeCode__languageID', 'C', 256, 'AN'],
    [cbc+'TransportModeCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TransportModeCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TransportModeCode__listID', 'C', 256, 'AN'],
    [cbc+'TransportModeCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TransportModeCode__listURI', 'C', 256, 'AN'],
    [cbc+'TransportModeCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TransportServiceCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransportServiceCode__listName', 'C', 256, 'AN'],
    [cbc+'TransportServiceCode__name', 'C', 256, 'AN'],
    [cbc+'TransportServiceCode__languageID', 'C', 256, 'AN'],
    [cbc+'TransportServiceCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'TransportServiceCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'TransportServiceCode__listID', 'C', 256, 'AN'],
    [cbc+'TransportServiceCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'TransportServiceCode__listURI', 'C', 256, 'AN'],
    [cbc+'TransportServiceCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'TransportationServiceDescription':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransportationServiceDescription__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'TransportationServiceDescription__languageID', 'C', 256, 'AN'],
    ],
cbc+'TransportationServiceDetailsURI':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'TransportationServiceDetailsURI__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'TransportationServiceDetailsURI__schemeID', 'C', 256, 'AN'],
    [cbc+'TransportationServiceDetailsURI__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'TransportationServiceDetailsURI__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'TransportationServiceDetailsURI__schemeName', 'C', 256, 'AN'],
    [cbc+'TransportationServiceDetailsURI__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'TransportationServiceDetailsURI__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'UBLVersionID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'UBLVersionID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'UBLVersionID__schemeID', 'C', 256, 'AN'],
    [cbc+'UBLVersionID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'UBLVersionID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'UBLVersionID__schemeName', 'C', 256, 'AN'],
    [cbc+'UBLVersionID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'UBLVersionID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'UNDGCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'UNDGCode__listName', 'C', 256, 'AN'],
    [cbc+'UNDGCode__name', 'C', 256, 'AN'],
    [cbc+'UNDGCode__languageID', 'C', 256, 'AN'],
    [cbc+'UNDGCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'UNDGCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'UNDGCode__listID', 'C', 256, 'AN'],
    [cbc+'UNDGCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'UNDGCode__listURI', 'C', 256, 'AN'],
    [cbc+'UNDGCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'URI':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'URI__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'URI__schemeID', 'C', 256, 'AN'],
    [cbc+'URI__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'URI__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'URI__schemeName', 'C', 256, 'AN'],
    [cbc+'URI__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'URI__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'UUID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'UUID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'UUID__schemeID', 'C', 256, 'AN'],
    [cbc+'UUID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'UUID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'UUID__schemeName', 'C', 256, 'AN'],
    [cbc+'UUID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'UUID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'UpperOrangeHazardPlacardID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'UpperOrangeHazardPlacardID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'UpperOrangeHazardPlacardID__schemeID', 'C', 256, 'AN'],
    [cbc+'UpperOrangeHazardPlacardID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'UpperOrangeHazardPlacardID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'UpperOrangeHazardPlacardID__schemeName', 'C', 256, 'AN'],
    [cbc+'UpperOrangeHazardPlacardID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'UpperOrangeHazardPlacardID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ValidateProcess':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ValidateProcess__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ValidateProcess__languageID', 'C', 256, 'AN'],
    ],
cbc+'ValidateTool':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ValidateTool__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ValidateTool__languageID', 'C', 256, 'AN'],
    ],
cbc+'ValidateToolVersion':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ValidateToolVersion__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ValidateToolVersion__languageID', 'C', 256, 'AN'],
    ],
cbc+'ValidationDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'ValidationResultCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ValidationResultCode__listName', 'C', 256, 'AN'],
    [cbc+'ValidationResultCode__name', 'C', 256, 'AN'],
    [cbc+'ValidationResultCode__languageID', 'C', 256, 'AN'],
    [cbc+'ValidationResultCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'ValidationResultCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'ValidationResultCode__listID', 'C', 256, 'AN'],
    [cbc+'ValidationResultCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'ValidationResultCode__listURI', 'C', 256, 'AN'],
    [cbc+'ValidationResultCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'ValidationTime':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'T'],
    ],
cbc+'ValidatorID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ValidatorID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'ValidatorID__schemeID', 'C', 256, 'AN'],
    [cbc+'ValidatorID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'ValidatorID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'ValidatorID__schemeName', 'C', 256, 'AN'],
    [cbc+'ValidatorID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'ValidatorID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'ValidityStartDate':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
cbc+'Value':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'Value__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'Value__languageID', 'C', 256, 'AN'],
    ],
cbc+'ValueAmount':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ValueAmount__currencyID', 'C', 256, 'AN'],
    [cbc+'ValueAmount__currencyCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'ValueMeasure':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ValueMeasure__unitCode', 'C', 256, 'AN'],
    [cbc+'ValueMeasure__unitCodeListVersionID', 'C', 256, 'AN'],
    ],
cbc+'ValueQualifier':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'ValueQualifier__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'ValueQualifier__languageID', 'C', 256, 'AN'],
    ],
cbc+'ValueQuantity':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'R'],
    [cbc+'ValueQuantity__unitCode', 'C', 256, 'AN'],
    [cbc+'ValueQuantity__unitCodeListAgencyName', 'C', 256, 'AN'],
    [cbc+'ValueQuantity__unitCodeListID', 'C', 256, 'AN'],
    [cbc+'ValueQuantity__unitCodeListAgencyID', 'C', 256, 'AN'],
    ],
cbc+'VersionID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'VersionID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'VersionID__schemeID', 'C', 256, 'AN'],
    [cbc+'VersionID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'VersionID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'VersionID__schemeName', 'C', 256, 'AN'],
    [cbc+'VersionID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'VersionID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'VesselID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'VesselID__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'VesselID__schemeID', 'C', 256, 'AN'],
    [cbc+'VesselID__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'VesselID__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'VesselID__schemeName', 'C', 256, 'AN'],
    [cbc+'VesselID__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'VesselID__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'VesselName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'VesselName__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'VesselName__languageID', 'C', 256, 'AN'],
    ],
cbc+'WebsiteURI':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'WebsiteURI__schemeDataURI', 'C', 256, 'AN'],
    [cbc+'WebsiteURI__schemeID', 'C', 256, 'AN'],
    [cbc+'WebsiteURI__schemeAgencyName', 'C', 256, 'AN'],
    [cbc+'WebsiteURI__schemeAgencyID', 'C', 256, 'AN'],
    [cbc+'WebsiteURI__schemeName', 'C', 256, 'AN'],
    [cbc+'WebsiteURI__schemeVersionID', 'C', 256, 'AN'],
    [cbc+'WebsiteURI__schemeURI', 'C', 256, 'AN'],
    ],
cbc+'WeekDayCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'WeekDayCode__listName', 'C', 256, 'AN'],
    [cbc+'WeekDayCode__name', 'C', 256, 'AN'],
    [cbc+'WeekDayCode__languageID', 'C', 256, 'AN'],
    [cbc+'WeekDayCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'WeekDayCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'WeekDayCode__listID', 'C', 256, 'AN'],
    [cbc+'WeekDayCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'WeekDayCode__listURI', 'C', 256, 'AN'],
    [cbc+'WeekDayCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'WorkPhase':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'WorkPhase__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'WorkPhase__languageID', 'C', 256, 'AN'],
    ],
cbc+'WorkPhaseCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'WorkPhaseCode__listName', 'C', 256, 'AN'],
    [cbc+'WorkPhaseCode__name', 'C', 256, 'AN'],
    [cbc+'WorkPhaseCode__languageID', 'C', 256, 'AN'],
    [cbc+'WorkPhaseCode__listAgencyID', 'C', 256, 'AN'],
    [cbc+'WorkPhaseCode__listSchemeURI', 'C', 256, 'AN'],
    [cbc+'WorkPhaseCode__listID', 'C', 256, 'AN'],
    [cbc+'WorkPhaseCode__listAgencyName', 'C', 256, 'AN'],
    [cbc+'WorkPhaseCode__listURI', 'C', 256, 'AN'],
    [cbc+'WorkPhaseCode__listVersionID', 'C', 256, 'AN'],
    ],
cbc+'XPath':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [cbc+'XPath__languageLocaleID', 'C', 256, 'AN'],
    [cbc+'XPath__languageID', 'C', 256, 'AN'],
    ],
ext+'ExtensionAgencyID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ext+'ExtensionAgencyID__schemeDataURI', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyID__schemeID', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyID__schemeAgencyName', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyID__schemeAgencyID', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyID__schemeName', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyID__schemeVersionID', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyID__schemeURI', 'C', 256, 'AN'],
    ],
ext+'ExtensionAgencyName':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ext+'ExtensionAgencyName__languageLocaleID', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyName__languageID', 'C', 256, 'AN'],
    ],
ext+'ExtensionAgencyURI':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ext+'ExtensionAgencyURI__schemeDataURI', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyURI__schemeID', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyURI__schemeAgencyName', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyURI__schemeAgencyID', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyURI__schemeName', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyURI__schemeVersionID', 'C', 256, 'AN'],
    [ext+'ExtensionAgencyURI__schemeURI', 'C', 256, 'AN'],
    ],
ext+'ExtensionContent':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ext+'ExtensionReason':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ext+'ExtensionReason__languageLocaleID', 'C', 256, 'AN'],
    [ext+'ExtensionReason__languageID', 'C', 256, 'AN'],
    ],
ext+'ExtensionReasonCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ext+'ExtensionReasonCode__listName', 'C', 256, 'AN'],
    [ext+'ExtensionReasonCode__name', 'C', 256, 'AN'],
    [ext+'ExtensionReasonCode__languageID', 'C', 256, 'AN'],
    [ext+'ExtensionReasonCode__listAgencyID', 'C', 256, 'AN'],
    [ext+'ExtensionReasonCode__listSchemeURI', 'C', 256, 'AN'],
    [ext+'ExtensionReasonCode__listID', 'C', 256, 'AN'],
    [ext+'ExtensionReasonCode__listAgencyName', 'C', 256, 'AN'],
    [ext+'ExtensionReasonCode__listURI', 'C', 256, 'AN'],
    [ext+'ExtensionReasonCode__listVersionID', 'C', 256, 'AN'],
    ],
ext+'ExtensionURI':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ext+'ExtensionURI__schemeDataURI', 'C', 256, 'AN'],
    [ext+'ExtensionURI__schemeID', 'C', 256, 'AN'],
    [ext+'ExtensionURI__schemeAgencyName', 'C', 256, 'AN'],
    [ext+'ExtensionURI__schemeAgencyID', 'C', 256, 'AN'],
    [ext+'ExtensionURI__schemeName', 'C', 256, 'AN'],
    [ext+'ExtensionURI__schemeVersionID', 'C', 256, 'AN'],
    [ext+'ExtensionURI__schemeURI', 'C', 256, 'AN'],
    ],
ext+'ExtensionVersionID':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    [ext+'ExtensionVersionID__schemeDataURI', 'C', 256, 'AN'],
    [ext+'ExtensionVersionID__schemeID', 'C', 256, 'AN'],
    [ext+'ExtensionVersionID__schemeAgencyName', 'C', 256, 'AN'],
    [ext+'ExtensionVersionID__schemeAgencyID', 'C', 256, 'AN'],
    [ext+'ExtensionVersionID__schemeName', 'C', 256, 'AN'],
    [ext+'ExtensionVersionID__schemeVersionID', 'C', 256, 'AN'],
    [ext+'ExtensionVersionID__schemeURI', 'C', 256, 'AN'],
    ],
ext+'UBLExtension':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
ext+'UBLExtensions':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
xmlns+'Invoice':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ],
xmlns+'CategoryCode':
    [
    ['BOTSID', 'M', 256, 'AN'],
    ['BOTSCONTENT', 'M', 256, 'AN'],
    ],
}
