import requests

from routes import app
from app import mqtt_client
from flask import request, jsonify


# MQTT 连接回调函数
@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe("sonar_alert")  # 订阅主题
    else:
        print('Bad connection. Code:', rc)


# MQTT 接收消息函数
@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print('Received message on topic: {topic} with payload: {payload}'.format(**data))
    if data['topic'] == 'sonar_alert':
        requests.post('http://localhost:5000/addWarn', json=data)


# MQTT 发布消息
@app.route('/publish', methods=['POST'])
def publish_message():
    request_data = request.get_json()
    print("发送MQTT => ", request_data)
    publish_result = mqtt_client.publish(request_data['topic'], request_data['msg'])
    return jsonify({'code': publish_result[0], "message": "发送成功"})
