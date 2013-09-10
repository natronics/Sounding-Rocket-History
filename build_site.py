#!/usr/bin/env python

from dateutil import parser

flights = {'all': [], 'year': {}, 'lv': {}, 'loc': {}}


with open('rawdata/sounding-rocket-history.csv', 'r') as f_in:
    for line in f_in:
        if line[0] != '#':
            li = line.split(',')
            date     = parser.parse((li[0]).strip())
            vehicle  =               li[1].strip()
            location =               li[2].strip()

            year = str(date.year)

            launch = {'date': date, 'vehicle': vehicle, 'location': location}

            flights['all'].append(launch)
            if year not in flights['year']:
                flights['year'][year] = []
            flights['year'][year].append(launch)
            if vehicle not in flights['lv']:
                flights['lv'][vehicle] = []
            flights['lv'][vehicle].append(launch)


# Chunk out by year
for year, launches in flights['year'].iteritems():
    with open('year/_posts/{year}-12-31-{year}.textile'.format(year=year), 'w') as post:
        post.write("""---
layout: base
title: {year}
---

h1. Data for {year}

table(table).
|.Launch Date|.Launch Vehicle|.Location|
""".format(year=year))
        for launch in launches:
            post.write("|{date}|{lv}|{loc}|".format(date=launch['date'], lv=launch['vehicle'], loc=launch['location']))


# Chunk out by lv
for lv, launches in flights['lv'].iteritems():
    with open('launch-vehicle/_posts/2013-01-01-{lv}.textile'.format(lv=lv.replace(' ','-')), 'w') as post:
        post.write("""---
layout: base
title: {lv}
---

h1. Data for {lv}

table(table).
|.Launch Date|.Launch Vehicle|.Location|
""".format(lv=lv))
        for launch in launches:
            post.write("|{date}|{lv}|{loc}|\n".format(date=launch['date'], lv=launch['vehicle'], loc=launch['location']))
