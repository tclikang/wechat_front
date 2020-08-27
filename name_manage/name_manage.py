# -*- coding:utf-8 -*-
import hashlib

class NameManage:
    # 初始化一个类
    def __init__(self):
        self.md = hashlib.md5()


    # 名字的生成规则
    def GenerateNameRule(self):
        return 'https://bigseriouslee.top/linshi/two_loss460.jpg'

    # 返回下载图片的地址
    def GenerateName(self, user_id, image_name):
        self.md.update(image_name.encode('utf-8'))
        union_img_name = self.md.hexdigest()
        img_name = user_id + '_' + union_img_name[-10 : -1] + '.jpg'
        return img_name


    def GenerateDownloadUrl(self, image_name):
        return 'https://bigseriouslee.top/linshi/' + image_name
























