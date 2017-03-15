## VAT Calculator

A simple VAT calculator using the command line interface.



### Installation

To install this package create a virtualenv and run from the root directory:
`$ pip install -e .`

### Usage

```
python main.py --help
usage: main.py [-h] -p PRODUCT -pr PRICE -c COUNTRY

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  -p PRODUCT, --product PRODUCT
                        Product name
  -pr PRICE, --price PRICE
                        Product price
  -c COUNTRY, --country COUNTRY
                        Country name
```

Example:

```
$ python main.py -p='Bread' -pr=12.50 -c='UK'
Total VAT paid on Bread in UK was £1.56
```

### Run Tests

To run the tests run:

```
$ python -m unittest discover -s tests
```
