#! -*- encoding:utf-8 -*-

import requests


# proxies = { "http": "http://121.205.254.142:39651", "https": "https://121.205.254.142:39651" }

# url = "http://www.ip138.com/"
# resp2 = requests.get(url, proxies=proxies)
# print(resp2.text)
# url = "https://ip.cn/"


# headers = {
#    'Host': 'ip.cn',
#     'Connection': 'keep-alive',
#     'Cache-Control': 'max-age=0',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cookie': '__cfduid=d096d04867cc8b20cd31368ba48a6f9631528429439; UM_distinctid=163dd7e6dfd406-0eb2de4aefe7fb-39614807-1fa400-163dd7e6dfe267; CNZZDATA123770=cnzz_eid%3D1594430154-1528428224-%26ntime%3D1529654482',
# }






# url = "https://ip.cn/"
# url = "https://httpbin.org/ip"

import json
url = "http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=fede78e789e747ecaabbf1a442089de3&count=1&expiryDate=0&format=1&newLine=2"
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
else:
    raise Exception

print(proxies)

# proxy_meta = "%(ip)s:%(port)s" % {
#   "ip" : proxy_ip,
#   "port" : proxy_port,
# }
# proxies = {
#     "http"  : "http://" + proxy_meta,
#     "https" : "https://" + proxy_meta,
# }
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}

# resp = requests.get(url, proxies=proxies)
# print(resp.text)



# url = "https://ip.cn/"

# headers = {
#     ':authority': 'ip.cn',
#     ':method': 'GET',
#     ':path': '/',
#     ':scheme': 'https',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'max-age=0',
#     'upgrade-insecure-requests': '1',
#     'cookie': '__cfduid=d096d04867cc8b20cd31368ba48a6f9631528429439; UM_distinctid=163dd7e6dfd406-0eb2de4aefe7fb-39614807-1fa400-163dd7e6dfe267; CNZZDATA123770=cnzz_eid%3D1594430154-1528428224-%26ntime%3D1529649082',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
# }


# resp = requests.get(url, headers=headers, proxies=proxies)


# print(resp.text)