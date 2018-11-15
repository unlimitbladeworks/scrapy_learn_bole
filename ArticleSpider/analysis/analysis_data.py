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

from .db import MysqlDb


class AnalysisData(object):
    def get_data(self):
        """ 获取mysql数据库中的相对数据"""
        setting = get_project_settings()
        mysqlDb = MysqlDb.from_settings(setting)
        mysqlDb.process_item()

    def word_count(self):
        # todo 词频统计分析

        pass

    def draw_picture(self):
        # todo pyecharts画图
        pass
