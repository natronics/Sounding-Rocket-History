#!/usr/bin/env python
from flask import Flask, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import admin
from flask.ext.admin.contrib import sqla
import config

app = Flask(__name__, static_folder='resources')
app.config.from_object('config')
db = SQLAlchemy(app)

from database.models import *

@app.route("/")
def index():
    return redirect('/admin')

class SiteAdmin(sqla.ModelView):
    column_display_pk = False
    column_list = ('name', 'latitude', 'longitude', 'country')
    form_columns = ['name', 'abbrv', 'desc', 'latitude', 'longitude', 'country']

class VehicleAdmin(sqla.ModelView):
    column_display_pk = False
    column_list = ('name', 'length', 'width')
    form_columns = ['name', 'desc', 'length', 'width']

class LaunchAdmin(sqla.ModelView):
    column_display_pk = False
    column_list = ('time', 'designation', 'launch_vehicle', 'launch_site', 'result',  'apogee')
    form_columns = ['time', 'designation', 'launch_vehicle', 'launch_site', 'result',  'apogee']

class ResultAdmin(sqla.ModelView):
    column_display_pk = False
    form_columns = ['name', 'desc']

class CountryAdmin(sqla.ModelView):
    column_display_pk = False
    column_list = ('name',)
    form_columns = ['name', 'geo_outline', 'flag']


if __name__ == "__main__":
    # Create admin interface
    admin = admin.Admin(app, 'Sound Rocket Database')
    admin.add_view(SiteAdmin(Site, db.session))
    admin.add_view(VehicleAdmin(Vehicle, db.session))
    admin.add_view(LaunchAdmin(Launch, db.session))
    admin.add_view(ResultAdmin(LaunchSuccess, db.session))
    admin.add_view(CountryAdmin(Country, db.session))

    # Run local webserver
    app.debug = True
    app.run()
