# -*- coding:utf-8 -*-
import urllib
import urllib2
import re



user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
 
page = 1
url = 'http://wx.58.com/hunqing/31298129882421x.shtml?adtype=1&PGTID=0d30218c-0005-dc6c-b65e-66bd9e54aaf9&entinfo=31298129882421_0&adact=3&psid=104176713198115575322035148&iuType=q_2&ClickID=1' 
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

content_pattern = re.compile('<div class="mainTitle">.*?<h1>(.*?)</h1>', re.S)
content_list = re.findall(content_pattern, html)

for item in content_list:
    print item



content_pattern = re.compile('<div class="nav">.*?>(.*?)</a>', re.S)
content_list = re.findall(content_pattern, html)

for item in content_list:
    print item


content_pattern = re.compile('<div class="commodity_des">(.*?)</div>', re.S)
content_list = re.findall(content_pattern, html)

for item in content_list:
    print item


content_pattern = re.compile('<div class="item-btn clearfix">.*?>(.*?)</a>', re.S)
content_list = re.findall(content_pattern, html)

for item in content_list:
    print item

content_pattern = re.compile('<div class="commodity_tags clearfix">.*?>(.*?)</a>', re.S)
content_list = re.findall(content_pattern, html)

for item in content_list:
    print item
