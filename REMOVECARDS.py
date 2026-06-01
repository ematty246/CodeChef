# cook your dish here
n=int(input())
for i in range(n):
    a=int(input())
    s=list(map(int,input().split()))
    mx=0
    for x in s:
        c=s.count(x)
        if(c>mx):
            mx=c
    print(a-mx)
        
        