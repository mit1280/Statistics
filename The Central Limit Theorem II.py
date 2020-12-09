import math

x = int(input())
n = int(input())
m = float(input())
sigma = float(input())

m = n * m 
sigma = math.sqrt(n) * sigma

print(round(0.5*(1 + math.erf((x - m)/(sigma*(math.sqrt(2))))), 4))
