# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n=int(input())
k=list(map(int,input().split(' ')))
k.sort()
n1=n//2
if(n%2!=0):
    x1=k[:n1]
    x2=k[n1+1:]
else:
    x1=k[:n1]
    x2=k[n1:]

n2=len(x1)//2
n3=len(x2)//2
if(n%2==0 and n2%2==0):
    print(x1[n2])
else:
    print((x1[n2]+x1[n2-1])//2)

if(n%2!=0):
    print(k[n1])
else:
    print((k[n1]+k[n1-1])//2)

if(n%2==0 and n3%2==0):
    print(x2[n3])
else:
    print((x2[n3]+x2[n3-1])//2)
