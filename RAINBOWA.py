# cook your dish here
n = int(input())

for i in range(n):
    a = int(input())

    l = list(map(int, input().split()))[:a]

    if l != l[::-1]:
        print("no")
        continue

    if set(l) != {1, 2, 3, 4, 5, 6, 7}:
        print("no")
        continue

    ok = True

    for j in range(1, a):
        if abs(l[j] - l[j-1]) > 1:
            ok = False
            break

    if ok:
        print("yes")
    else:
        print("no")