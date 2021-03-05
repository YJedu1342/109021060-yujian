import sys
def fun(a):
    if a<=1:
        return 1
    else:
        return fun(a-1)+fun(a-2)
a=int(sys.argv[1])
print(a)