#! -*- encoding:utf-8 -*-

import requests

# 要访问的目标页面
# targetUrl = "http://test.abuyun.com"
#targetUrl = "http://proxy.abuyun.com/switch-ip"
targetUrl = "http://proxy.abuyun.com/current-ip"
# targetUrl = "https://www.ipip.net/ip.html"

# 代理服务器
proxyHost = "http-pro.abuyun.com"
proxyPort = "9010"

# 代理隧道验证信息
proxyUser = "H6ZYD81Q8C00C74P"
proxyPass = "AB29C3D713C0006F"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
  "host" : proxyHost,
  "port" : proxyPort,
  "user" : proxyUser,
  "pass" : proxyPass,
}

proxies = {
    "http"  : proxyMeta,
    "https" : proxyMeta,
}

session = requests.session()
resp = session.get(targetUrl, proxies=proxies)

print(resp.status_code)
print(resp.text)