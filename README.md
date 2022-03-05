# UBLCII

Translate Invoice UBL 2.1 to/from CrossIndustryInvoice (CII) D16B


## Installation

* Pre-required: python2 or python3
* Additional-requirements: java (for invoicing rules validation)

```bash
pip install ublcii
```


## Usages
```bash
ubl2cii Input-Invoice-UBL.xml Output-Invoice-CII-D16B.xml
cii2ubl Input-Invoice-CII-D16B.xml Output-Invoice-UBL.xml
```

### With validation
```bash
ubl2cii --validate Input-Invoice-UBL.xml
ubl2cii --validate Input-Invoice-UBL.xml Output-Invoice-CII-D16B.xml
```


## Authors
* Ludovic Watteaux (Development)
* Claude Charmot (Specifications)


## Support

https://sourceforge.net/projects/converter-ubl-cii-invoice-xml/support


## Changelog

* v1.1.1: 2022.03.04
	* [cii2ubl] Fix BT-17: /Invoice /OriginatorDocumentReference /ID

* v1.1.0: 2022.01.20
	* [ubl2cii] BT-20 = "Avoir" if no BT-9 and no BT-20
	* Fix for fixed validation bug with [BT-110] TaxAmount
	* [ubl2cii] Fixes [BT-84] [BT-84-0] Add IBAN detection
	* Add map [BT-17],[BT-17-0], Fix [BT-18-0] and [BT-11-0]
	* [BT-18-2][BT-18-0] Added
	* [ubl2cii] remove email attribute ram:URIID@schemeID SMTP
	* [ubl2cii] Fix same PaymentReference, now appear only once
	* [ubl2cii] No more .../PayeePartyCreditorFinancialAccount /ProprietaryID
	* [ubl2cii] Only accept UBL type: Invoice & CreditNote
	* [cii2ubl] Raise exception if input xml is not a CrossIndustryInvoice
	* Add validation option: https://github.com/ConnectingEurope/eInvoicing-EN16931
	* Fix & clean error logs
	* Fixes: GlobalID, schemeID
		* BT-31, BT-32, BT-31-2
		* BT-48-2
		* BT-60-0, BT-60-1
		* BT-63-2
		* BT-71-1
		* BT-95-1, BT-102-1
	* Fix setup env for *nix
	* Fixes TaxCurrencyCode
	* Fixes and update mappings fields
	* [BT-8] code convertion ubl2005 <> cii2475
	* Fixes for BT-83 & BT-84
	* Add map if not IBANID:
		* CII: /PayeePartyCreditorFinancialAccount/ProprietaryID
		* UBL: /PaymentMeans/PayeeFinancialAccount/ID
	* UBL21 CreditNote added
	* Increase size of CII:AttachmentBinaryObject to 999999999
	* Increase size of UBL:EmbeddedDocumentBinaryObject to 999999999
	* map:BT-90 with @shemeID SEPA
	* map: BT-40-0 & rules for cii:{ram}DepartmentName  BT-56-0
	* Fixes: BT-128-1/2, [BR-CL-17] [UBL-CR-139] & Note SubjectCode
	* Add UBL /Invoice/Note with CII SubjectCode between #SubjectCode#
	* Fix [UBL-CR-203]
	* [ubl2cii] Fixes [CII-DT-031] currencyID should not be present
	* [cii2ubl] Fixes [BR-57] & [UBL-SR-24], PaymentDueDate
	* map: - /Invoice /PaymentMeans /PaymentDueDate
	* map: - /Invoice /TaxTotal /TaxSubtotal /TaxCategory /TaxScheme /TaxTypeCode
	* Fix [BR-57] & [UBL-SR-24] No more several occurence of /Invoice /Delivery
	* Fix BT-28 & BT-45 : CII/*/TradingBusinessName
	* Fixes DueDate, /Party Contact, CategoryCode and TypeCode
	* Update usage with in and out type in filename
	* Add validation option on input/output files
	* Update and fixes mapped fields with references BG-XX, BT-XX
	* [ubl2cii] Fix 'xmlns:qdt' namespace could appear twice
	* [cii2ubl] Last Fix of TaxCurrencyCode
	* [cii2ubl] Fix some default currency in ubl
	* Fix default curenncy for ubl fields
		* /Invoice /TaxTotal /TaxSubtotal /TaxableAmount /TaxableAmount__currencyID
		* /Invoice /TaxTotal /TaxSubtotal /TaxAmount /TaxAmount__currencyID
	* Fix /Invoice /LegalMonetaryTotal /TaxInclusiveAmount /TaxInclusiveAmount__currencyID
	* Map: /Invoice /InvoiceLine /Delivery /ActualDeliveryDate
	* [ubl2cii] skip null AllowangeChargeAmount, add schemeID='SMTP' attr to emails
	* Fix: /Invoice /PaymentMeans /PayeeFinancialAccount /FinancialInstitutionBranch /ID
	* Map: /Invoice /PaymentMeans /PaymentMeansCode__* attrs
	* Map: /Invoice /InvoicePeriod /Description
	* [cii2ubl] avoid empty attr <PaymentMeansCode name="">
	* Fix bad ns in ubl2cii and fixes for AllowanceCharge
	* Map: /Invoice /InvoicePeriod /DescriptionCode > .../DueDateTypeCode
	* Fix /Invoice /TaxPointDate for ubl2cii
	* Map /NetPriceProductTradePrice /BasisQuantity > InvoiceLine /Price /BaseQuantity
	* Fix for BusinessProcessSpecifiedDocumentContextParameter
	* Change mapped CII fields with IndicatorString to Indicator
		* for UBL /InvoiceLine /AllowanceCharge /ChargeIndicator
		* all CII fields with Indicator replace IndicatorString
	* Map /BusinessProcessSpecifiedDocumentContextParameter /ID
	* Map AllowanceCharge..TaxTypeCode > SpecifiedTradeAllowanceCharge..CategoryCode
	* Map cac:DespatchDocumentReference > ram:DespatchAdviceReferencedDocument
	* Add mappings rules for default currencyID from InvoiceCurrencyCode or 'EUR'
	* [UBL2CII] New map rule for CII /ProcuringProjectType /Name

* v1.0.3 : 2019-07-29 - Fixes and Updates
	* [CII2UBL] Fixes for /Invoice/Delivery/DeliveryLocation/ID
	* Add xml namespaces: qdt, udt, xsi, xsi:schemaLocation
	* [CII2UBL] Map /IncludedNote/SubjectCode in begin of /Invoice/Note
	* Increase xml D16B ram:Content len to 1024
	* Set minimum occurance of UBL /Invoice/InvoiceLine to 0

* v1.0.2 : 2019-07-23 - Fixes and Updates
	* Map field /Invoice/InvoiceLine/AllowanceCharge/ChargeIndicator
	* Set default mandatory field ChargeIndicator to 'false'
	* Fix /Invoice/PaymentMeans
	* Fix /Invoice/InvoiceLine/Price/AllowanceCharge/BaseAmount

* v1.0.1 : 2019-07-19 - Packaging infos updates

* v1.0.0 : 2019-07-18 - First release on pypi
