import os
import numpy as np
import pandas as pd
# jt -t monokai -f ubuntu -fs 14 -lineh 120 -ofs 10 -cellw 1500
pd.set_option('display.width',1000)

test_path = 'D:\\data\\Metro\\Metro_testA\\'
train_path = 'D:\\data\\Metro\\Metro_train\\'
out_path = 'D:\\data\\Metro\\midData\\'
f = os.listdir(train_path)

#exact trips

for i in f:
    print(i)
    data = pd.read_csv(train_path + i)
    data = data.sort_values(by=['userID', 'time']).reset_index(drop=True)
    data = data.drop_duplicates()
#     print(data.loc[:20])
    trips = pd.DataFrame(columns=['UID', 'PY', 'iT', 'iLID', 'iSID', 'iDID', 'oT', 'oLID', 'oSID', 'oDID'])
    n = len(data)
    for j in range(0, n):
        print(j)
        if data.loc[j].status == 0 or j == n or data.loc[j+1].status == 1 or data.loc[j].userID != data.loc[j+1].userID:
            continue
        trips.loc[len(trips)] = [data.loc[j].userID, data.loc[j].payType, data.loc[j].time, data.loc[j].lineID,
                                  data.loc[j].stationID, data.loc[j].deviceID, data.loc[j+1].time, data.loc[j+1].lineID,
                                   data.loc[j+1].stationID, data.loc[j+1].deviceID]
        # print(trips.loc[len(trips)-1])
    trips.to_csv(out_path + i.split('_')[1].split('.')[0] + '_trips.csv')
