# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(float, input().split())
    c=a*b
    if(a>1000):
        print(c*0.90)
    else:
        print(c)