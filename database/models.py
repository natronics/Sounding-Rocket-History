from editor import db

UNKNOWN, SUCCESS, PARTIAL_SUCCESS, FAILURE = range(4)


class Vehicle(db.Model):
    """A launch vehicle (rocket)."""

    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.UnicodeText())
    length = db.Column(db.Float())
    width = db.Column(db.Float())
    launches = db.relationship('Launch', backref='vehicle', lazy='dynamic')

    def __repr__(self):
        return '%s [%d]' % (self.name, self.id)


class Site(db.Model):
    """A launch site"""

    __tablename__ = 'site'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.UnicodeText())
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    country = db.Column(db.String(128))
    launches = db.relationship('Launch', backref='site', lazy='dynamic')

    def __repr__(self):
        return '%s [%d]' % (self.name, self.id)


class LaunchSuccess(db.Model):

    __tablename__ = 'launchsuccess'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.UnicodeText())

    def __repr__(self):
        return str(self.name)


class Launch(db.Model):
    """Info about single launch"""

    __tablename__ = 'launch'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, index=True, unique=False)
    designation = db.Column(db.String(64))
    lv_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
    lv = db.relationship('Vehicle', backref='launch')
    ls = db.relationship('Site', backref='launch')
    result_id = db.Column(db.Integer, db.ForeignKey('launchsuccess.id'))
    result = db.relationship('LaunchSuccess', backref='launch')



    def __repr__(self):
        return '<launch %d>' % self.id
