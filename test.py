# -*- coding:utf-8 -*-
import base64
from flask import Flask, request
import hashlib
from name_manage.name_manage import NameManage
from image_procession.image_procession import ImageProcession
from config import config

# --------------
name_manage = NameManage()
img_proc = ImageProcession()
# 设置生成图片的地址
app = Flask(__name__, static_folder=config.file_save_image)

# 下面这个装饰器表明了hello world与url的绑定
# 也就是说访问'/'这个url的路径和方法才会调用下面的hello world的函数
@app.route('/', methods=['POST','GET'])
def receive_image():
    user_id = request.form.get("user_id")        # 获取用户的id
    image_name = request.form.get("image_name")  # 获取用户的照片名称
    img = request.files['photo']
    # ------------------生成一张新的图片的名字----------------------------------------
    new_img_name = name_manage.GenerateName(user_id, image_name)
    img_proc.GenerateImage(new_img_name)
    # ------------------
    download_image_url = name_manage.GenerateDownloadUrl(new_img_name)
    print download_image_url
    return download_image_url



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=443,
            ssl_context=('/root/projects/Nginx/1_bigseriouslee.top_bundle.crt',
                         '/root/projects/Nginx/2_bigseriouslee.top.key'))