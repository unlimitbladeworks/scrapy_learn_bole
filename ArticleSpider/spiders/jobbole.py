# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request
from urllib import parse
from ArticleSpider.items import JobBoleArticleItem


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    # start_urls = ['http://blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):

        """
        1. 获取文章列表的url进行解析
        2. 获取下一页的url并交给scrapy下载,完成后交给parse
        """
        # 解析列表页中的所有文章url并交给scrapy下载后解析
        post_nodes = response.css('#archive .floated-thumb .post-thumb a').extract()
        for post_node in post_nodes:
            # 抓取所有列表的首页图片
            image_url = post_node.css('img::attr(src)').extract_first('')
            post_url = post_node.css('::attr(href)').extract_first('')

            # 通过yield 交给scrapy处理
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url},
                          callback=self.parse_detail)

        # 提取下一页交给scrapy进行下载
        next_url = response.css('.next.page-numbers::attr(href)').extract_first()
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    # 提取文章具体逻辑(文章详情)
    def parse_detail(self, response):
        # 实例化一个jobboleitem
        article_item = JobBoleArticleItem()

        # 获取meta,获取到Request的封面图提取出来
        front_image_url = response.meta.get('front_image_url', '')

        """ --------------    css   案例 start    --------------"""
        # 标题  extract_first()防止数组越界
        article_title_css = response.css('div.entry-header h1::text').extract_first('')

        # 时间
        article_time_css = response.css('p.entry-meta-hide-on-mobile::text').extract_first('').strip().replace(
            '·', '').strip()

        # 点赞数
        article_praise_css = response.css('#112048votetotal::text').extract_first('')

        # 收藏数
        bookmark_css = response.css(
            '.btn-bluet-bigger.href-style.bookmark-btn.register-user-only::text').extract_first('')
        # 正则提取收藏数字
        match_bookmark_css = re.match('.*(\d+).*', bookmark_css)
        if match_bookmark_css:
            article_bookmark_css = int(match_bookmark_css.group(1))
            print(article_bookmark_css)
        else:
            article_bookmark_css = 0

        # 评论数
        comments_css = response.css('a[href="#article-comment"] span::text').extract_first('')
        match_comments_css = re.match('.*(\d+).*', comments_css)
        if match_comments_css:
            article_comments_css = int(match_comments_css.group(1))
            print(article_comments_css)
        else:
            article_comments_css = 0
        # 文章详情
        article_contents_css = response.css('.entry').extract()[0]

        # 文章标签
        tag_list_css = response.css('p.entry-meta-hide-on-mobile a::text').extract()
        # 去重标签
        tag_list_css = [element for element in tag_list_css if not element.strip().endswith("评论")]
        tags_css = ','.join(tag_list_css)
        print(tags_css)

        """ --------------    css   案例 end    --------------"""

        article_item["title"] = article_title_css
