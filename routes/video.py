import socket
import subprocess
import cv2
import numpy as np
from flask import Response, jsonify

from routes import app

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9090))
print("running in 0.0.0.0:9090")

# 视频存储信息
video_type_avi = cv2.VideoWriter.fourcc('X','V','I','D')  # 使用XVID编码器创建avi文件
video_flag = False
image_flag = False
video_name = None
image_name = None
avi_file = None


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

                # 保存视频到avi文件
                if video_flag and avi_file is not None:
                    avi_file.write(img)

                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', img)[1].tobytes() + b'\r\n')

            except Exception as e:
                print(f"Error processing received data: {e}")

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')


# 开始录制视频到avi文件
@app.route("/video_start")
def startSaveVideo():
    global video_flag, video_name, avi_file
    video_name = "video"
    avi_file = cv2.VideoWriter(f'./video/{video_name}.avi', video_type_avi, 5, (480, 320))
    print('开始保存视频到.avi文件')
    video_flag = True
    return jsonify({'code': 200, "message": "开始保存视频"})


# 结束录制视频并调用FFmpeg进行转码
@app.route("/video_end")
def endSaveVideoAndConvert():
    global video_flag, avi_file, video_name
    if video_flag and avi_file is not None:
        avi_file.release()
        avi_file = None
        video_flag = False
        print('结束保存avi视频')

        # 调用FFmpeg将avi转换为h264 mp4格
        ffmpeg_command = " ffmpeg -i ./video/video.avi -vcodec h264 ./video/video.mp4"
        try:
            subprocess.check_call(ffmpeg_command, shell=True)
            print("视频已成功转换")
            return jsonify({'code': 200, "message": "视频保存并转换成功", "video_name": "video.mp4"})
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg转换错误: {e}")
            return jsonify({'code': 500, "message": "视频转换失败，请检查FFmpeg是否正确安装或配置"})
    else:
        return jsonify({'code': 400, "message": "未在录制状态，无法完成转换"})


# 截图
@app.route("/capture")
def capture():
    global image_flag, image_name
    image_name = "image"
    image_flag = True

    return jsonify({'code': 200, "message": "图片保存成功", "image_name": image_name})