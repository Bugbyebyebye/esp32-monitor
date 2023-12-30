import socket

import cv2
import numpy as np
from flask import Response, jsonify

from routes import app

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9090))
print("running in 0.0.0.0:9090")

# 视频存储格式
video_type = cv2.VideoWriter.fourcc('H', '2', '6', '4')
# 保存的位置
video_flag = False
image_flag = False
video_name = None
image_name = None


# 向前端输送视频
@app.route('/video')
def video_feed():
    def generate():
        global image_flag
        while True:
            data, addr = s.recvfrom(100000)
            if not data:
                continue
            try:
                image = np.frombuffer(data, dtype=np.uint8)
                img = cv2.imdecode(image, cv2.IMREAD_COLOR)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                if image_flag:
                    print('截图成功')
                    filename = f'./image/{image_name}.jpg'
                    cv2.imwrite(filename, img)
                    image_flag = False

                # 保存视频
                if video_flag:
                    print('正在保存视频...')
                    avi_file.write(img)

                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', img)[1].tobytes() + b'\r\n')

            except Exception as e:
                print(f"Error processing received data: {e}")

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')


# 开始录制视频
@app.route("/video_start")
def startSaveVideo():
    global video_flag, video_name, avi_file
    video_name = "video"
    avi_file = cv2.VideoWriter(f'./video/{video_name}.mp4', video_type, 5, (480, 320))
    print('开始保存视频')
    video_flag = True
    return jsonify({'code': 200, "message": "开始保存视频"})


# 结束录制视频
@app.route("/video_end")
def endSaveVideo():
    global video_flag
    print('结束保存视频')
    video_flag = False
    avi_file.release()

    return jsonify({'code': 200, "message": "视频保存成功", "video_name": video_name})


# 截图
@app.route("/capture")
def capture():
    global image_flag, image_name
    image_name = "image"
    image_flag = True

    return jsonify({'code': 200, "message": "图片保存成功", "image_name": image_name})
