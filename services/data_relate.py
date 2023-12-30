from models.data_user_model import DataUserRelate
from routes import db


def addRelate(user_id, data_id):
    relate = DataUserRelate(user_id=user_id, data_id=data_id)
    db.session.add(relate)
    db.session.commit()
    return relate

def getDataIdList(user_id):
    dataIdList = []
    list = db.session.query(DataUserRelate).filter_by(user_id=user_id).all()
    # print(list)
    for relate in list:
        dataIdList.append(relate.data_id)
    return dataIdList