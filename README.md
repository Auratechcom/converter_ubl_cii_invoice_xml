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


