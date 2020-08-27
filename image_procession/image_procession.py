# -*- coding:utf-8 -*-
import os
import sys
import shutil
import cv2

class ImageProcession:
    def __init__(self):
        self.image_folder = os.path.join(os.getcwd(), 'linshi')
    # 给出图像名拷贝一个图像,并以这个名称命名
    def GenerateImage(self, img_name):
        old_file = os.path.join(self.image_folder, 'meinv.jpg')
        new_file = os.path.join(self.image_folder, img_name)
        print old_file, new_file
        shutil.copyfile(old_file, new_file)
        print "success copy file"


    def GetCvImageFrom




















