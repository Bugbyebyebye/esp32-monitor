from models.warn_user_model import WarnUserRelate
from routes import db


def addRelate(user_id, warn_id):
    relate = WarnUserRelate(user_id=user_id, warn_id=warn_id)
    db.session.add(relate)
    db.session.commit()
    return relate


def getWarnIdList(user_id):
    warnIdList = []
    list = db.session.query(WarnUserRelate).filter_by(user_id=user_id).all()
    # print(list)
    for relate in list:
        warnIdList.append(relate.warn_id)
    return warnIdList