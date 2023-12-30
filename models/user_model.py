from routes import db


class User(db.Model):
    __tablename__ = 't_user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    state = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.BigInteger, nullable=False)