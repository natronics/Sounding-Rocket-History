from editor import db

UNKNOWN, SUCCESS, PARTIAL_SUCCESS, FAILURE = range(4)

lat_num = {'min': -90.0, 'max': 90.0, 'step': 0.0001}
lon_num = {'min': -180.0, 'max': 180.0, 'step': 0.0001}
length_num = {'min': 0.0, 'max': 110.6, 'step': 0.01}


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.UnicodeText())
    length = db.Column(db.Float())
    width = db.Column(db.Float())
    launches = db.relationship('Launch', backref='vehicle', lazy='dynamic')

    crud = [
        {'key': 'name', 'title': u"Name", 'type': 'short'},
        {'key': 'length', 'title': u"Length", 'type': 'number', 'units': "meters", 'validate': length_num},
        {'key': 'width', 'title': u"Width", 'type': 'number', 'units': "meters", 'validate': length_num},
        {'key': 'desc', 'title': u"Article", 'type': 'text'},
    ]

    def __repr__(self):
        return '<vehicle %s (%d)>' % (self.name, self.id)


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.UnicodeText())
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    country = db.Column(db.String(128))
    launches = db.relationship('Launch', backref='site', lazy='dynamic')

    crud = [
        {'key': 'name', 'title': u"Name", 'type': 'short'},
        {'key': 'lat', 'title': u"Latitude", 'type': 'number', 'units': "degrees", 'validate': lat_num},
        {'key': 'lon', 'title': u"Longituded", 'type': 'number', 'units': "degrees", 'validate': lon_num},
        {'key': 'country', 'title': u"Country", 'type': 'short'},
        {'key': 'desc', 'title': u"Article", 'type': 'text'},
    ]


    def __repr__(self):
        return '<site %s (%d)>' % (self.name, self.id)

class Launch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, index=True, unique=False)
    designation = db.Column(db.String(64))
    success = db.Column(db.SmallInteger, default=UNKNOWN)
    lv_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))


    def __repr__(self):
        return '<launch %d>' % self.id
