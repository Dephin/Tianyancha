#! /usr/local/bin/python3
#coding: utf-8

from config import proxy_url


class ParseContents(ScrawlContents):
    """docstring for ParseContents"""
    def __init__(self):
        super(ScrawlContents, self).__init__()

    def get_proxies(self, url):
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
            return proxies
            print("Connect: Set Proxy %s" % proxy_meta)
            print()
        else:
            raise Exception


    def reset_proxies(self):
        proxies = self.get_proxies()
        self.set_proxy()

    def parse(self):
        while True:
            try:
                scrawler.parse_url_content(url, url_id)
                company_data = self.parse_company_info()
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
                if error_num >= 5:
                    raise Exception
                else:
                    error_num = 0
                    continue

        while True:
            try:
                corporate_data = self.parse_corporate_info()
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
                if error_num >= 5:
                    raise Exception
                else:
                    error_num = 0
                    continue

        while True:
            try:
                finacing_data = self.parse_finacing_info()
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
                if error_num >= 5:
                    raise Exception
                else:
                    error_num = 0
                    continue
    

    def run(self):
        self.set_cookie()
        proxies = self.get_proxies(proxy_url)
        self.set_proxy()
