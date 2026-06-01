# cook your dish here
n=int(input())
for i in range(n):
    a=int(input())
    s=list(map(int,input().split()))
    m=min(s)
    moves=0
    for i in s:
        moves=moves+(i-m)
    print(moves)