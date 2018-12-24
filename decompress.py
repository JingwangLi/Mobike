# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 10:16
# @Author  : Jingwang Li
# @Email   : jingwanali@gmail.com
# @Blog    : www.jingwangl.com

import sys
import os
import pandas
import gzip
open_path = ''
save_path = 'E:\\data'
os.chdir(open_path)#转到路径
#首先，通过zipfile模块打开指定位置zip文件
#传入文件名列表，及列表文件所在路径，及存储路径
def Decompression(files,file_path,save_path):
    os.getcwd()#当前路径
    os.chdir(file_path)#转到路径
    for file_name in files:
        print(file_name)
        os.chdir(file_path)  # 转到路径
        with gzip.open(file_name, 'rb') as f1:
            # f_content = f.read()
            os.chdir(save_path)#转到存储路径
            with open(file_name[:-3], 'wb') as f2:
                f2.write(f1.read())

def files_save(open_path):
    for file_path, sub_dirs, files in os.walk(open_path):#获取所有文件名，路径
        # print(file_path, sub_dirs, files)
        print(file_path)
        Decompression(files, file_path, save_path)

files_save(open_path)


