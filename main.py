#! /usr/local/bin/python3
#coding: utf-8

import time
import random

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


def test():
	db = Mysql(**db_conf)
	scrawler = Scrawler(**web_conf)
	scrawler.get_current_ip()

	count = 1
	error_num = 0
	req_num = 0
	for i in range(0, 1000):
		if req_num >= 40:
			scrawler.set_proxy()
			scrawler.set_cookie()
			req_num = 0

		print('Task: No.%d' % count)
		print()

		data = db.select("SELECT url_id,url FROM urls WHERE flag=0 ORDER BY url_id LIMIT 1;")
		url_id = data[1][0]
		url = data[1][1]

		while True:
			try:
				scrawler.parse_url_content(url, url_id)
				company_data = scrawler.parse_company_info()
				# time.sleep(1)
				break
			except:
				error_num += 1
				print("Connect: Refused By Server")
				print("Let me sleep for 5 seconds.")
				time.sleep(5)
				print("ZZzzz...")
				print("Was a nice sleep, now let continue.")
				scrawler.set_proxy()
				scrawler.set_cookie()
				if error_num >= 5:
					raise Exception
				else:
					error_num = 0
					continue

		while True:
			try:
				corporate_data = scrawler.parse_corporate_info()
				# time.sleep(1)
				break
			except:
				error_num += 1
				print("Connect: Refused By Server")
				print("Let me sleep for 5 seconds.")
				time.sleep(5)
				print("ZZzzz...")
				print("Was a nice sleep, now let continue.")
				scrawler.set_proxy()
				scrawler.set_cookie()
				if error_num >= 5:
					raise Exception
				else:
					error_num = 0
					continue

		while True:
			try:
				finacing_data = scrawler.parse_finacing_info()
				# time.sleep(1)
				break
			except:
				error_num += 1
				print("Connect: Refused By Server")
				print("Let me sleep for 5 seconds.")
				time.sleep(5)
				print("ZZzzz...")
				print("Was a nice sleep, now let continue.")
				scrawler.set_proxy()
				scrawler.set_cookie()
				if error_num >= 5:
					raise Exception
				else:
					error_num = 0
					continue

		if (len(company_data) > 1) and (len(corporate_data) > 1) and (len(finacing_data) > 1):
			db.update('DELETE FROM company_info WHERE url_id=%d;' % url_id)
			db.update('DELETE FROM corporate_info WHERE url_id=%d;' % url_id)
			db.update('DELETE FROM finacing_info WHERE url_id=%d;' % url_id)
			print('Database: Initiliaze Data')

			db.insert('company_info', company_data)
			print('Database: Inserted Company Data')
			db.insert('corporate_info', corporate_data)
			print('Database: Inserted Corporate Data')
			db.insert('finacing_info', finacing_data)
			print('Database: Inserted Finacing Data')
			db.update("UPDATE urls SET flag=1 WHERE url_id=%s" % url_id)
			print()
			print('----------------------------------------------------------------------')
			count += 1

		req_num += 3

		if count >= 120:
			print('Time Break: 60 seconds')
			time.sleep(60)
			print('----------------------------------------------------------------------')
			req_num = 0	



if __name__ == '__main__':
	# save_contents(20)
	test()


