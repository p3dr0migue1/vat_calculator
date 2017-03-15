# -*- coding: utf-8 -*-


ten_percent = 1.10
tweenty_percent = 1.20


class EUvat(object):
    special_vat = {
        'Bread': 1.125
    }
    non_taxable = {
        'Bread': 0.05
    }


class GERMANYvat(object):
    u"""
    - Germany, like in EU, but also:
        The base VAT changes to 15%
        For bread, like in EU, but the first €1.00 is tax-free
        For wine, the VAT is 20%
    """

    base_vat = 1.15
    products_vat = {'Wine': tweenty_percent}
    special_vat = {
        'Bread': 1.125
    }
    non_taxable = {
        'Bread': 1.0
    }

    @classmethod
    def get_vat(cls, item, price):
        if item in cls.special_vat:
            taxable = (float(price) - cls.non_taxable[item])
            gross = round(taxable * cls.special_vat[item], 2)
            vat = round(gross - taxable, 2)
            return vat

        if item in cls.products_vat:
            gross = round(price * cls.products_vat[item], 2)
            vat = round(gross - price, 2)
            return vat
        else:
            gross = round(price * cls.base_vat, 2)
            vat = round(float(gross) - float(price), 2)
            return vat


class UKvat(EUvat):
    u"""
    UK, like in EU, but also:
        For first £20 the VAT is like in EU
        For the next £80, the VAT is 15%
        For the rest, it's 20%
        For wine, the VAT is 10%, regardless of price
    """

    # I've assumed that further rules would be simple enough to
    # be added using the following dict structure.
    #
    # Additionally I could have refactored these methods to be called
    # and overwritten from the parent class.
    products_vat = {'Wine': ten_percent}

    @classmethod
    def get_vat(cls, item, price):
        if item in cls.special_vat:
            taxable = price - cls.non_taxable[item]
            gross = round(taxable * cls.special_vat[item], 2)
            vat = round(gross - taxable, 2)
            return vat

        if item in cls.products_vat:
            gross = round(price * cls.products_vat[item], 2)
            vat = round(gross - price, 2)
            return vat
        else:
            if price <= 20:
                gross = round(price * 1.125, 2)
            elif price <= 80:
                gross = round(price * 1.15, 2)
            else:
                gross = round(price * 1.20, 2)
            vat = round(gross - price, 2)
            return vat


class VATRules(object):
    rules = {
        'UK': UKvat,
        'Germany': GERMANYvat,
    }

    @classmethod
    def get_country_rules(cls, country):
        # Could not really understand what to do if the country is
        # not listed so, I decided just to return a list of the
        # available countries to the user
        if country in cls.rules:
            return cls.rules[country]
        else:
            return cls.rules.keys()
