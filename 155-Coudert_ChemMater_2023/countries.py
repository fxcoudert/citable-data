#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# purpose:  read list of Twitter user profiles and extract matching countries
# license:  MIT License
# author:   François-Xavier Coudert
# e-mail:   fxcoudert@gmail.com
#

import sys
import json

from collections import Counter
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd

with open(sys.argv[1], "r") as f:
    data = json.load(f)

geolocator = Nominatim(user_agent='myapplication')
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.1)
loc = [x["location"].strip() for x in data]
loc = [x for x in loc if len(x) > 1]

print(f'Found {len(loc)} locations')
print(f'Found {len(set(loc))} unique locations')

res = []
count = Counter(loc)

for loc, freq in count.most_common():
    x = geocode(loc, exactly_one=True, language="english", namedetails=True, addressdetails=True)
    if x:
        c = x.raw['address'].get('country_code', 'none')
    else:
        c = 'none'
    res.append((loc, freq, c))

df = pd.DataFrame(res)
df.to_excel("countries.xlsx")
