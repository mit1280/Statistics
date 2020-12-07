l, r = list(map(float, input().split(" ")))
n=int(input())
p=l/r
q=1-p
print(round(pow(q,(n-1))*p,3))
