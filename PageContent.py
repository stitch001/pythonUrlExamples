#coding:utf8
'''
Created on 2015年6月10日

@author: Stitch
'''

def pageDict(site):
    pageDict = {
        "chinanews.com":[
            "content" #content
        ],
        "http://news.163.com":[
            "h1#h1title", #title
            "div.ep-time-soure", #time&source
            'div#endText>p', #"content":
        ],
        "http://www.ithome.com":[
            "div.post_title", #title time&source
            "div#paragraph>p",
        ],
        "http://www.cnbeta.com":[
            "div.body>header", #title time source
            "div.introduction", #introduction
            "div.content", #content
            "div.commt_list", #comment
        ]
                       
                
    }
    return pageDict[site]  