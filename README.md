# UBLCII

Translate Invoice UBL 2.1 to/from CrossIndustryInvoice (CII) D16B


## Installation

* Pre-required: python2 or python3

```bash
pip install ublcii
```


## Usages
```bash
ubl2cii Input-Invoice-UBL.xml Output-Invoice-CII-D16B.xml
cii2ubl Input-Invoice-CII-D16B.xml Output-Invoice-UBL.xml
```

## Authors
* Ludovic Watteaux (Development)
* Claude Charmot (Specifications)


## Support

https://sourceforge.net/projects/converter-ubl-cii-invoice-xml/support


## Changelog
* v1.0.2 : 2019-07-23 - Fixes and Updates
	* Map field /Invoice/InvoiceLine/AllowanceCharge/ChargeIndicator
	* Set default mandatory field ChargeIndicator to 'false'
	* Fix /Invoice/PaymentMeans
	* Fix /Invoice/InvoiceLine/Price/AllowanceCharge/BaseAmount

* v1.0.1 : 2019-07-19 - Packaging infos updates
* v1.0.0 : 2019-07-18 - First release on pypi
