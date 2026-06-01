from functools import reduce
T=int(input())
for i in range(T):
    x=input()
    y=list(x)
    a=map(int,y)
    total=reduce(lambda x,y:x+y,a)
    print(total)
    
    