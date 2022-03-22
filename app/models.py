from . import db
from werkzeug.security import generate_password_hash

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String)
    rooms = db.Column(db.String)
    bathrooms = db.Column(db.String)
    price = db.Column(db.String(80))
    propertytype = db.Column(db.String(80))
    location = db.Column(db.String(80))
    filename = db.Column(db.String(250))


    def __init__(self,title,description,rooms,bathrooms,price,propertytype,location,filename):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.propertytype = propertytype
        self.location = location
        self.filename = filename


