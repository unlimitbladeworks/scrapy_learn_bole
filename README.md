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
# 创建项目
## 第一步
创建一个Scrapy项目的文件夹--scrapy_learn_bole

进入目录中,执行命令:

`cd scrapy_learn_bole`

## 第二步

执行命令:

`scrapy startproject ArticleSpider`

创建目录如下:

```
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
```
创建scrapy工程后,具体骨架有了,但是还需要我们使用基础模板生成一个py爬虫文件,请看第三步.

## 第三步

进入ArticleSpider目录,执行命令:

`cd ArticleSpider`

进入后,执行命令:

`scrapy genspider jobbole blog.jobble.com`

随后在spiders目录下生成了属于我们自己的py爬虫文件--jobbole.py

----

# 爬取网站

## 第一步

当写完自定义的爬虫文件后,启动scrapy的命令如下:

`scrapy crawl jobbole`

## 第二步

调试小技巧:

查看代码中的main.py,如果我们想打断点调试scrapy项目,从main.py入手debug即可.

原理:

```
# 利用scrapy类似cmd/shell,通过代码实现启动
from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole"])
```