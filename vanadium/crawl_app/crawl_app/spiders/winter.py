# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WinterSpider(CrawlSpider):
    name = 'winter'
    allowed_domains = ['http://digitalnasrbija.org']
    start_urls = ['http://http://digitalnasrbija.org/']


    custom_settings = {
       'FEED_URI' : 'tmp/milan.csv'
   }

    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield {'image_urls': [img_url]}
