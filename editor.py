#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import admin
from flask.ext.admin.contrib import sqla

from dateutil import parser
import config

app = Flask(__name__, static_folder='resources')
app.config.from_object('config')
db = SQLAlchemy(app)

from database.models import *


@app.route("/")
def index():
    launches = Launch.query.all()
    return render_template('index.html', launches=launches)


@app.route("/vehicle/<int:lvid>", methods=['GET', 'POST'])
def vehicle(lvid):
    vehicle = Vehicle.query.get(lvid)
    updated = False
    if request.method == 'POST':
        vehicle.name = request.form['vehicle.name']
        vehicle.desc = request.form['vehicle.desc']
        vehicle.length = request.form['vehicle.length']
        vehicle.width = request.form['vehicle.width']
        db.session.merge(vehicle)
        db.session.commit()
        updated = True

    fields = []
    for meta in vehicle.crud:
        fields.append(dict({'val': getattr(vehicle, meta['key'])}, **meta))
        
    return render_template('vehicle.html', name=vehicle.name, fields=fields, updated=updated)


@app.route("/vehicle/new", methods=['GET', 'POST'])
def new_vehicle():
    if request.method == 'POST':
        name = request.form['vehicle.name']
        desc = request.form['vehicle.desc']
        lv = database.models.Vehicle(name=name, desc=desc)
        db.session.add(lv)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('vehicle.html', name=None, fields=database.models.Vehicle.crud, updated=False)


@app.route("/launch/new", methods=['GET', 'POST'])
def launch():
    if request.method == 'POST':
        time = parser.parse(request.form['launch.datetime'])
        desig = request.form['launch.desg']
        success = int(request.form['launch.status'])
        lvid = request.form['launch.lv']
        siteid = request.form['launch.site']

        lch = database.models.Launch(time=time, designation=desig, success=success, lv_id=lvid, site_id=siteid)
        db.session.add(lch)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('launch.html', vehicles=database.models.Vehicle.query.all(), sites=database.models.Site.query.all())


@app.route("/site/<int:siteid>", methods=['GET', 'POST'])
def site(siteid):
    site = database.models.Site.query.get(siteid)
    updated = False
    if request.method == 'POST':
        site.name = request.form['site.name']
        site.desc = request.form['site.desc']
        site.lat  = request.form['site.lat']
        site.lon  = request.form['site.lon']
        site.country = request.form['site.country']

        db.session.merge(site)
        db.session.commit()
        updated = True

    fields = []
    for meta in site.crud:
        fields.append(dict({'val': getattr(site, meta['key'])}, **meta))

    context = {
        'fields': fields,
        'updated': updated,
        'entrytype': "Launch Site",
        'model': "site",
        'name': site.name,
    }

    return render_template('edit_entry.html', **context)


@app.route("/site/new", methods=['GET', 'POST'])
def new_site():
    if request.method == 'POST':
        name = request.form['site.name']
        desc = request.form['site.desc']
        lat  = request.form['site.lat']
        lon  = request.form['site.lon']
        country = request.form['site.country']

        site = database.models.Site(name=name, desc=desc, lat=lat, lon=lon, country=country)
        db.session.add(site)
        db.session.commit()
        return redirect(url_for('index'))

    context = {
        'fields': database.models.Site.crud,
        'updated': False,
        'entrytype': "Launch Site",
        'model': "site",
        'name': None,
    }

    return render_template('edit_entry.html', **context)


class SiteAdmin(sqla.ModelView):
    column_display_pk = False
    form_columns = ['name', 'desc', 'lat', 'lon', 'country']

class VehicleAdmin(sqla.ModelView):
    column_display_pk = False
    form_columns = ['name', 'desc', 'length', 'width']

class LaunchAdmin(sqla.ModelView):
    column_display_pk = True
    form_columns = ['time', 'designation', 'success', 'lv_id']


if __name__ == "__main__":
    # Create admin
    admin = admin.Admin(app, 'Sound Rocket Models')
    admin.add_view(SiteAdmin(Site, db.session))
    admin.add_view(VehicleAdmin(Vehicle, db.session))
    admin.add_view(LaunchAdmin(Launch, db.session))

    app.debug = True
    app.run()
