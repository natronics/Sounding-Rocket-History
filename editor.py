#!/usr/bin/env python
from flask import Flask, render_template
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

if __name__ == "__main__":
    app.debug = True
    app.run()
