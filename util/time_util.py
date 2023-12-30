import time

# 获取当前时间的Unix时间戳（毫秒）
def getCurrentUnixTime():
    millis = int(round(time.time() * 1000))
    return millis
