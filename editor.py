#!/usr/bin/env python
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
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
        db.session.commit()
        updated = True

    return render_template('vehicle.html', vehicle=vehicle, updated=updated)

if __name__ == "__main__":
    app.debug = True
    app.run()
