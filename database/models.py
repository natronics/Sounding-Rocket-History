from editor import db


class Vehicle(db.Model):
    """A launch vehicle (rocket).
    """

    __tablename__ = 'vehicle'

    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(128), nullable=False)
    desc            = db.Column(db.UnicodeText())
    length          = db.Column(db.Float())
    width           = db.Column(db.Float())
    launches        = db.relationship('Launch', backref='vehicle', lazy='dynamic')

    def __repr__(self):
        return '%s [%d]' % (self.name, self.id)


class Site(db.Model):
    """The facility, not individual pad where launches occur has a link to the country
    it's in or is operated by, in the case of territories
    """

    __tablename__ = 'site'

    id = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(128), nullable=False)
    abbrv           = db.Column(db.String(16), nullable=False)
    desc            = db.Column(db.UnicodeText())
    latitude        = db.Column(db.Float, nullable=False)
    longitude       = db.Column(db.Float, nullable=False)
    launches        = db.relationship('Launch', backref='site', lazy='dynamic')
    country_id      = db.Column(db.Integer, db.ForeignKey('country.id'))
    country         = db.relationship('Country', backref='site')

    def __repr__(self):
        return str(self.name)


class LaunchSuccess(db.Model):
    """Many launches have some information about if they worked. This is strictly
    for the physical launch vehicle itself. Further information about payload success
    sould be kept somewhere else
    """

    __tablename__ = 'launchsuccess'

    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(128), nullable=False)
    desc            = db.Column(db.UnicodeText())

    def __repr__(self):
        return str(self.name)


class Country(db.Model):
    """A country, mostly so the flag and geo data can be kept in one place.
    """

    __tablename__ = 'country'

    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(128), nullable=False)
    geo_outline     = db.Column(db.UnicodeText())
    flag            = db.Column(db.UnicodeText(), nullable=False)

    def __repr__(self):
        return str(self.name)


class Launch(db.Model):
    """Information for single launch that occured. Links back to the vehicle
    and launch site. There are medatadata fields as well. This is the primary
    chunck of info for the site
    """

    __tablename__ = 'launch'

    id              = db.Column(db.Integer, primary_key=True)
    time            = db.Column(db.DateTime, index=True, unique=False)
    designation     = db.Column(db.String(64))
    lv_id           = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    launch_vehicle  = db.relationship('Vehicle', backref='launch')
    site_id         = db.Column(db.Integer, db.ForeignKey('site.id'), nullable=False)
    launch_site     = db.relationship('Site', backref='launch')
    result_id       = db.Column(db.Integer, db.ForeignKey('launchsuccess.id'), nullable=False)
    result          = db.relationship('LaunchSuccess', backref='launch')
    apogee          = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return 'launch %s [%d]' % (self.designation, self.id)
