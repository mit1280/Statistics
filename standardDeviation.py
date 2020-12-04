n=int(input())
k=list(map(int,input().split(' ')))
sum=0
for i in range(n):
    sum=sum+k[i]
mean=sum/n
sum=0
for i in range(n):
    sum=sum+((k[i]-mean)**2)
print(round(pow(sum/n,1/2), 1))
