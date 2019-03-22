# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 9:48
# @Author  : Jingwang Li
# @Email   : jingwanali@gmail.com
# @Blog    : www.jingwangl.com


import shapefile

map_path = 'G:\Lab6'
file = shapefile.Reader(map_path + '\\' + 'Road')
print(file)