n=int(input())

for i in range(n):
    s=input()
    b=[]
    for j in s:
        if j.isdigit():
            a=b.append(int(j))
    print(sum(b))
    