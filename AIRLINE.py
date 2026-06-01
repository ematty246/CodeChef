# cook your dish here
n=int(input())
for i in range(n):
    a,b,c,d,e=map(int,input().split())
    c1=a+b<=d and c<=e
    c2=b+c<=d and a<=e
    c3=a+c<=d and b<=e
    if c1 or c2 or c3:
        print("YES")
    else:
        print("NO")
        # TODO: write code...
        # TODO: write code...