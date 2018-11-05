# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/subject/24852545/comments?sort=new_score&status=P']

    def parse(self, response):
        pass
