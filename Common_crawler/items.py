# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerScrapyItem(scrapy.Item):
    '''定义需要格式化的内容（或是需要保存到数据库的字段）'''
    # define the fields for your item here like:
    # name = scrapy.Field()
    log_Title = scrapy.Field()
    log_Intro = scrapy.Field()
    log_Content = scrapy.Field()
