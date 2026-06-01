# cook your dish here

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    
    mn = min(l)
    
    if l.count(mn) >= 2:
        print("YES")
    else:
        print("NO")