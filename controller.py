#! /usr/local/bin/python3
# coding: utf-8
import time
import requests
import json

from config import cookies, db_conf
from mysql import Mysql
from parser import Parser
from scrawller import Scrawller


class Controller(object):
	def __init__(self):
		self.db = Mysql(**db_conf)
		self.scrawller = Scrawller()
		self.parser = Parser()
		proxies = self.get_proxies()
		self.scrawller.set_cookie(cookies[0])
		self.scrawller.set_proxies(proxies)

	def get_proxies(self):
		url = "http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=3873239366fb4548a227fcbf310862ba&count=1&expiryDate=0&format=1&newLine=2"
		resp = requests.get(url)
		if resp.status_code == 200:
			resp_json = json.loads(resp.text)
			proxy_ip = resp_json['msg'][0]['ip']
			proxy_port = resp_json['msg'][0]['port']
			proxy_meta = "%(ip)s:%(port)s" % {
				"ip": proxy_ip,
				"port": proxy_port,
			}
			proxies = {
				"http": "http://" + proxy_meta,
				"https": "https://" + proxy_meta,
			}
			print("Connect: Set Proxy %s" % proxy_meta)
			print()
			return proxies
		else:
			raise Exception

	def get_url(self):
		data = self.db.select("SELECT url_id,url FROM urls WHERE flag=0 ORDER BY url_id LIMIT 1;")
		url_id = data[1][0]
		url = data[1][1]
		return url_id, url

	def insert_data(self, company_data, corporate_data, finacing_data):
		if (len(company_data) > 1) and (len(corporate_data) > 1) and (len(finacing_data) > 1):
			self.db.update('DELETE FROM company_info WHERE url_id=%d;' % url_id)
			self.db.update('DELETE FROM corporate_info WHERE url_id=%d;' % url_id)
			self.db.update('DELETE FROM finacing_info WHERE url_id=%d;' % url_id)
			print('Database: Initiliaze Data')

			self.db.insert('company_info', company_data)
			print('Database: Inserted Company Data')
			self.db.insert('corporate_info', corporate_data)
			print('Database: Inserted Corporate Data')
			self.db.insert('finacing_info', finacing_data)
			print('Database: Inserted Finacing Data')
			self.db.update("UPDATE urls SET flag=1 WHERE url_id=%s" % url_id)
			print()
			print('----------------------------------------------------------------------')

	def init(self):
		url_id, url = self.get_url()
		self.parser.init(url_id, url)

	def get_company_data(self):
		if self.parser.company_link:
			url = self.parser.company_link
			resp = self.scrawller.req_get(url)
			if resp.status_code == 200:
				company_data = self.parser.parse_company_info(resp)
				return company_data
			else:
				proxies = self.get_proxies()
				self.scrawller.set_proxies(proxies)

	def get_corporate_data(self):
		if self.parser.corporate_link:
			url = self.parser.corporate_link
			resp = self.scrawller.req_get(url)
			if resp.status_code == 200:
				corporate_data = self.parser.parse_corporate_info(resp)
				return corporate_data
			else:
				proxies = self.get_proxies()
				self.scrawller.set_proxies(proxies)

	def get_finacing_data(self):
		if self.parser.finacing_link:
			url = self.parser.finacing_link
			resp = self.scrawller.req_get(url)
			if resp.status_code == 200:
				finacing_data = self.parser.parse_finacing_info(resp)
				return finacing_data
			else:
				proxies = self.get_proxies()
				self.scrawller.set_proxies(proxies)

	def run(self):
		self.init()

		while True:
			try:
				company_data = self.get_company_data()
				break
			except:
				continue

		time.sleep(1)

		while True:
			try:
				corporate_data = self.get_corporate_data()
				break
			except:
				continue

		time.sleep(1)

		finacing_data = self.get_finacing_data()
		time.sleep(1)

		print(company_data, corporate_data, finacing_data)
# self.insert_data(company_data, corporate_data, finacing_data)
