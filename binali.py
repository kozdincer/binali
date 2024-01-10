#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
from argparse import ArgumentParser
from binali_quotes import QUOTES as binaliQuotes

parser = ArgumentParser(description="Echoes well-known quotes from binali.")
# 29 is the index of "Binali feda olsun" quote.
parser.add_argument('--feda', action='store_const', const=29)
args = parser.parse_args()

if args.feda is not None:
	print(binaliQuotes[args.feda])
	print("modif")
else:
	print(random.choice(binaliQuotes))
