from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email, phone, address, country):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.country = country

    def serialize(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'country': self.country
        }
