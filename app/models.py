from app import db

class Task(db.Model):
  id = db.Column(db.String(50), primary_key=True)
  name = db.Column(db.String(500))
  deadline = db.Column(db.DateTime)
  length = db.Column(db.Integer)
  priority = db.Column(db.Integer)
  slot = db.Column(db.Integer)

class User(db.Model):
  id = db.Column(db.String(50), primary_key=True)
  usename = db.Column(db.String(120), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)