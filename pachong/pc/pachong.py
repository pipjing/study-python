# coding:utf8
import urllib
import urllib2
import re

def get_video(page):
    req = urllib2.Request('http://www.budejie.com/')
    req.add_header("user-agent","Mozilla/5.0")
    html = urllib2.urlopen(req).read()
    reg = r'data-mp4="(.*?)"'
    for i in re.findall(reg,html):
        filename = i.split("/")[-1]#分割文件名
        print '正在下载%s' %filename
        urllib.urlretrieve(i,"mp4/%s" %filename)#下载

for i in range(1,3):
    get_video(i)

