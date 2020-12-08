import math
l=float(input())
k = int(input())
mul=1
for i in range(1,k+1):
    mul=mul*i
print(round(pow(l,k)/(pow(math.e,l)*mul),3))
