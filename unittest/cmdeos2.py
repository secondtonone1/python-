#-*-coding:utf-8-*-

import sys
import os

#传参类型
# eoss11111111  resonance 0.0500  eoss11111111 600 

if __name__ == '__main__':
    argn = len(sys.argv)
    print("参数个数为: %d \n" %argn)
    print("参数分别为: %s \n" %str(sys.argv))
    if(argn != 6):
        print("参数数目不正确")
    else :
        str1 = "./cleos.sh transfer " + sys.argv[1] + " "+ sys.argv[2] +" " + '"'+sys.argv[3] +" EOS"+ '"' " "+ '"'+sys.argv[4]+'"' + \
            ' -p '+ sys.argv[1]
        print("your cmd is %s" %str1)
        os.system(str1)


   # ./cleos.sh transfer eoss11111111  resonance "0.0500 EOS"  "eoss11111111" -p eoss11111111
   # if argn <
