from routes import db


class Data(db.Model):
    __tablename__ = 't_data'
    data_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.BigInteger, nullable=False)
