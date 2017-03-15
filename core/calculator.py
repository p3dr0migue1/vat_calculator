# -*- coding: utf-8 -*-
from rules import VATRules


def main(product, price, country):
    rule = VATRules.get_country_rules(country)

    if isinstance(rule, list):
        print '{} is not currently listed.'.format(country)
        print 'Available countries are:'
        for country in rule:
            print country
    else:
        vat = rule.get_vat(product, price)
        return 'Total VAT paid on {} in {} was £{}'.format(
            product,
            country,
            vat
        )
