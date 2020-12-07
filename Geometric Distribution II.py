l, r = list(map(float, input().split(" ")))
n=int(input())
p=l/r
q=1-p
print(round(sum([q**(n - x) * p for x in range(1, 6)]), 3))
