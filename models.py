from extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

class User(db.Model, BaseModel, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date)
    gender = db.Column(db.String)
    country = db.Column(db.String)

    messages = db.relationship("Message", backref="user", lazy=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password, password)




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Message(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    sent_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    is_chatbot = db.Column(db.Boolean)