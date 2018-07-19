# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import datetime

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_jobbole(value):
    return value + '-suyu'


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, '%Y/%m%d').date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date


# 自定义文章Item
class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field(
        # 传入item时做的预处理参数
        input_processor=MapCompose(lambda x: x + '-jobbole', add_jobbole)
    )
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
        output_processor=TakeFirst()
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field()
    comments_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
