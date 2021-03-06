import sys
from MyModule import getsquare
#當前只保留陣列平方 目前程式有:費波那契數列、陣列平方、組合數C、求數值位數、求證是否為回文
x=list(map(int,sys.argv[1].split()))
print(getsquare(x))