from routes import db


class DataUserRelate(db.Model):
    __tablename__ = 't_data_user_relate'
    data_user_id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)