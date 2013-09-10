#!/usr/bin/env python

from dateutil import parser
from copy import deepcopy
import json

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
            if location not in flights['loc']:
                flights['loc'][location] = []
            flights['loc'][location].append(launch)


for key, name in {'year': "year", 'lv': "launch-vehicle", 'loc': "location"}.iteritems():

    for slicekey, launches in flights[key].iteritems():

        # Textile for jekyll pages
        filename = '{setkey}/_posts/2013-01-01-{slice}.textile'.format(setkey=name, slice=slicekey.replace(' ','-'))
        if key == 'year':
            filename = '{setkey}/_posts/{slice}-12-31-{slice}.textile'.format(setkey=name, slice=slicekey)
        with open(filename, 'w') as post:
            post.write("""---
layout: base
title: {slice}
---

h1. {slice} Launches

table(table).
|.Launch Date|.Launch Vehicle|.Location|
""".format(slice=slicekey))

            for launch in launches:
                post.write("|{date}|{lv}|{loc}|\n".format(date=launch['date'], lv=launch['vehicle'], loc=launch['location']))

            post.write("\n")

        # Raw data
        filename = 'data/{setkey}/{slice}.json'.format(setkey=name, slice=slicekey.replace(' ','-'))

        l = []
        for launch in launches:
            tmp = deepcopy(launch)
            tmp['date'] = tmp['date'].isoformat()
            l.append(tmp)

        with open(filename, 'w') as data:
            data.write(json.dumps({'launches': l}))
