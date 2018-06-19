# -*- coding: utf-8 -*-
import scrapy
import re


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    # start_urls = ['http://blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/112048/']

    def parse(self, response):
        # 标题
        article_title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        # 时间
        article_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace(
            '·', '').strip()
        # 点赞数
        article_praise = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]
        # 收藏数
        bookmark = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        # 正则提取收藏数字
        match_bookmark = re.match('.*(\d+).*', bookmark)
        if match_bookmark:
            article_bookmark = match_bookmark.group(1)
        # 评论数
        comments = response.xpath('//a[@href="#article-comment"]/text()').extract()[0]
        match_comments = re.match('.*(\d+).*', bookmark)
        if match_comments:
            article_comments = match_comments.group(1)

        pass
