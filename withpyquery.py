#coding:utf-8
'''
Created on 2015年6月7日

@author: Stitch
'''
from pyquery import PyQuery as pq
import PageContent
#url = "http://www.ithome.com"
#d('div.new-list-1>ul>li.new'

htmlheaderStr = ''' 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
'''
htmlDocEncode = 'UTF-8'
#baiduTopNews
def baiduNews():
    urlArray = []
    
    url = 'http://news.baidu.com'
    d = pq(url)
    topNews = d('div.hotnews>ul>li')
    
    len = topNews('li').length
    for i in range(len):
        hd = topNews.eq(i)
        if hd.find('strong').length > 0:
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

#NewEaseNews
def netEaseNews():
    urls = [];
    url = 'http://news.163.com'
    d = pq(url)
    children = d('div.ns-wnews.mb20').children()
    for child in children:
        a = d(child).find('a')
        if a.length >0 :
            urls.append(a.attr('href'))
    return urls
def cnbetaNews():
    urls = [];
    url = "http://www.cnbeta.com"
    selectorStr = "div#allnews_all>div.items_area"
    d = pq(url)
    children = d(selectorStr).children('div')
    for item in children:
        #print d(item)
        itemSub = d(item).find('div.hd')
        if itemSub.length > 0:
            urls.append(url + itemSub.find('div.title').find('a').attr('href'))
    return urls

def writeNewsToFile(url,contentSelectors,titleSelector):
    d = pq(url)
    htmlContent = ''
    for selector in contentSelectors:
        htmlItems = d(selector)
        for item in htmlItems:
            htmlContent += d(item).outer_html()
    files = open(url[-6:],'w+')
    files.write(htmlheaderStr.encode(htmlDocEncode))
    files.write(htmlContent.encode(htmlDocEncode))
    files.write('</html>'.encode(htmlDocEncode))
    files.flush()
    files.close()
    
#urls = netEaseNews()
#pageSelectors = PageContent.pageDict("news.163.com")

#urls = ithomeaNews()
#pageSelectors = PageContent.pageDict("www.ithome.com")

urls = cnbetaNews()
pageSelectors = PageContent.pageDict("http://www.cnbeta.com")
writeNewsToFile(urls[1],pageSelectors,None)