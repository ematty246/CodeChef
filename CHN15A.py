# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    s=list(map(int,input().split()))
    c=0
    for i in range(a):
        if((b+s[i])%7==0):
            c+=1
    print(c)
            

