#! /usr/local/bin/python3
#coding: utf-8

import time


def excep():
    raise Exception


def t():
    n = 0 
    while True:
        try:
            excep()
            break
        except:
            n += 1
            print(n)
            time.sleep(1)
            if n >= 3:
                raise Exception
            continue

def t2():
    n = 0
    try:
        print('ok')
        t()
    except:
        n += 1
        if n ==2 :
            raise Exception
        t2()


t2()


