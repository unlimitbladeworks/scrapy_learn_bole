初识Scrapy(慕课学习笔记)--初学者教程
===
初次学习Scrapy爬虫框架----抓取伯乐在线相关文章

项目环境:
- python3
- Anaconda(可选)
- Scrapy库

另:Scrapy库官方文档----

https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html

----
## 第一步
创建一个Scrapy项目的文件夹--scrapy_learn_bole

进入目录中,执行命令:

`cd scrapy_learn_bole`

## 第二步

执行命令:

`scrapy startproject ArticleSpider`

创建目录如下:

scrapy_learn_bole/
    scrapy.cfg

    ArticleSpider/
        __init__.py

        items.py

        pipelines.py

        settings.py

        spiders/
            __init__.py
            ...