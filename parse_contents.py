#! /usr/local/bin/python3
#coding: utf-8

import json
import time
from scrawl_contents import ScrawlContents


class ParseContents(ScrawlContents):
    """docstring for ParseContents"""
    def __init__(self):
        super(ParseContents, self).__init__()


    def parse(self):
        error_num = 0

        while True:
            try:
                company_data = self.parse_company_info()
                # time.sleep(1)
                error_num = 0
                break
            except Exception as e:
                print(e)
                error_num += 1
                print("Connect: Refused By Server")
                print("Let me sleep for 5 seconds.")
                time.sleep(5)
                print("ZZzzz...")
                print("Was a nice sleep, now let continue.")
                if error_num >= 3:
                    raise Exception
                else:
                    continue

        while True:
            try:
                corporate_data = self.parse_corporate_info()
                # time.sleep(1)
                error_num = 0
                break
            except Exception as e:
                print(e)
                error_num += 1
                print("Connect: Refused By Server")
                print("Let me sleep for 5 seconds.")
                time.sleep(5)
                print("ZZzzz...")
                print("Was a nice sleep, now let continue.")
                if error_num >= 3:
                    raise Exception
                else:
                    continue

        while True:
            try:
                finacing_data = self.parse_finacing_info()
                # time.sleep(1)
                error_num = 0
                break
            except Exception as e:
                print(e)
                error_num += 1
                print("Connect: Refused By Server")
                print("Let me sleep for 5 seconds.")
                time.sleep(5)
                print("ZZzzz...")
                print("Was a nice sleep, now let continue.")
                if error_num >= 3:
                    raise Exception
                else:
                    continue

        return company_data, corporate_data, finacing_data
