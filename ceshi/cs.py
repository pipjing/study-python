# coding:utf8
import urllib
import urllib2
import re
import urlparse

head_url = 'https://www.bilibili.com/video/kichiku.html'
req = urllib2.Request(head_url)
print req
html = urllib2.urlopen(req).read()
print html
reg = r'href="(/video/av+)"'
for i in re.findall(reg,html):
    print i
    new_full_url = urlparse.urljoin(head_url,i)
    print new_full_url
    filename = new_full_url.split("/")[-1]#分割文件名
    print '正在下载%s' %filename
    urllib.urlretrieve(new_full_url,"mp4/%s" %filename)#下载
