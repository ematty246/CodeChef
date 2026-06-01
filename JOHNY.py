n=int(input())

for i in range(n):
    s=int(input())
    a=list(map(int,input().split()))
    k=int(input())

    johny = a[k-1]

    sor = sorted(a)

    print(sor.index(johny)+1)