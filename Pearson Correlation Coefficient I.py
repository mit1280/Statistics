import statistics as s
n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))
xm=s.mean(x)
ym=s.mean(y)

sum=0
sum1=0
sum2=0
for i in range(len(x)):
    sum=sum+(x[i]-xm)*(y[i]-ym)
    sum1=sum1+(x[i]-xm)**2
    sum2=sum2+(y[i]-ym)**2
covx=pow(sum1/n,1/2)
covy=pow(sum2/n,1/2)
print(round(sum/(n*covy*covx),3))
