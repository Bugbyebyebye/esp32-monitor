from routes import db


class WarnUserRelate(db.Model):
    __tablename__ = 't_warn_user_relate'
    warn_user_id = db.Column(db.Integer, primary_key=True)
    warn_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)