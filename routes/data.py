from routes import app
from flask import jsonify, request

from services.data_relate import addRelate, getDataIdList
from util import file_util
from services.data_service import addData, getDataById



# 上传图片和视频
@app.route("/upload", methods=['POST'])
def uploadFile():
    param = request.get_json()
    print(param)
    url = file_util.UploadFileToQiNiu(param['path'])
    return jsonify({"code": 200, "message": "上传成功", "url": url})


@app.route("/addData", methods=['POST'])
def saveData():
    param = request.get_json()
    print(param)

    if param['type'] == 'image':
        dataType = 0
    else:
        dataType = 1
    data = addData(param['title'], param['content'], param['url'], dataType)
    print(data)

    relate = addRelate(param['user_id'], data.data_id)
    print(relate)

    return jsonify({"code": 200, "message": "保存成功"})


@app.route("/getImageList", methods=['GET'])
def getImageList():
    userId = request.args.get("user_id")
    # print(userId)
    dataIdList = getDataIdList(userId)

    dataList = []
    for id in dataIdList:
        data = getDataById(id)
        if data.type == 0:
            dic = {
                "data_id": data.data_id,
                "title": data.title,
                "content": data.content,
                "url": data.url,
                "type": data.type,
                "create_time": data.create_time,
                "update_time": data.update_time
            }
            dataList.append(dic)

    return jsonify({"code": 200, "message": "获取成功", "data": dataList})


@app.route("/getVideoList", methods=['GET'])
def getVideoList():
    userId = request.args.get("user_id")
    # print(userId)
    dataIdList = getDataIdList(userId)

    dataList = []
    for id in dataIdList:
        data = getDataById(id)
        if data.type == 1:
            dic = {
                "data_id": data.data_id,
                "title": data.title,
                "content": data.content,
                "url": data.url,
                "type": data.type,
                "create_time": data.create_time,
                "update_time": data.update_time
            }
            dataList.append(dic)

    return jsonify({"code": 200, "message": "获取成功", "data": dataList})
