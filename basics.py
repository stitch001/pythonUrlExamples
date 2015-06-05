#coding:utf8
'''
Created on 2015年6月5日
@author: stitch
'''
# 1.导入包

import urllib2
import urllib

url = 'http://cn.bing.com'
'''
# 2.直接发送url请求
response = urllib2.urlopen(url)
repstr = response.read()

# 3.使用request发送请求
request = urllib2.Request(url)
response = urllib2.urlopen(request)
repstr = response.read()
'''
# 3.加入请求参数和UA(user Agent)
url2 = url+'/search?'
values = {'q':'123'}
data = urllib.urlencode(values)
request = urllib2.Request(url2+data)
response = urllib2.urlopen(request)

# 4.加入UserAgent

f1 = open('re.html','w+')
f1.write(response.read())
f1.flush()
f1.close()
