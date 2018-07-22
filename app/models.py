import time, datetime
from app import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(128))
    receiver = db.Column(db.String(128))
    amount = db.Column(db.Numeric())
    timestamp = db.Column(db.DateTime())
    status = db.Column(db.String(32))

    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.status = 'submitted';

class Balance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(128))
    amount = db.Column(db.Numeric())
    lastUpdated = db.Column(db.DateTime())

    def __init__(self, user):
        self.user = user
        self.amount = 0
        self.lastUpdated = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    def deposit(self, fund):
        self.amount += fund

    def withdraw(self, fund):
        if self.amount >= fund:
            self.amount -= fund
            return True
        else:
            return False
