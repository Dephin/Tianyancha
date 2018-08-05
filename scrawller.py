#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : scrawler.py
# @Author  : dephin
# @File    : 2018/7/7

import requests

class Scrawller(object):
	req_num = 0

	def __init__(self):
		self.headers = {
			'Host': 'www.tianyancha.com',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Referer': 'https://www.tianyancha.com/',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'zh-CN,zh;q=0.9',
		}
		self.url = None
		self.__url_id = None
		self.proxies = None

	def set_cookie(self, cookie):
		self.headers['cookie'] = cookie
		print("Connect: Reset Cookie")

	def set_proxies(self, proxies):
		self.proxies = proxies
		print("Connect: Set Proxies %s" % proxies["https"])

	def req_get(self, url):
		resp = requests.get(url, headers=self.headers, proxies=self.proxies, timeout=10)
		if resp.status_code == 200:
			Scrawller.req_num += 1
		return resp


