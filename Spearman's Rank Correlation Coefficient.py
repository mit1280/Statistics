n = int(input())
x = [float(i) for i in input().strip().split()]
y = [float(i) for i in input().strip().split()]
x1=sorted(x)
y1=sorted(y)
l=[]
for i in x:
    l.append(x1.index(i)+1)
l1=[]
for i in y:
    l1.append(y1.index(i)+1)
rxy =1-(sum([(l[i]-l1[i])**2 for i in range(n)])*6/(n*(n**2-1)))
print(round(rxy,3))
