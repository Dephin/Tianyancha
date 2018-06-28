# coding: utf-8


class Kls(object):
    def __init__(self, data):
        self.data = data

    x = 0
    def printd(self):
        print(self.data)
    @staticmethod
    def smethod(*arg):
        print('Static:', arg)
    @classmethod
    def xx(cls, x):
        cls.x = cls.x + 1
 
# ik = Kls(23)
# ik.printd()
# ik.smethod(10)
# ik.cmethod(11)
# Kls.smethod()
# Kls.cmethod()
Kls.xx(3)
print(Kls.x)