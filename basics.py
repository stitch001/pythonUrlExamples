#coding:utf8
'''
Created on 2015年6月5日
@author: stitch
'''
# 1.导入包

import urllib2
import urllib

url = 'http://cn.bing.com'

# 2.直接发送url请求
response = urllib2.urlopen(url)
repstr = response.read()

# 3.使用request发送请求
request = urllib2.Request(url)
response = urllib2.urlopen(request)
repstr = response.read()

# 3.加入请求参数 使用GET方式传递参数
url2 = url+'/search?'
values = {'q':'123'}
data = urllib.urlencode(values)
request = urllib2.Request(url2+data)
response = urllib2.urlopen(request)

# 4.加入header(Accept cookies user-agent等信息)
#使用POST方法传递参数
'''
http://mail.163.com/js6/main.jsp?sid=gApTlovZMyLPSYTldJZZZevdOriMLvit&df=mail163_letter
'''
userAgent = '5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36'
url2 = 'http://mail.163.com/js6/main.jsp?'
values = {}
values['sid'] = 'gApTlovZMyLPSYTldJZZZevdOriMLvit'
values['df'] = 'mail163_letter'
headers = { 'User-Agent' : userAgent }
data = urllib.urlencode(values)
request=urllib2.Request(url=url2,data,headers)
response = urllib2.urlopen()

f1 = open('re.html','w+')
f1.write(response.read())
f1.flush()
f1.close()
