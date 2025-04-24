from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize SQLAlchemy here

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    crops = db.relationship('Crop', backref='farmer', lazy=True)

class Dealer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    bids = db.relationship('Bid', backref='dealer', lazy=True)

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'))
    bids = db.relationship('Bid', backref='crop', lazy=True)

class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    transport_fee = db.Column(db.Float, default=0.0)
    dealer_id = db.Column(db.Integer, db.ForeignKey('dealer.id'))
    crop_id = db.Column(db.Integer, db.ForeignKey('crop.id'))