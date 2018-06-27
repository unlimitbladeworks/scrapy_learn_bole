# -*- coding: utf-8 -*-
import scrapy
import re


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    # start_urls = ['http://blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/112048/']

    def parse(self, response):

        """
        1. 获取文章列表的url进行解析
        2. 获取下一页的url并交给scrapy下载,完成后交给parse
        """
        # 解析列表页中的所有文章url并交给scrapy下载后解析
        post_urls = response.css('.floated-thumb .post-thumb a::attr(href)')
        for post_url in post_urls:
            print(post_url)

        """ --------------    css   案例 start    --------------"""
        # 标题  extract_first()防止数组越界
        article_title_css = response.css('div.entry-header h1::text').extract_first()

        # 时间
        article_time_css = response.css('p.entry-meta-hide-on-mobile::text').extract_first().strip().replace(
            '·', '').strip()

        # 点赞数
        article_praise_css = response.css('#112048votetotal::text').extract_first()

        # 收藏数
        bookmark_css = response.css(
            '.btn-bluet-bigger.href-style.bookmark-btn.register-user-only::text').extract_first()
        # 正则提取收藏数字
        match_bookmark_css = re.match('.*(\d+).*', bookmark_css)
        if match_bookmark_css:
            article_bookmark_css = match_bookmark_css.group(1)
            print(article_bookmark_css)

        # 评论数
        comments_css = response.css('a[href="#article-comment"] span::text').extract_first()
        match_comments_css = re.match('.*(\d+).*', comments_css)
        if match_comments_css:
            article_comments_css = match_comments_css.group(1)
            print(article_comments_css)
        # 文章详情
        article_contents_css = response.css('.entry').extract()[0]

        # 文章标签
        tag_list_css = response.css('p.entry-meta-hide-on-mobile a::text').extract()
        # 去重标签
        tag_list_css = [element for element in tag_list_css if not element.strip().endswith("评论")]
        tags_css = ','.join(tag_list_css)
        print(tags_css)

        """ --------------    css   案例 end    --------------"""
