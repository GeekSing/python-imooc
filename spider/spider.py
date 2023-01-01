# -*- coding: utf-8 -*-
import requests
import re
from bs4 import  BeautifulSoup

# �ϵ����
class Spider():
    url = 'https://live.kuaishou.com/match'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        r = requests.get(Spider.url,headers=Spider.headers)
        # bytes
        return r.text

    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {'name':name,'number':number}
            anchors.append(anchor)
        a = 1
        return anchors

    def __refine(self,anchors):
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
        }
        return map(l,anchors)
    
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine())
        self.__analysis(htmls)

spider = Spider()
spider.go()
    
