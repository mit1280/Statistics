import math

x = int(input())
n = int(input())
m = int(input())
sigma = int(input())

m = n * m 
sigma = math.sqrt(n) * sigma

print(round(0.5*(1 + math.erf((x - m)/(sigma*(math.sqrt(2))))), 4))
