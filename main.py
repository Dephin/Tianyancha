#! /usr/local/bin/python3
#coding: utf-8

import time

from scrawler import Scrawler
from mysql import Mysql
from config import web_conf, db_conf



def save_urls():
	db = Mysql(**db_conf)
	scrawler = Scrawler(**web_conf)

	for page_num in range(1, 251):
		data = [['url', 'page_num', 'flag']]
		urls = scrawler.parse_urls(page_num)
		for url in urls:
			data.append([url, page_num, '0'])
		db.insert_ignore('urls', data)
		time.sleep(2)

def save_contents(n, period):
	db = Mysql(**db_conf)
	scrawler = Scrawler(**web_conf)

	count = 0
	for i in range(0, 1000):
		data = db.select("SELECT url_id,url FROM urls WHERE flag=0 ORDER BY url_id LIMIT 1;")
		url_id = data[1][0]
		url = data[1][1]
		scrawler.parse_url_content(url, url_id)
		print(url)
		time.sleep(2)
		company_data = scrawler.parse_company_info()
		time.sleep(2)
		corporate_data = scrawler.parse_corporate_info()
		time.sleep(2)
		finacing_data = scrawler.parse_finacing_info()
		time.sleep(2)

		if (len(company_data) > 1) and (len(corporate_data) > 1) and (len(finacing_data) > 1):
			db.update('DELETE FROM company_info WHERE url_id=%d;' % url_id)
			db.update('DELETE FROM corporate_info WHERE url_id=%d;' % url_id)
			db.update('DELETE FROM finacing_info WHERE url_id=%d;' % url_id)
			db.insert('company_info', company_data)
			db.insert('corporate_info', corporate_data)
			db.insert('finacing_info', finacing_data)
			db.update("UPDATE urls SET flag=1 WHERE url_id=%s" % url_id)

		count += 1

		if count == n:
			time.sleep(period)

if __name__ == '__main__':
	save_contents(30, 30)


