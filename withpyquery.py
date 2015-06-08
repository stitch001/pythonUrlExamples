#coding:utf-8
'''
Created on 2015年6月7日

@author: Stitch
'''
from pyquery import PyQuery as pq
#url = "http://www.ithome.com"
#d('div.new-list-1>ul>li.new'
htmlheaderStr = ''' 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
'''
#baiduTopNews
def baiduNews():
    urlArray = []
    
    url = 'http://news.baidu.com'
    d = pq(url)
    topNews = d('div.hotnews>ul>li')
    
    len = topNews('li').length
    for i in range(len):
        hd = topNews.eq(i)
        if hd.find('strong'):
            urlArray.append(topNews.eq(i)('strong>a').attr('href'))
        else:
            urlArray.append(topNews.eq(i)('a').attr('href'))

    return urlArray

#ithomeNews

def ithomeNews():
    
    url = 'http://www.ithome.com'
    d = pq(url)
    uls = d('div.new-list-1>ul')
    urlArrays = []
    for i in range(0,6,2):
        liUrl = uls.eq(i)('li.new')
        for j in range(liUrl.length): 
            urlArrays.append(liUrl.eq(j)('span>a').attr('href'))
    return urlArrays

def writeNewsToFile(url,contentSelector,titleSelector):
    d = pq(url)
    contentElement = d(contentSelector)
    title = contentElement(contentSelector).html()
    files = open(url[-5:],'w+')
    files.write(htmlheaderStr.encode('utf-8'))
    files.write(contentElement.html().encode('utf-8'))
    files.write('</html>'.encode('utf-8'))
    files.flush()
    files.close()
    
urls = ithomeNews()
writeNewsToFile(urls[0], 'div.content', 'h1')