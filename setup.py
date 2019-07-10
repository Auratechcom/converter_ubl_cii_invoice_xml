# -*- coding: utf-8 -*-

"""Setup for ubl <> cii translators

"""
import os
import setuptools


setup_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(setup_dir, 'ublcii', '__about__.py')) as f:
    exec(f.read(), about)

long_description = """Two way translator: Invoice UBL 2.1 <> Cross Invoice Industry D16B
"""

install_requires = [
    'setuptools',
    'django>=1.10',
    'bots-ediint>=3.3.1rc1',
]

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Topic :: Office/Business',
    'Topic :: Office/Business :: Financial',
    'Topic :: Other/Nonlisted Topic',
    'Topic :: Communications',
    'Environment :: Console',
    'Environment :: Web Environment',
]

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__email__'],
    long_description=long_description,
    platforms='OS Independent (Written in an interpreted language)',
    license=about['__license__'],
    keywords='edi xml invoice ubl 2.1 CII CrossIndustryInvoice D16B',
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=classifiers,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'ublcii-clean = ublcii:clean',
            'ubl2cii = ublcii.translate:ubl2cii',
            'cii2ubl = ublcii.translate:cii2ubl',
        ]
    },
    project_urls={
        'Home': about['__url__'],
        'Bug Reports': 'https://github.com/Auratechcom/converter_ubl_cii_invoice_xml/issues',
        'Say Thanks!': 'http://www.auratechcom.fr/contact.htm',
        'Say Thanks2!': 'https://www.edi-intelligentsia.com/contact/',
        'Source': 'https://github.com/Auratechcom/converter_ubl_cii_invoice_xml.git',
    },
)
