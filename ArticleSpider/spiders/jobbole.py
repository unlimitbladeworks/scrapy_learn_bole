# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    # start_urls = ['http://blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/114132/']

    def parse(self, response):
        re_selector = response.xpath('//div[@class="entry-header"]/h1')
        pass
