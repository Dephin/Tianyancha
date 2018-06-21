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


def save_contents(period):
	db = Mysql(**db_conf)
	scrawler = Scrawler(**web_conf)

	count = 1
	for i in range(0, 1000):
		try:
			print('Task: No.%d Begin' % count)
			data = db.select("SELECT url_id,url FROM urls WHERE flag=0 ORDER BY url_id LIMIT 1;")
			url_id = data[1][0]
			url = data[1][1]
			scrawler.parse_url_content(url, url_id)
			company_data = scrawler.parse_company_info()
			time.sleep(3)
			corporate_data = scrawler.parse_corporate_info()
			time.sleep(3)
			finacing_data = scrawler.parse_finacing_info()
			time.sleep(3)

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
				print('Task: No.%d Compeleted' % count)
				print('----------------------------------------------------------------------')
				count += 1

			# if (count != 1) and ((count % 5) == 1):
			# 	print('Time Break: %d seconds' % period)
			# 	time.sleep(period)
			# 	print('----------------------------------------------------------------------')

		except Exception as e:
			print("[ERROR] %s" % e)
			raise e


def test():
	db = Mysql(**db_conf)
	scrawler = Scrawler(**web_conf)
	data = db.select("SELECT url_id,url FROM urls WHERE flag=0 ORDER BY url_id LIMIT 1;")
	url_id = data[1][0]
	url = data[1][1]
	scrawler.parse_url_content(url, url_id)
	company_data = scrawler.parse_company_info()
	time.sleep(3)
	corporate_data = scrawler.parse_corporate_info()
	time.sleep(3)
	finacing_data = scrawler.parse_finacing_info()



if __name__ == '__main__':
	# save_contents(20)
	test()


