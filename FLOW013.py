# cook your dish here
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    s=a+b+c
    if(s==180):
        print("YES")
    else:
        print("NO")