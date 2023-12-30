from routes import db


class Warn(db.Model):
    __tablename__ = 't_warn'
    warn_id = db.Column(db.Integer, primary_key=True)
    warn_name = db.Column(db.String(255), nullable=False)
    state = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.BigInteger, nullable=False)
