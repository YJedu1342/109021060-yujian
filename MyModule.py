def getplus(a,b):
    return a+b
def getless(a,b):
    return a-b
def getmultiply(a,b):
    return a*b
def getdivision(a,b):
    return a/b
def getFibonacci(a):
    if a<=1:
        return 1
    else:
        return getFibonacci(a-1)+getFibonacci(a-2)
def getcombination(a,b):
    tmp1=1
    tmp2=1
    tmp3=1
    for i in range(1,a+1):
        tmp1*=i
    for i in range(1,b+1):
        tmp2*=i
    for i in range(1,a-b+1):
        tmp3*=i
    return tmp1/(tmp2*tmp3)
def getsquare(a):
    for i in range(len(a)):
        a[i]=a[i]*a[i]
    return a
def getnumberdigit(a):    
    i=0
    while a>0:
        i+=1
        a=a//10
    return i
def getpalindrome(a):
    flag=True
    tmp=len(a)//2
    for i in range(tmp):
        if a[i]==a[len(a)-1-i]:
            flag=True
        else:
            flag=False
    return flag