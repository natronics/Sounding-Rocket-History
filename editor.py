#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from dateutil import parser
import config

app = Flask(__name__, static_folder='resources')
app.config.from_object('config')
db = SQLAlchemy(app)

import database.models

@app.route("/")
def index():
    launches = database.models.Launch.query.all()
    return render_template('index.html', launches=launches)

@app.route("/vehicle/<int:lvid>", methods=['GET', 'POST'])
def vehicle(lvid):
    vehicle = database.models.Vehicle.query.get(lvid)
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

    return render_template('launch.html', vehicles=database.models.Vehicle.query.all())

if __name__ == "__main__":
    app.debug = True
    app.run()
