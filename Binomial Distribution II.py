def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

l, r = list(map(float, input().split(" ")))
x1=(round(sum([b(i, r, l/100) for i in range(3)]), 3))
x2=(round(b(2, r, l/100) , 3))
print(x1)
print(round(1-x1+x2,3))
