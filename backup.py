'''
# #coding=utf-8
# import scrapy
# import re
# import os
# import urllib
# import pymysql
# import sys
# import numpy as np
# import datetime
# import requests
# import json
# import time
# import random
# from lxml import etree
# from bs4 import BeautifulSoup as bs
# from scrapy.spider import CrawlSpider
# from scrapy.selector import Selector
# from scrapy.http import Request
# from youyong.items import WebcrawlerScrapyItem
# from youyong.nameData import getname_in_chinese
#
#
#
# class youyongSpider(scrapy.spiders.Spider):
#     name = 'youyong'
#     start_urls = [
#         "http://www.ps288.com/zhishitiku/"
#     ]
#     end_page = 33
#     # for next_page in range(2,end_page):
#     #     link = "http://www.ps288.com/wangluojishu/index_" + str(next_page) + ".html"
#     #     # link = "http://www.ps288.com/zhishitiku/index_" + str(next_page) + ".html"
#     #     start_urls.append(link)
#     count = 1
#     while count <= end_page:
#         count = count + 1
#         link = "http://www.ps288.com/zhishitiku/index_" + str(count) + ".html"
#         start_urls.append(link)
#
#     def start_requests(self):
#         for url in self.start_urls:
#             yield Request(url=url, callback=self.parse)
#     count = 0
#     def parse(self,response):
#         selector = Selector(response)
#         self.log('爬取页数： %s' % self.count)
#         ulli = selector.xpath('body/div[@class="wrap"]/div[@id="news_list"]/ul/li')
#         articlearr = []
#         for list in ulli:
#             articlearr.append({
#                 "href": list.css('a::attr("href")').extract_first()
#             })
#
#         for load_item in articlearr:
#             pre_href = re.search(r'www.ps', load_item["href"], re.M | re.I)
#             if pre_href is not None:
#                 href = load_item["href"]
#             else:
#                 href = 'http://www.ps288.com' + load_item["href"]
#             response = requests.get(href)
#             if response.status_code == 200:
#                 # 解决中文乱码
#                 response.encoding = 'gb2312'
#                 soup = bs(response.text, 'html.parser')
#                 soup.encode('gb2312')
#                 storage_title = soup.title.string
#                 # 去掉网站原本标题填充的标识
#                 storage_title = storage_title[0:len(storage_title) - 4]
#                 main_content = soup.select('#content')
#                 main_content_result = self.delete_ad(main_content)
#                 storage_item = WebcrawlerScrapyItem()
#                 storage_item["log_Title"] = storage_title
#                 storage_inport = main_content_result.__str__()
#                 storage_item["log_Intro"] = storage_inport
#                 storage_item["log_Content"] = storage_inport
#                 name = getname_in_chinese().getname()
#                 storage_item["log_Meta"] = 'a:6:{s:14:"Blogs_suoluetu";s:15:"";s:10:"Blogs_wzlx";s:1:"1";s:12:"Blogs_zuozhe";s:12:" %s";s:13:"Blogs_laiyuan";s:12:"互联网共享";s:10:"md_content";s:6:"正文";s:8:"md_intro";s:22:"正文<!--autointro-->";}}' % name
#                 storage_item["log_Template"] = 'page-full'
#                 storage_item["log_CateID"] = 4
#                 storage_item["log_AuthorID"] = 1
#                 storage_item['log_PostTime'] = int(time.time()) - int(random.randint(5000,100000))
#                 storage_item['log_ViewNums'] = int(random.randint(256,5000))
#                 storage_item['log_Tag'] = 7
#                 self.count = self.count + 1
#                 print('已爬取第 %s 篇文章' % self.count)
#
#                 yield storage_item
#
#
#     def delete_ad(self,param):
#         arr = ['.thea6','.thea7','script','.content','#prevnext','.correlative','.thea3','#meta','h1']
#         for cont_i in param:
#             for arr_i in arr:
#                 try:
#                     remove = cont_i.select(arr_i)
#                     for remove_i in remove:
#                         remove_i.decompose()
#                 except:
#                     print('==============发生错误================')
#         return param
#
#     def __str__(self):
#         return self.name
'''