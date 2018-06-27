# -*- coding: utf-8 -*-
"""
@author: sy

@file: spider_wiki.py

@time: 2018-06-27 20:56:53

@desc: search wiki

"""

import requests
from bs4 import BeautifulSoup as bs
from requests import RequestException


# get html source code
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        # 如果状态码等于200返回html源码
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    soup = bs(html, 'lxml')
    output = soup.find(name='div', attrs={'class': 'mw-parser-output'})
    p_list = output.find_all(name='p')
    for p_content in p_list:
        write_to_file(p_content.get_text())


def write_to_file(content):
    with open('wiki.txt', 'a', encoding='utf-8') as f:
        f.write(content + '\n')
        f.close()


def main():
    keyword = input('input what you want to search:\n')
    url = 'https://en.wikipedia.org/wiki/Special:Search?search=' + keyword + '&go=Go'
    html = get_one_page(url)
    parse_one_page(html)


if __name__ == '__main__':
    main()
