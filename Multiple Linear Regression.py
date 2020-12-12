from sklearn import linear_model
m,n=list(map(int,input().split(" ")))
x=[]
y=[]
for i in range(n):
    *x1,y1=list(map(float,input().split(" ")))
    x.append(x1)
    y.append(y1)
x3=int(input())
z=[]
for i in range(x3):
    z.append(list(map(float,input().split(" "))))
lm = linear_model.LinearRegression()
lm.fit(x, y)
pred=lm.predict(z)
for i in pred:
    print(round(i,2))
