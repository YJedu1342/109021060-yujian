def plus(a,b):
    return a+b
def less(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def fs(a):
    if a<=1:
        return 1
    else:
        return fs(a-1)+fs(a-2)