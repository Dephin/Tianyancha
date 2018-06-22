#! -*- encoding:utf-8 -*-

import requests

# 要访问的目标页面
# targetUrl = "http://test.abuyun.com"
#targetUrl = "http://proxy.abuyun.com/switch-ip"
# targetUrl = "http://proxy.abuyun.com/current-ip"
targetUrl = "https://www.ipip.net/ip.html"

# # 代理服务器
# proxyHost = "http-pro.abuyun.com"
# proxyPort = "9010"

# # 代理隧道验证信息
# proxyUser = "H6ZYD81Q8C00C74P"
# proxyPass = "AB29C3D713C0006F"

# proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
#   "host" : proxyHost,
#   "port" : proxyPort,
#   "user" : proxyUser,
#   "pass" : proxyPass,
# }


proxy_host = "117.95.83.165"
proxy_port = "40551"

proxy_meta = "%(ip)s:%(port)s" % {
	"ip": proxy_host,
	"port": proxy_port,
}


proxies = {
    "http"  : "http://" + proxy_meta,
    "https" : "https://" + proxy_meta,
}

# proxies = {
#     "http"  : proxyMeta,
#     "https" : proxyMeta,
# }
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
print(proxies)
session = requests.session()
resp = session.get(targetUrl, headers=headers, proxies=proxies)

print(resp.status_code)
print(resp.text)