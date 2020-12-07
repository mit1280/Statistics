def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, r):
    return fact(n) / (fact(r) * fact(n-r))

def b( n,r, p):
    return comb(n, r) * p**r * (1-p)**(n-r)

n1,n2= list(map(float, input().split(" ")))
p = n1 / n2
print(round(sum([b( 6,i, p / (1 + p)) for i in range(3, 7)]), 3))
