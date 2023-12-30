from flask import request, jsonify

from routes import app
from services.warn_relate import addRelate, getWarnIdList
from services.warn_service import addWarn, getWarnById


@app.route("/getWarnList", methods=['GET'])
def getWarnList():
    userId = request.args.get("user_id")
    # print(userId)
    warnIdList = getWarnIdList(userId)

    warnList = []
    for id in warnIdList:
        warn = getWarnById(id)
        dic = {
            "warn_id": warn.warn_id,
            "name": warn.warn_name,
            "create_time": warn.create_time,
            "update_time": warn.update_time
        }
        warnList.append(dic)

    warnList.sort(key=lambda x: x['create_time'], reverse=True)

    return jsonify({"code": 200, "message": "获取成功", "data": warnList})

@app.route("/addWarn",methods=['POST'])
def addTheWarn():
    param = request.get_json()
    print(param['payload'])
    warn = addWarn(param['payload'])
    addRelate(10001,warn.warn_id)
    return jsonify({"code": 200, "message": "添加成功"})