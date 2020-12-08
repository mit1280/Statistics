import math
m,d=list(map(int,input().split(" ")))
a1=float(input())
a,b=list(map(int,input().split(" ")))
def fi(x):
    return(0.5 * (1 + math.erf((x - m) / (d * (2 ** 0.5)))))
print(round(fi(a1),3))
print(round(fi(b)-fi(a),3))
