from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    message = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)

    def __init__(self, username, message, timestamp):
        self.username = username
        self.message = message
        self.timestamp = timestamp