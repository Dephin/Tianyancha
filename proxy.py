#! /usr/local/bin/python3
#coding: utf-8


import random

a = ['1', '2']
print( random.choice(a) )
exit()





import requests


# 代理服务器
# 代理服务器
proxyHost = "101.236.36.119"
proxyPort = "8866"

# 代理隧道验证信息
proxyUser = "HH30H1A522679P8D"
proxyPass = "74EF13F061719736"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

print(proxyMeta)

exit()

session = requests.session()
resp = session.get("http://httpbin.org/ip", proxies=proxies).text


login_res=self.s.post(url=login_url,headers=headers,data=form_data,proxies=self.proxies).text  #这是报错部分 






session = requests.session()
proxies = { "http": "http://183.167.217.152:63000", "https": "http://101.236.36.119:8866", }   
print(session.proxies)
resp = session.get("http://httpbin.org/ip", proxies=proxies) 

print(resp.content)