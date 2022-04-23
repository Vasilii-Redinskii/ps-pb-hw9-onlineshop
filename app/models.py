from datetime import datetime

from app import db


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    items = db.relationship('Item', backref='brand', cascade='all,delete')

    def __repr__(self):
        return self.title


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    price = db.Column(db.Numeric(9, 2))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    user_items = db.relationship('UserItem', backref='item')

    def __repr__(self):
        return self.title

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    user_items = db.relationship('UserItem', backref='user', cascade='all,delete')

    def __repr__(self):
        return self.title


class UsersItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
