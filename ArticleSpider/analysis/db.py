# coding = utf-8

"""
@author: sy

@file: db.py

@time: 2018/11/15 21:08

@desc: 自定义脱离scrapy 数据库模块

"""

import pymysql
from twisted.enterprise import adbapi


class MysqlDb(object):
    def __init__(self, db_pool):
        self.db_pool = db_pool

    # 声明函数,scrapy会将settings的文件内容读取进来
    @classmethod
    def from_settings(cls, settings):
        # 将settings中的参数作为dict传入连接池中,dict的key需要和pymysql的Connection对应
        db_params = dict(
            host=settings['MYSQL_HOST'],
            database=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )

        db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        return cls(db_pool)

    # 使用Twisted 将mysql插入变成异步操作
    def process_item(self):
        query = self.db_pool.runInteraction(self.do_insert)
        # 添加自己的处理异常的函数
        query.addErrback(self.handle_error)

    # 处理插入异常
    def handle_error(self, failure):
        print(failure)

    # 执行具体的插入逻辑
    def do_insert(self, cursor):
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)
