# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    s=list(map(int,input().split()))[:a]
    if(sum(s)<=b):
        print("Yes")
    else:
        print("No")