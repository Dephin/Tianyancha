#! -*- encoding:utf-8 -*-

import requests
from bs4 import BeautifulSoup


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









url = "https://m.intl.taobao.com/detail/detail.html?id=559123596040"

headers = {
    'Host': 'detail.tmall.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'cna=wGxrEh6svkcCAWXnW9LrOZQP; thw=cn; t=190e2f449c9a1c64b9c6f4ca88b846c6; tg=0; enc=onO6R0zF6MvLCHIvC3sq%2FDJHTf7K68VjuGRZEO24xy2rwhkkB4L%2FGdBIiwugohMcD2z8qZi%2BZCKJW35OsjJ1Lg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=jackwolfskin%5Cu4E59%5Cu592E%5Cu4E13%5Cu5356%5Cu5E97; _cc_=Vq8l%2BKCLiw%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; UM_distinctid=162f70e6e605e6-03b80a949a337b-3a614f0b-1fa400-162f70e6e6130b; miid=802374001772122251; v=0; cookie2=1150c80fd02a67766a94b73c1108b4db; _tb_token_=3013ef7339e79; isg=BNfX-JdRQAVuqMZQv8QG_v-xZkvhtM7OC6DhFikFbaYMWPeaMew7zpU5vvjGsIP2',
}

resp = requests.get(url)
print(resp.text)

with open('./test.html', 'wb') as f:
    f.write(resp.content)


# soup = BeautifulSoup(resp.text, "html5lib")
# s = soup.find_all('div', attrs={'class': 'tm-price'})
# print(s)