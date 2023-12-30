from routes import app
from flask_mqtt import Mqtt

# 配置mqtt拓展
app.config['MQTT_BROKER_URL'] = '8.130.84.188'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 5

mqtt_client = Mqtt(app)

# 启动服务器
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
