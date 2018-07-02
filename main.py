#! /usr/local/bin/python3
#coding: utf-8

import time
from task import Task
from config import db_conf, cookies


def main():
    try:
        t = Task(db_conf=db_conf)
        run(t)
    except:
        main()



def run(t):
    for i in range(0, 1000):
        p1 = t.get_proxies()
        t.run(p1, cookies[0])
        time.sleep(5)
        p2 = t.get_proxies()
        t.run(p2, cookies[1])
        time.sleep(5)
        p3 = t.get_proxies()
        t.run(p3, cookies[2])
        time.sleep(1)

        for j in range(1,10):
            t.run(p1, cookies[0])
            t.run(p2, cookies[1])
            t.run(p3, cookies[2])
            time.sleep(1)

        time.sleep(60)




if __name__ == '__main__':
    main()
    # t = Task(db_conf=db_conf)
    # run(t)
    # test()