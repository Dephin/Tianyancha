#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : parse.py
# @Author  : dephin
# @File    : 2018/7/6

from bs4 import BeautifulSoup


class Parser(object):
	def __init__(self):
		self.url_id = None
		self.company_link = None
		self.company_name = None
		self.corporate_link = None
		self.corporate_name = None
		self.finacing_link = None

	def init(self, url_id, url):
		self.url_id = url_id
		self.company_link = url
		self.company_name = None
		self.corporate_link = None
		self.corporate_name = None
		self.finacing_link = None

	def parse_company_info(self, resp):
		print('Parsing: Company Info\n')
		soup = BeautifulSoup(resp.text, "html5lib")

		data = [['url_id', 'company_name', 'company_address', 'company_intro', 'company_status']]
		url_id = self.url_id
		header = soup.find('div', attrs={'class': 'company_header_width'})
		company_name = header.h1.get_text()
		company_info = header.find_all('div', attrs={'class': ['f14', 'sec-c2']})
		company_address = company_info[1].contents[1].contents[1].get_text()
		company_intro = header.find('script', attrs={'id': 'company_base_info_detail'})
		if company_intro:
			company_intro = company_intro.get_text().strip()
		else:
			company_intro = '暂无信息'

		company_info2 = soup.find_all('div', attrs={'class': 'baseinfo-module-content-value'})
		if company_info2:
			company_status = company_info2[2].get_text()
		else:
			company_status = '暂无信息'

		data.append([url_id, company_name, company_address, company_intro, company_status])

		corporate_info = soup.find('div', attrs={'class': 'human-top'})
		if corporate_info and ('human' in corporate_info.a['href']):
			# self.corporate_info = corporate_info.a
			self.corporate_name = corporate_info.get_text()
			self.corporate_link = corporate_info['href']

		self.finacing_link = header.contents[2]

		return data

	def parse_corporate_info(self, resp):
		data = [['url_id', 'corporate_name', 'company_role', 'company_name', 'company_province', 'company_date',
				 'company_capital', 'company_status']]

		url_id = self.url_id

		if self.corporate_link:
			corporate_name = self.corporate_name

			print('Parsing: Corporate Info\n')
			corporate_soup = BeautifulSoup(resp.content, "html5lib")
			companies = corporate_soup.find('div', attrs={'id': '_container_syjs'}).table.tbody.find_all('tr')

			for i in range(0, len(companies)):
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

				data.append([url_id, corporate_name, company_role, company_name, company_province, company_date,
							 company_capital, company_status])

		else:
			data.append([url_id, '-', '-', '-', '-', '-', '-', '-'])

		return data

	def parse_finacing_info(self, resp):
		data = [['url_id', 'company_name', 'finacing_time', 'turn', 'appraisement', 'capital', 'propertion', 'invenstors']]
		url_id = self.url_id
		company_name = self.company_name

		if self.finacing_link:
			print('Parsing: Finacing Info\n')
			finacing_soup = BeautifulSoup(resp.text, "html5lib")
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
					data.append(
						[url_id, company_name, finacing_time, turn, appraisement, capital, propertion, invenstors])
			else:
				data.append([url_id, company_name, '-', '-', '-', '-', '-', '-'])
		else:
			data.append([url_id, company_name, '-', '-', '-', '-', '-', '-'])

		return data
