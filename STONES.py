# cook your dish here
n=int(input())
for i in range(n):
    J=input()
    S=input()
    count=0
    for ch in S:
        if ch in J:
                count+=1
    print(count)