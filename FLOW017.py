# cook your dish here
n=int(input())
for i in range(n):
    a=list(map(int, input().split()))
    x,y,z=sorted(a)
    print(y)