# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n=int(input())
k=list(map(int,input().split(' ')))
f=list(map(int,input().split(' ')))
z=dict(zip(k,f))
z=sorted(z.items())
l=[]

sum=0
for i in range(len(z)):
    sum=sum+z[i][1]
    l.append(sum)
if(sum%2!=0):
    sum=sum+1
q1=sum//4
q3=sum*3//4

for i in range(len(l)):
    if(l[i]-q1<0):
        continue
    if(l[i]-q1==0):
        q11=((z[i][0]+z[i+1][0])/2)
        break
    else:
        q11=z[i][0]
        break

for i in range(len(l)):
    if(l[i]-q3<0):
        continue
    if(l[i]-q3==0):
        q21=((z[i][0]+z[i+1][0])/2)
        break
    else:
        q21=z[i][0]
        break
        
print(float(q21-q11))
