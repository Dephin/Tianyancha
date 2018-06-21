#! /usr/local/bin/python3
#coding: utf-8

import requests
import urllib
import json
import hashlib
import random

from bs4 import BeautifulSoup


class Scrawler(object):
    """docstring for  Scrawler"""
    def __init__(self, user='', passwd='', cookie='', proxies=[]):
        self.session = requests.session()
        self.session.headers = {
            'Host': 'www.tianyancha.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'https://www.tianyancha.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': cookie
        }
        self.soup = None
        self.url_id = None
        self.proxies = proxies


    def get_proxy(self):
        proxy = random.choice(self.proxies)
        self.session.proxies = { 'https': proxy }
        print("Choose Proxy: https %s" % proxy)


    def parse_urls(self, page_no):
        if page_no == 1:
            url = "https://www.tianyancha.com/search?key=%E7%A7%91%E6%8A%80%E9%87%91%E8%9E%8D"
        else:
            url = "https://www.tianyancha.com/search/p" + str(page_no) + "?key=%E7%A7%91%E6%8A%80%E9%87%91%E8%9E%8D"

        self.get_proxy()
        resp = self.session.get(url)

        urls_soup = BeautifulSoup(resp.content)
        urls = []
        url_list = urls_soup.find_all('div', attrs={'class': 'search_result_single'})

        for li in url_list:
            url = li.find('a')['href']
            urls.append(url)

        return urls


    def parse_url_content(self, url, url_id):
        print('Parse Url Content: %s' % url)
        self.get_proxy()
        resp = self.session.get(url)
        self.soup = BeautifulSoup(resp.content)
        self.url_id = url_id


    def parse_company_info(self):
        print('Parse Company Info')
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
        print('Parse Corporate Info')
        data = [['url_id', 'corporate_name', 'company_role', 'company_name', 'company_province', 'company_date', 'company_capital', 'company_status']]
        corporate_info = self.soup.find('div', attrs={'class': 'human-top'})

        if corporate_info and ('human' in corporate_info.a['href']):

            corporate_info = corporate_info.a
            corporate_name = corporate_info.get_text()
            corporate_link = corporate_info['href']
        
            resp = self.session.get(corporate_link)
            
            corporate_soup = BeautifulSoup(resp.content)
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
        print('Parse Finacing Info')
        data = [['url_id', 'company_name', 'finacing_time', 'turn', 'appraisement', 'capital', 'propertion', 'invenstors']]
        header = self.soup.find('div', attrs={'class': 'company_header_width'})
        company_name = header.h1.get_text()
        finacing_link = header.contents[2]

        if finacing_link.contents:
            finacing_link = finacing_link.a['href']
            resp = self.session.get(finacing_link)
            finacing_soup = BeautifulSoup(resp.content)
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
