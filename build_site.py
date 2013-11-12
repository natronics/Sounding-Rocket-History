#!/usr/bin/env python
import json
from database.models import *

# Write all flights to json
with open('data/sounding-rockets.json', 'w') as all_launches:
    launches = Launch.query.all()
    llist = []
    for launch in launches:
        l = {
            'time': launch.time.isoformat(),
            'designation': launch.designation,
            'vehicle': launch.launch_vehicle.name,
            'location': launch.launch_site.name,
            'result': launch.result.name,
            'apogee': launch.apogee,
        }
        llist.append(l)
    all_launches.write(json.dumps(llist))


vehicles =  Vehicle.query.all()
for vehicle in vehicles:
    
    filename = 'launch-vehicle/_posts/2013-01-01-{name}.markdown'.format(name=vehicle.name.lower().replace(' ','-'))
    with open(filename, 'w') as jekyll:
        jekyll.write("""---
layout: base
title: {name}
tags: [{launches}]
---

# {name} Launches

## Over Time:

{{% include launchchart.html %}}

--------------------------------------------------------------------------------

## Table:

{{: .table .table-hover}}
 Launch Date | Launch Vehicle | Location
 ----------- | -------------- | --------
""".format(name=vehicle.name, launches=1))

        for launch in vehicle.launches:
            jekyll.write(" {date} | {lv} | [{loc}](../{loclink}) \n".format(date=launch.time.isoformat(), lv=vehicle.name, loc=launch.launch_site.name, loclink=launch.launch_site.name.lower().replace(' ','-')))

        jekyll.write("\n\nDownload raw data: [{{ page.id | remove_first:'/'}}.json](../data/{{ page.categories }}/{{ page.id | remove_first:'/'}}.json)\n")

