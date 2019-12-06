# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 23:25
# @Author  : Jingwang Li
# @Email   : jingwanali@gmail.com
# @Blog    : www.jingwangl.com

import os
import numpy as np
import pandas as pd

read_path = "E:\\data\\Mobike\\unzip\\"
save_path = "E:\\data\\Mobike\\byday\\"

# file_list = os.listdir(read_path)
#
# def sort_by_ID(name):
#     data = pd.read_csv(read_path + name)
#     data.columns = ['time', 'ID', 'lon', 'lat']
#     data['ID'] = data['ID'].apply(lambda x: x[:-1])
#     data = data.sort_values(by='ID', ascending='True')
#     data.to_csv(save_path + name, index=False)
#
# for file in file_list:
#     print(file)
#     sort_by_ID(file)


# def exact_trips(a, b):
#     file1, file2 = pd.read_csv(day_path + a), pd.read_csv(day_path + b)
#     i = j = 0
#     n1, n2 = len(file1), len(file2)
#     while i < n1 and j < n2:
#         if file1.iloc[i, 1] < file2.iloc[j, 1]:
#             i += 1
#         elif file1.iloc[i, 1] > file2.iloc[j, 1]:
#             j += 1
#         else:
#             if file1.iloc[i, 2] != file2.iloc[j, 2] or file1.iloc[i, 3] != file2.iloc[j, 3]:
#                 trips.loc[len(trips)] = [file1.iloc[i, 1], file1.iloc[i, 0], (file1.iloc[i, 2], file1.iloc[i, 3]),
#                                          file2.iloc[j, 0], (file2.iloc[j, 2], file2.iloc[j, 3])]
#                 print('i:%d j:%d' % (i, j))
#                 # print(trips.loc[len(trips)-1])
#             i += 1
#             j += 1

from geopy.distance import geodesic
# print(geodesic((30.28708,120.12802999999997), (28.7427,115.86572000000001)).m) #计算两个坐标直线距离
# print(geodesic((30.28708,120.12802999999997), (28.7427,115.86572000000001)).km) #计算两个坐标直线距离

def calDis(x):
    return geodesic((x.slat, x.slon), (x.elat, x.elon)).m

## st: start time, ss: start_site, et: end_time, es: end site
for i in range(1, 8):
    trips = pd.DataFrame(columns=['st', 'ID', 'slon', 'slat', 'et', 'elon', 'elat'])
    day_path = save_path + '2018090' + str(i) +'\\'
    file_list = os.listdir(day_path)
    n = len(file_list)
    # for a, b in zip(file_list[:-1], file_list[1:]):
    for a in range(0, n-2, 2):
        print(file_list[a])
        file1, file2 = pd.read_csv(day_path + file_list[a]), pd.read_csv(day_path + file_list[a+2])
        data = pd.merge(file1, file2, how='inner', on='ID')
        data = data[(data.lon_x != data.lon_y) | (data.lat_x != data.lat_y)]
        data.columns = ['st', 'ID', 'slon', 'slat', 'et', 'elon', 'elat']
        trips = pd.concat([trips, data])

    trips['distance'] = trips.apply(calDis, axis=1)
    trips.to_csv(day_path[:-1] + '_trips_20', index=False)
