# -*- coding: utf-8 -*-
from urllib import parse

import scrapy
from scrapy import Request

from items import DouBanItem, DouBanItemLoad


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/subject/24852545/comments?sort=new_score&status=P']
    #start_urls = ['https://movie.douban.com/review/best/']

    def parse(self, response):
        """ 交给parse_details 进行处理 """
        comment_nodes = response.css('mod-bd')
        for _ in comment_nodes:
            yield Request(callback=self.parse_details)

        # 提取下一页交给scrapy进行下载
        next_page = response.css('.next::attr(href)').extract_first('')
        if next_page:
            yield Request(url=parse.urljoin(response.url, next_page), callback=self.parse)

    def parse_details(self, response):
        """ 解析爱情公寓具体短评论 """
        item_loader = DouBanItemLoad(item=DouBanItem(), response=response)
        item_loader.add_css('douban_url', '//*[@id="comments"]/div[1]/div[2]/h3/span[2]/a/text()')

        pass
