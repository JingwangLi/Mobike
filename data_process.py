# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 23:25
# @Author  : Jingwang Li
# @Email   : jingwanali@gmail.com
# @Blog    : www.jingwangl.com

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cm

# 绘制基础地图，选择绘制的区域，因为是绘制美国地图，故选取如下经纬度，lat_0和lon_0是地图中心的维度和经度

map = Basemap(projection='stere',lat_0=90,lon_0=-105,\
            llcrnrlat=23.41 ,urcrnrlat=45.44,\
            llcrnrlon=-118.67,urcrnrlon=-64.52,\
            rsphere=6371200.,resolution='l',area_thresh=10000)
# map = Basemap(projection='stere',
#               lat_0=0, lon_0=280,
#               llcrnrlon=73.33,
#               llcrnrlat=3.51,
#               urcrnrlon=112.16,
#               urcrnrlat=53.123)

map.drawmapboundary()   # 绘制边界
#map.fillcontinents()   # 填充大陆，发现填充之后无法显示散点图，应该是被覆盖了
map.drawstates()        # 绘制州
map.drawcoastlines()    # 绘制海岸线
map.drawcountries()     # 绘制国家
# map.drawcounties()      # 绘制县

parallels = np.arange(0.,90,10.)
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10) # 绘制纬线

meridians = np.arange(-110.,-60.,10.)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) # 绘制经线

plt.title('Population distribution in America')
plt.show()