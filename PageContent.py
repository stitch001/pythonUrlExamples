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
        "netEaseNews":[
            "h1#h1title", #title
            "div.ep-time-soure", #time&source
            'div#endText>p', #"content":
        ],
        "ithomeNews":[
            "div.post_title", #title time&source
            "div#paragraph>p",
        ],
        "cnbetaNews":[
            "div.body>header", #title time source
            "div.introduction", #introduction
            "div.content", #content
            "div.commt_list", #comment
        ]
                       
                
    }
    return pageDict[site]  