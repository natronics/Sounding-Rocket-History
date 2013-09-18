#!/usr/bin/env python
from database import models
from editor import db
import datetime


lv = models.Vehicle(name='Nike Asp')
db.session.add(lv)
db.session.commit()

site = models.Site(name='Wallops Flight Facility', lat=37.8445, lon=-75.4798, country="USA")
db.session.add(site)
db.session.commit()



lch = models.Launch(time=datetime.datetime(1960, 3, 1, 22, 11), designation='3.01 GS', success=models.SUCCESS, vehicle=lv, site=site)
db.session.add(lch)
db.session.commit()
