import math
n=int(input())
k=list(map(int,input().split(' ')))
sum=0
for i in k:
    sum=sum+i
print(sum/n)
k.sort()
n1=n//2
print((k[n1]+k[n1-1])/2)
d={}
for i in k:
    d[i]=k.count(i)
p=max(d,key=d.get)
print(p)
