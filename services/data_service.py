from models.data_model import Data
from routes import db
from util.time_util import getCurrentUnixTime


def getDataById(id):
    data = db.session.query(Data).filter_by(data_id=id).first()
    return data


def addData(title, content, url, type):
    data = Data(title=title, content=content, url=url, type=type, state=1, create_time=getCurrentUnixTime())
    db.session.add(data)
    db.session.commit()
    return data
