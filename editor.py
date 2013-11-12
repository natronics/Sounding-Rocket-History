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
    form_columns = ['name', 'desc', 'lat', 'lon', 'country']

class VehicleAdmin(sqla.ModelView):
    column_display_pk = False
    form_columns = ['name', 'desc', 'length', 'width']

class LaunchAdmin(sqla.ModelView):
    column_display_pk = True
    form_columns = ['time', 'designation', 'success', 'lv', 'ls']


if __name__ == "__main__":
    # Create admin
    admin = admin.Admin(app, 'Sound Rocket Models')
    admin.add_view(SiteAdmin(Site, db.session))
    admin.add_view(VehicleAdmin(Vehicle, db.session))
    admin.add_view(LaunchAdmin(Launch, db.session))

    app.debug = True
    app.run()
