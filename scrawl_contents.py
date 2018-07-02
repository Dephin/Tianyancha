#! /usr/local/bin/python3
#coding: utf-8

import requests
import urllib
import json
import hashlib
import time

from bs4 import BeautifulSoup


class ScrawlContents(object):
    """docstring for  Scrawler"""
    def __init__(self):
        # self.session = requests.session()
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
        }
        self.soup = None
        self.url = None
        self.url_id = None
        self.proxies = None 

    SCRAWLER_NUM = 0

    @classmethod
    def build(cls, cookie, proxies):
        s = cls(cookies, proxies)
        cls.SCRAWLER_NUM += 1
        return s

    def set_cookie(self, cookie):
        self.headers['cookie'] = cookie
        print("Connect: Reset Cookie")

    def set_proxies(self, proxies):
        self.proxies = proxies
        print("Connect: Set Proxies %s" % proxies["https"])

    def set_url(self, url):
        self.url = url

    def set_url_id(self, url_id):
        self.url_id = url_id

    def req_get(self, url):
        resp = requests.get(url, headers=self.headers, proxies=self.proxies, timeout=10)
        return resp



    def parse_company_info(self):
        print('Connect: GET %s' % self.url)
        resp = self.req_get(self.url)

        print('Parsing: Company Info')
        print()
        self.soup = BeautifulSoup(resp.content, "html5lib")

        data = [['url_id', 'company_name', 'company_address', 'company_intro', 'company_status']]
        header = self.soup.find('div', attrs={'class': 'company_header_width'})
        company_name = header.h1.get_text()
        company_info = header.find_all('div', attrs={'class': ['f14', 'sec-c2']})
        company_address = company_info[1].contents[1].contents[1].get_text()
        company_intro = header.find('script', attrs={'id': 'company_base_info_detail'})
        if company_intro:
            company_intro = company_intro.get_text().strip()
        else:
            company_intro = '暂无信息'

        company_info2 = self.soup.find_all('div', attrs={'class': 'baseinfo-module-content-value'})
        if company_info2:
            company_status = company_info2[2].get_text()
        else:
            company_status = '暂无信息'

        data.append([self.url_id, company_name, company_address, company_intro, company_status])

        return data


    def parse_corporate_info(self):
        data = [['url_id', 'corporate_name', 'company_role', 'company_name', 'company_province', 'company_date', 'company_capital', 'company_status']]
        corporate_info = self.soup.find('div', attrs={'class': 'human-top'})

        if corporate_info and ('human' in corporate_info.a['href']):

            corporate_info = corporate_info.a
            corporate_name = corporate_info.get_text()
            corporate_link = corporate_info['href']
        
            print('Connect: GET %s' % corporate_link)
            resp = self.req_get(corporate_link)

            print('Parsing: Corporate Info')
            print()
            corporate_soup = BeautifulSoup(resp.content, "html5lib")
            companies = corporate_soup.find('div', attrs={'id': '_container_syjs'}).table.tbody.find_all('tr')

            for i in range(0,len(companies)):
                if companies[i].contents[0].contents[0].get_text():
                    company_role = companies[i].contents[0].contents[0].get_text()
                    company_name = companies[i].contents[1].contents[1].get_text()
                    company_province = companies[i].contents[2].get_text()
                    company_date = companies[i].contents[3].get_text()
                    company_capital = companies[i].contents[4].get_text()
                    company_status = companies[i].contents[5].get_text()
                else:
                    company_name = companies[i].contents[0].contents[1].get_text()
                    company_province = companies[i].contents[1].get_text()
                    company_date = companies[i].contents[2].get_text()
                    company_capital = companies[i].contents[3].get_text()
                    company_status = companies[i].contents[4].get_text()

                data.append([self.url_id, corporate_name, company_role, company_name, company_province, company_date, company_capital, company_status])
        
        else:
            data.append([self.url_id, '-', '-', '-', '-', '-', '-', '-'])

        return data


    def parse_finacing_info(self):   
        data = [['url_id', 'company_name', 'finacing_time', 'turn', 'appraisement', 'capital', 'propertion', 'invenstors']]
        header = self.soup.find('div', attrs={'class': 'company_header_width'})
        company_name = header.h1.get_text()
        finacing_link = header.contents[2]

        if finacing_link.contents:
            finacing_link = finacing_link.a['href']

            print('Connect: GET %s' % finacing_link)
            resp = self.req_get(finacing_link)

            print('Parsing: Finacing Info')
            print()
            finacing_soup = BeautifulSoup(resp.content, "html5lib")
            finacing_info = finacing_soup.find('div', attrs={'id': '_container_rongzi'})
            if finacing_info:
                finacing_table = finacing_info.tbody.contents

                for tr in finacing_table:
                    finacing_time = tr.contents[1].get_text()
                    turn = tr.contents[2].get_text()
                    appraisement = tr.contents[3].get_text()
                    capital = tr.contents[4].get_text()
                    propertion = tr.contents[5].get_text()
                    invenstors = tr.contents[6].get_text()
                    data.append([self.url_id, company_name, finacing_time, turn, appraisement, capital, propertion, invenstors])

            else:
                data.append([self.url_id, company_name, '-', '-', '-', '-', '-', '-'])   
        else:
            data.append([self.url_id, company_name, '-', '-', '-', '-', '-', '-'])

        return data



    def set_proxy(self):
        url = "http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=3873239366fb4548a227fcbf310862ba&count=1&expiryDate=0&format=1&newLine=2"
        resp = self.session.get(url)
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
            self.proxies = proxies
            print("Connect: Set Proxy %s" % proxy_meta)
            print()
        else:
            raise Exception


    def get_current_ip(self):
        url = "https://httpbin.org/ip"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        }
        resp = requests.get(url, headers=headers, proxies=self.proxies, timeout=10)
        print("Connect: Current IP %s" % resp.text.strip())
        return resp


    




