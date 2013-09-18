#!/usr/bin/env python
from database import models
from editor import db
import datetime


lv = models.Vehicle(name='Nike Asp')
db.session.add(lv)
db.session.commit()


lch = models.Launch(time=datetime.datetime(1960, 3, 1, 22, 11), designation='3.01 GS', success=models.SUCCESS, vehicle=lv)
db.session.add(lch)
db.session.commit()
