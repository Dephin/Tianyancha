#! /usr/local/bin/python3
#coding: utf-8

import requests
import urllib
import json
import hashlib

from bs4 import BeautifulSoup



class ScrawlUrls(object):
    """docstring for  Scrawler"""
    def __init__(
        self,
        cookie="",
        proxy=
    ):
        self.session = requests.session()
        # self.session.keep_alive = False
        self.headers = {
            'Host': 'www.tianyancha.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'https://www.tianyancha.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': cookie,
        }
        self.soup = None
        self.url_id = None
        self.proxies = None
        self.set_proxy()


        def req_get(self, url):
        resp = requests.get(url, headers=self.headers, proxies=self.proxies, timeout=10)
        return resp


    def parse_urls(self, page_no):
        if page_no == 1:
            url = "https://www.tianyancha.com/search?key=%E7%A7%91%E6%8A%80%E9%87%91%E8%9E%8D"
        else:
            url = "https://www.tianyancha.com/search/p" + str(page_no) + "?key=%E7%A7%91%E6%8A%80%E9%87%91%E8%9E%8D"

        resp = self.session.get(url)

        urls_soup = BeautifulSoup(resp.content, "html5lib")
        urls = []
        url_list = urls_soup.find_all('div', attrs={'class': 'search_result_single'})

        for li in url_list:
            url = li.find('a')['href']
            urls.append(url)

        return urls
