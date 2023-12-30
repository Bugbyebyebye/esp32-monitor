from qiniu import Auth, put_data, put_file
import uuid

access_key = '89VRcOeJLPI3HAuf_lbdT0qU6KrazC7_KdtCZsxT'
secret_key = 'UBMz3-03Cw-z-qkIfbMqbvFygbP_72nZCCodlSkg'

auth = Auth(access_key=access_key, secret_key=secret_key)
bucket_name = 'hjbsport'
domain = 'cdn.emotionalbug.top'


# 上传文件
def UploadFileToQiNiu(file_path):
    print('/upload filepath => ', file_path)

    key = 'Esp32/' + str(uuid.uuid4())
    token = auth.upload_token(bucket_name, key, 3600)

    ret, info = put_file(token, key, file_path)

    if info.status_code == 200:
        print(ret.get("key"))
        return "http://" + domain + "/" + ret.get("key")
    else:
        print("上传失败")
