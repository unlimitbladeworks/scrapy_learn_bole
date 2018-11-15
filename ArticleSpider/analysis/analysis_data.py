# coding = utf-8

"""
@author: sy

@file: analysis_data.py

@time: 2018/11/15 20:36

@desc: 对爬取下来的数据进行数据分析统计

"""
import jieba
import wordcloud
import pyecharts
from scrapy.utils.project import get_project_settings

from analysis.sql_items import DouBanSqlItems
from .db import MysqlDb

from twisted.internet import reactor

class AnalysisData(object):

    def __init__(self):
        """ 初始化获取mysql数据库中的相对数据"""
        setting = get_project_settings()
        mysqlDb = MysqlDb.from_settings(setting)
        douBanSqlItems = DouBanSqlItems()
        query_result = mysqlDb.process_item_interaction(douBanSqlItems)
        query_result.addCallback(self.word_count)
        reactor.run()


    def word_count(self,data):
        # todo 词频统计分析
        if data:
            for short_comments in data:
                print(short_comments)
        pass

    def draw_picture(self):
        # todo pyecharts画图
        pass
