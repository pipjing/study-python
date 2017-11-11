# coding:utf8
import matplotlib.pyplot as plt
import csv
from datetime import datetime
# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False




# 获取最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    highs = []
    lows = []
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# 设置格式
# 设置标题，加上坐标轴标签
plt.title(u"每日最高,低气温",fontsize=24)
plt.xlabel("Value",fontsize=16)
fig.autofmt_xdate() # 避免标签重合
plt.ylabel(u"气温(F)",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()

for index,column_header in enumerate(header_row):
    print(index,column_header)