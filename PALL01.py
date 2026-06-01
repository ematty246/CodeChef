# cook your dish here
n=int(input())
for i in range(n):
    a=int(input())
    s=str(a)
    rev=int(s[::-1])
    if(a==rev):
        print("wins")
    else:
        print("loses")