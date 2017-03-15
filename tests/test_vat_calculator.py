# -*- coding: utf-8 -*-
import unittest

from core.calculator import main


class TestVATCalculator(unittest.TestCase):
    def test_uk_vat_for_listed_product_with_special_vat_rule(self):

        product = 'Bread'
        price = 2.50
        country = 'UK'
        vat = 0.31
        expected = 'Total VAT paid on {} in {} was £{}'.format(
            product,
            country,
            vat
        )
        output = main(product, price, country)

        self.assertEqual(output, expected)

    def test_uk_vat_for_wine(self):
        product = 'Wine'
        price = 20
        country = 'UK'
        vat = 2.0
        expected = 'Total VAT paid on {} in {} was £{}'.format(
            product,
            country,
            vat
        )
        output = main(product, price, country)

        self.assertEqual(output, expected)

    def test_uk_vat_for_unlisted_product_tweenty_percent(self):
        product = 'Juices'
        price = 90
        country = 'UK'
        vat = 18.0
        expected = 'Total VAT paid on {} in {} was £{}'.format(
            product,
            country,
            vat
        )
        output = main(product, price, country)

        self.assertEqual(output, expected)

    def test_uk_vat_for_unlisted_product_fifteen_percent(self):
        product = 'Juices'
        price = 80
        country = 'UK'
        vat = 12.0
        expected = 'Total VAT paid on {} in {} was £{}'.format(
            product,
            country,
            vat
        )
        output = main(product, price, country)

        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
