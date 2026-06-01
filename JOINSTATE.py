# cook your dish here
t = int(input())

for _ in range(t):
    st, req = map(int, input().split())
    s = list(map(int, input().split()))

    count = 0
    total = 0

    for j in s:
        total += j

        if total >= req:
            count += 1
            total = 0

    print(count)