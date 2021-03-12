import sys
a=int(sys.argv[1])
i=0
while a>0:
    i+=1
    a=a//10
print(i)