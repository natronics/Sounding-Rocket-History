#!/usr/bin/env python

from dateutil import parser

all_flights = []


with open('rawdata/sounding-rocket-history.csv', 'r') as f_in:
    for line in f_in:
        if line[0] != '#':
            li = line.split(',')
            date     = parser.parse((li[0]).strip())
            vehicle  =               li[1].strip()
            location =               li[2].strip()

            all_flights.append({'date': date, 'vehicle': vehicle, 'location': location})


for flight in all_flights:
    with open('_posts/%d-12-31-%d.textile' % (flight['date'].year, flight['date'].year), 'w') as post:
        post.write("""---
layout: base
title: Data by year
---

h1. Data for %d

 * %s, %s, %s

{%% include datetest.html %%}

"""  % (flight['date'].year, flight['date'].isoformat(), flight['vehicle'], flight['location']))

    with open('launch-vehicle/_posts/2013-01-01-%s.textile' % flight['vehicle'].replace(' ','-'), 'w') as post:
        post.write("""---
layout: base
title: Data for %s
---

h1. Data for %s

 * %s, %s, %s

{%% include datetest.html %%}

"""  % (flight['vehicle'], flight['vehicle'], flight['date'].isoformat(), flight['vehicle'], flight['location']))

