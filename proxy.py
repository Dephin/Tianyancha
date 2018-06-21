#! /usr/local/bin/python3
#coding: utf-8

import requests



# import socket

# sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sk.settimeout(5)

# try:
#     host = '125.120.206.225'
#     port = 6666
#     sk.connect((host, port))
#     print("Server port is ok")
# except Exception as e:
#     print(e)
#     print("%s Server port %s is close" % (host, port))
# finally:
#     sk.close()



# import telnetlib

# try:
#     telnetlib.Telnet('125.120.206.225', port=6666, timeout=20)
# except Exception as e:
#     print('connect failed')
#     print(e)
# else:
#     print('success')



# session = requests.session()
# proxies = { "https": "http//125.120.206.225:6666" }   
# resp = session.get("https://www.ipip.net/ip.html", proxies=proxies, verify=False) 
# print(resp)
# requests.get('http://wenshu.court.gov.cn/', proxies=proxies)

# with open("./ip.html", "wb") as f:
#     f.write(resp.content)

# exit()


# import random



# 代理服务器
# 代理服务器
# proxyHost = "101.236.36.119"
# proxyPort = "8866"

# # 代理隧道验证信息
# proxyUser = "HH30H1A522679P8D"
# proxyPass = "74EF13F061719736"

# proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
#     "host": proxyHost,
#     "port": proxyPort,
#     "user": proxyUser,
#     "pass": proxyPass,
# }

# proxies = {
#     "http": proxyMeta,
#     "https": proxyMeta,
# }

# session = requests.session()
# resp = session.get("http://httpbin.org/ip", proxies=proxies).text


# login_res = self.s.post(url=login_url,headers=headers,data=form_data,proxies=self.proxies).text  #这是报错部分 






# session = requests.session()
# proxies = { "http": "http://125.120.206.225:6666" }   
# resp = session.get("http://httpbin.org/ip", proxies=proxies) 

# print(resp.content)