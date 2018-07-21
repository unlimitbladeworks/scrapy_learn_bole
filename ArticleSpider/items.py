# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import datetime
import re

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.loader import ItemLoader


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


# 自定义ItemLoad,重载scrapy自带的ItemLoader
class ArticleItemLoad(ItemLoader):
    default_output_processor = TakeFirst()


# 正则提取收藏数字
def get_nums(value):
    match_re = re.match('.*(\d+).*', value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


# 自定义文章Item
class JobBoleArticleItem(scrapy.Item):
    """
    title = scrapy.Field(
        # 传入item时做的预处理参数
        input_processor=MapCompose(lambda x: x + '-jobbole', add_jobbole)
    )
    """
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
        # 此处注释,因为用到了自定义的ItemLoad,里面已经写了输出时的规范,list取出第一行
        # output_processor=TakeFirst()
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comments_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        #input_processor=MapCompose(get_nums),
        output_processor=Join(",")
    )
    content = scrapy.Field()
