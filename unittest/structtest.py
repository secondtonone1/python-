#-*-coding:utf-8-*-

import sys
import os

#传参类型
# eoss11111111  resonance 0.0500  eoss11111111 600 

class ST(object):
    def __init__(self,name,age):
        self.name=name
        self.age = age
    def changeMember(self,name):
        self.name = name

def changeST(st):
    print("st addr is %d" % (id(st)))
    st.changeMember("LiLei")



if __name__ == '__main__':
    zack = ST("Zack",31)
    bob = ST("Bob",22)
    print("zack addr %d" % id(zack))
    print("bob addr %d" % id(bob))
    zackcopy = zack
    print("zack2 addr %d" % id(zackcopy))
    changeST(zackcopy)
    print(zackcopy.name)
    print(zackcopy.age)

   # ./cleos.sh transfer eoss11111111  resonance "0.0500 EOS"  "eoss11111111" -p eoss11111111
   # if argn <
