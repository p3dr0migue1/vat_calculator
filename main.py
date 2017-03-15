#!/usr/bin/env python
import argparse

from core.calculator import main


if __name__ == '__main__':
    # I wasn't sure what to do if a argument had not been passed by the
    # user, so I decided to make all arguments required
    parser = argparse.ArgumentParser()
    required_args = parser.add_argument_group('required named arguments')

    required_args.add_argument('-p',
                               '--product',
                               help='Product name',
                               required=True)

    required_args.add_argument('-pr',
                               '--price',
                               help='Product price',
                               required=True,
                               type=float)

    required_args.add_argument('-c',
                               '--country',
                               help='Country name',
                               required=True)

    args = parser.parse_args()
    print main(args.product, args.price, args.country)
