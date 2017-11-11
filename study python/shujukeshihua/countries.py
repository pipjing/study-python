# coding:utf8
from pygal_maps_world.i18n import COUNTRIES
import matplotlib.pyplot as plt
# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])



