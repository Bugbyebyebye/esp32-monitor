from routes import app
from flask import jsonify, request
from services import user_service,data_relate,data_service,warn_service,warn_relate


@app.route("/login", methods=['POST'])
def login():
    param = request.get_json()
    print("param => ", param)
    user = user_service.getUserByUsername(param['username'])
    if user.password == param['password'] or user is not None:
        return jsonify(
            {"code": 200, "message": "登录成功", "data": {"user_id": user.user_id, "create_time": user.create_time}})
    else:
        return jsonify({"code": 400, "message": "用户名或密码错误"})


@app.route("/register", methods=['POST'])
def register():
    param = request.get_json()
    print(param)
    user = user_service.addUser(username=param['username'], password=param['password'])
    print(user)

    return jsonify(
        {"code": 200, "message": "注册成功", "data": {"user_id": user.user_id, "create_time": user.create_time}})


@app.route("/stats",methods=['POST'])
def getStats():
    param = request.get_json()
    print(param)

    datalist = data_relate.getDataIdList(param['user_id'])
    warnlist = warn_relate.getWarnIdList(param['user_id'])

    imageNum = 0
    videoNum = 0
    warnNum = len(warnlist)

    for id in datalist:
        data = data_service.getDataById(id)
        if data.type == 0:
            imageNum = imageNum + 1
        else:
            videoNum = videoNum + 1

    return jsonify({"code": 200, "message": "获取成功", "data": {"imageNum": imageNum, "videoNum": videoNum, "warnNum": warnNum}})