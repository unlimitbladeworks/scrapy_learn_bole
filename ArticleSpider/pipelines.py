# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
# 文件操作的库,编码比普通的with open要好用
import codecs
import json
from scrapy.exporters import JsonItemExporter

import pymysql


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        # 打开json文件,进行写入操作
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 将item转为字典格式在转成str类型的 json格式
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_close(self, spider):
        self.file.close()


"""
spider解析速度超过入库速度,此种方法插入速度太慢,跟不上解析速度,commit时会阻塞
所以不用此种方法
"""


class MysqlPineline(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1', 'root', 'root123!', 'article_spider', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            INSERT INTO jobbole_article (title,url,create_time,fav_nums) 
            VALUES (%s,%s,%s,%s)
        """
        self.cursor.execute(insert_sql, (item['title'], item['url'], item['create_date'], item['fav_nums']))
        self.conn.commit()


class JsonExporterPipeline(object):
    # 调用scrapy 提供的json export 导出json文件
    def __init__(self):
        self.file = open('articleexporter.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ArticleImagePipeline(ImagesPipeline):
    # 重写该方法可从result中获取到图片的实际下载地址
    def item_completed(self, results, item, info):
        image_file_path = ''
        for ok, value in results:
            image_file_path = value["path"]
        item['front_image_path'] = image_file_path
        return item
