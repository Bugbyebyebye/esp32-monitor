from models.warn_model import Warn
from routes import db
from util.time_util import getCurrentUnixTime


def getWarnById(id):
    warn = db.session.query(Warn).filter_by(warn_id=id).first()
    return warn


def addWarn(name):
    warn = Warn(warn_name=name, state=1, create_time=getCurrentUnixTime())
    db.session.add(warn)
    db.session.commit()
    return warn
