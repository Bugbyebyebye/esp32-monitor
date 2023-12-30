from models.user_model import User
from routes import db
from util.time_util import getCurrentUnixTime


# 登录
def getUserByUsername(username):
    user = db.session.query(User).filter_by(username=username).first()
    return user


# 注册新用户
def addUser(username, password):
    new_user = User(username=username, password=password, state=1, create_time=getCurrentUnixTime())
    db.session.add(new_user)
    db.session.commit()
    return new_user
