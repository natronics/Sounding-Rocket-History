#!/usr/bin/env python
import json
from database.models import *

# Write all flights to json
with open('data/sounding-rockets.json', 'w') as all_launches:
    launches = Launch.query.all()
    llist = []
    for launch in launches:
        l = {
            'date': launch.time.isoformat(),
            'designation': launch.designation,
            'vehicle': launch.launch_vehicle.name,
            'location': launch.launch_site.name,
            'result': launch.result.name,
            'apogee': launch.apogee,
        }
        llist.append(l)
    all_launches.write(json.dumps({'launches': llist}))


vehicles =  Vehicle.query.all()
for vehicle in vehicles:

    slug = vehicle.name.lower().replace(' ','-')
    launches = vehicle.launches
    llist = []

    filename = 'launch-vehicle/_posts/2013-01-01-{name}.markdown'.format(name=slug)
    with open(filename, 'w') as jekyll:
        jekyll.write("""---
layout: base
title: {name}
tags: [{launches}]
---

# <span class="small">Launch Vehicle:</span>  {name}

{desc}

## Launches Over Time:

{{% include launchchart.html %}}

--------------------------------------------------------------------------------

## Table:

{{: .table .table-hover}}
 Designator | Launch Date | Launch Site | Result | Apogee \[**km**\] 
 ---------- | ----------- | ----------- | ------ | ----------------- 
""".format(name=vehicle.name, desc=vehicle.desc, launches=vehicle.launches.count()))

        for launch in vehicle.launches:
            jekyll.write(" {des} | {date} | [{loc}](../{loclink}) | {res} | {apogee} \n".format(des=launch.designation,
                date=launch.time.isoformat(),
                loc=launch.launch_site.name,
                loclink=launch.launch_site.name.lower().replace(' ','-'),
                res=launch.result.name,
                apogee=launch.apogee
                ))
            l = {
                'date': launch.time.isoformat(),
                'designation': launch.designation,
                'vehicle': launch.launch_vehicle.name,
                'location': launch.launch_site.name,
                'result': launch.result.name,
                'apogee': launch.apogee,
            }
            llist.append(l)

        jekyll.write("\n\nDownload raw data: [{{ page.id | remove_first:'/'}}.json](../data/{{ page.categories }}/{{ page.id | remove_first:'/'}}.json)\n")

    rawdata = "data/launch-vehicle/{slug}.json".format(slug=slug)
    with open(rawdata, 'w') as raw:
        raw.write(json.dumps({'launches': llist}))


sites =  Site.query.all()
for location in sites:

    slug = location.name.lower().replace(' ','-')
    launches = location.launches

    llist = []

    filename = 'location/_posts/2013-01-01-{name}.markdown'.format(name=slug)
    with open(filename, 'w') as jekyll:
        jekyll.write("""---
layout: base
title: {name}
tags: [{launches}]
---

# <span class="small">Launch Site:</span>  {name}

{desc}

## Launches Over Time:

{{% include launchchart.html %}}

--------------------------------------------------------------------------------

## Table:

{{: .table .table-hover}}
 Designator | Launch Date | Launch Vehicle | Result | Apogee \[**km**\] 
 ---------- | ----------- | -------------- | ------ | ----------------- 
""".format(name=location.name, desc=location.desc, launches=launches.count()))


        for launch in launches:
            jekyll.write(" {des} | {date} | [{lv}](../{lvlink}) | {res} | {apogee} \n".format(des=launch.designation,
                date=launch.time.isoformat(),
                lv=launch.launch_vehicle.name,
                lvlink=launch.launch_vehicle.name.lower().replace(' ','-'),
                res=launch.result.name,
                apogee=launch.apogee
                ))

            l = {
                'date': launch.time.isoformat(),
                'designation': launch.designation,
                'vehicle': launch.launch_vehicle.name,
                'location': launch.launch_site.name,
                'result': launch.result.name,
                'apogee': launch.apogee,
            }
            llist.append(l)

        jekyll.write("\n\nDownload raw data: [{{ page.id | remove_first:'/'}}.json](../data/{{ page.categories }}/{{ page.id | remove_first:'/'}}.json)\n")

    rawdata = "data/location/{slug}.json".format(slug=slug)
    with open(rawdata, 'w') as raw:
        raw.write(json.dumps({'launches': llist}))

