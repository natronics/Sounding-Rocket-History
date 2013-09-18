from editor import db

UNKNOWN, SUCCESS, PARTIAL_SUCCESS, FAILURE = range(4)


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    launches = db.relationship('Launch', backref='vehicle', lazy='dynamic')

    def __repr__(self):
        return '<vehicle %s (%d)>' % (self.name, self.id)


class Launch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, index=True, unique=False)
    designation = db.Column(db.String(64))
    success = db.Column(db.SmallInteger, default=UNKNOWN)
    lv_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

    def __repr__(self):
        return '<launch %d>' % self.id
