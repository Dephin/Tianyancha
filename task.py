#! /usr/local/bin/python3
#coding: utf-8

import requests
import json

from parse_contents import ParseContents
from mysql import Mysql


class Task(object):
    """docstring for Task"""
    def __init__(self, db_conf={}):
        self.db = Mysql(**db_conf)

    def get_proxies(self):
        url = "http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=3873239366fb4548a227fcbf310862ba&count=1&expiryDate=0&format=1&newLine=2"
        resp = requests.get(url)
        if resp.status_code == 200:
            resp_json = json.loads(resp.text)
            proxy_ip = resp_json['msg'][0]['ip']
            proxy_port = resp_json['msg'][0]['port']
            proxy_meta = "%(ip)s:%(port)s" % {
                "ip" : proxy_ip,
                "port" : proxy_port,
            }
            proxies = {
                "http"  : "http://" + proxy_meta,
                "https" : "https://" + proxy_meta,
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
        return url, url_id


    def insert_data(self, url, url_id, company_data, corporate_data, finacing_data):
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


    def run(self, proxies, cookie):
        s = ParseContents()
        url, url_id = self.get_url()
        s.set_url(url)
        s.set_url_id(url_id)
        s.set_proxies(proxies)
        s.set_cookie(cookie)
        company_data, corporate_data, finacing_data = s.parse()
        self.insert_data(url, url_id, company_data, corporate_data, finacing_data)






