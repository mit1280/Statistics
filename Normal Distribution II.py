import math
m,d=list(map(int,input().split(" ")))
a=int(input())
b=int(input())
def fi(x):
    return(0.5 * (1 + math.erf((x - m) / (d * (2 ** 0.5)))))

print(round((1-fi(a))*100,2))
print(round((1-fi(b))*100,2))
print(round(fi(b)*100,2))
