#coding=utf-8

import scrapy
import re
import requests
import time
import random
from bs4 import BeautifulSoup as bs
from scrapy.http import Request
from Common_crawler.items import WebcrawlerScrapyItem


class Common_crawlerSpider(scrapy.spiders.Spider):
    '''
        爬虫依据：分析脚本之家链接，发现链接有共同的特征：
        http://www.jb51.net/article/" + 页数 + ".htm
        知道这个特点我们就可以好好利用一下，减轻敲代码的负担
        做一个简单的爬虫。
    '''
    name = 'Common_crawler'
    allowed_domains = ["jb51.net"]
    start_urls = [
        "http://www.jb51.net/article/8.htm"
    ]
    print('请勿使用爬虫程序爬取网站受保护内容， 否则可能触犯相关法律律法规。')
    # 设置爬取的页数
    # 测试时请注意：切记，仅作学习爬虫测试，请求不要太频繁，照顾一下对方的服务器。
    # end_page = 10000
    end_page = 15 # 开发模式爬取前15个页面作为分析
    count = 1
    while count <= end_page:
        count = count + 1
        link = "http://www.jb51.net/article/" + str(count) + ".htm"
        start_urls.append(link)

    def start_requests(self):
        for url in self.start_urls:
            # proxy = self.get_proxy()
            # self.getHtml2(url,proxy)
            yield Request(url,callback=self.parse)

    def getHtml2(self,url,proxy):
        response = requests.get(url, proxies={"http": "http://{}".format(proxy.decode())})
        print(response)


    count = 0
    def parse(self,response):
        '''
        爬取页面结束后会执行这个解析函数，
        我们可以在这里提取到想要的东西保存到数据库：
        例如：我们现在先提取文章标题、文章简介、文章内容；
        如果有需要，还可以提取发表时间，作者之类的来做数据分析。
        :param response:
        :return:
        '''
        self.logger.info('thr url is :%s', response.url)
        if response.status == 200:
            # 解决中文乱码
            # response.encoding = 'gb2312'
            soup = bs(response.text, 'html.parser')
            # 指定文档编码，和网页保持一致
            soup.encode('gb2312')
            storage_title = soup.title.string
            # 去掉网站原本标题填充的标识
            storage_title = storage_title[0:len(storage_title) - 5]
            # 获取主要内容并去掉广告
            main_content = soup.select('#content')
            storage_item = WebcrawlerScrapyItem()
            main_content_result = self.delete_ad(main_content)
            # 获取简介
            word = soup.find_all(text=re.compile('脚本之家')) # 去掉脚本之家包含的字符串
            for single in word:
                single_null = re.sub('脚本之家',' ',single)
            meta = soup.findAll('meta',attrs={'name':True})
            # 提取文章中的简介
            for m in meta:
                if m.get('name') == "description":
                    storage_item["log_Intro"] = m.get('content')
                    break
            # 实例化字符对象，获取文章标题
            storage_item["log_Title"] = storage_title
            # 获取文章内容
            storage_inport = main_content_result[0].__str__()
            storage_item["log_Content"] = storage_inport

            # yield 用于自动保存到mysql数据库
            yield storage_item

        else:
            return ' '


    def delete_ad(self,param):
        '''
            删除网页中的广告包含的HTML标签
            你知道的，脚本之家广告真的很多很烦。。。。。
            对爬取的东西进行清洗
        '''
        arr = ['.art_xg','.lbd','.xgcomm','script','.tags','#shoucang','#comments','.content-shequ','#right-share','iframe','.w350','.toolbar_item','.command_help','.help']
        for cont_i in param:
            for arr_i in arr:
                try:
                    remove = cont_i.select(arr_i)
                    for remove_i in remove:
                        remove_i.decompose()
                except:
                    print('==============error occur================')
        return param

    def __str__(self):
        return self.name



