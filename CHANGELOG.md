# ublcii - CHANGELOG

## 1.1.2: 2023.02.04
* Fixes for UBL CreditNote: Add PaymentDueDate
* Fix CII /SpecifiedProcuringProject /ID
* [cii2ubl] Add /Invoice /PaymentMeans /CardAccount /NetworkID
* [cii2ubl] Fix for missing incoming cii //rsm:ExchangedDocument/ram:TypeCode
* [cii2ubl] Fix mapping of specifiedprocuringprojectid for CreditNote
* [eInvoicing-EN16931] Update to 2022-10-27

## 1.1.1: 2022.03.04
* [cii2ubl] Fix BT-17: /Invoice /OriginatorDocumentReference /ID

## 1.1.0: 2022.01.20
* [ubl2cii] BT-20 = "Avoir" if no BT-9 and no BT-20

## 1.1.0rc21: 2021.12.29
* Fix for fixed validation bug with [BT-110] TaxAmount

## 1.1.0rc20: 2021.12.23
* [ubl2cii] Fixes [BT-84] [BT-84-0] Add IBAN detection
* Add map [BT-17],[BT-17-0], Fix [BT-18-0] and [BT-11-0]

## 1.1.0rc19: 2021.10.14
* [BT-18-2][BT-18-0] Added
* [ubl2cii] remove email attribute ram:URIID@schemeID SMTP

## 1.1.0rc18: 2021.09.14
* [ubl2cii] Fix same PaymentReference, now appear only once
* [ubl2cii] No more .../PayeePartyCreditorFinancialAccount /ProprietaryID

## 1.1.0rc17: 2021.09.02
* [ubl2cii] Only accept UBL type: Invoice & CreditNote
* [cii2ubl] Raise exception if input xml is not a CrossIndustryInvoice
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
* Add validation option: UBL & CII: **v1.3.2** (2020-05-25) - https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.5

## 1.0.3 : 2019-07-29 - Fixes and Updates
* [CII2UBL] Fixes for /Invoice/Delivery/DeliveryLocation/ID
* Add xml namespaces: qdt, udt, xsi, xsi:schemaLocation
* [CII2UBL] Map /IncludedNote/SubjectCode in begin of /Invoice/Note
* Increase xml D16B ram:Content len to 1024
* Set minimum occurance of UBL /Invoice/InvoiceLine to 0

## 1.0.2 : 2019-07-23 - Fixes and Updates
* Map field /Invoice/InvoiceLine/AllowanceCharge/ChargeIndicator
* Set default mandatory field ChargeIndicator to 'false'
* Fix /Invoice/PaymentMeans
* Fix /Invoice/InvoiceLine/Price/AllowanceCharge/BaseAmount

## 1.0.1 : 2019-07-19 - Packaging infos updates

## 1.0.0 : 2019-07-18 - First release on pypi
