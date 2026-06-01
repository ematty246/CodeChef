# cook your dish here
T=int(input())
for i in range(T):
    x=int(input())
    s=str(x)
    l=len(s)
    print(int(s[0])+int(s[l-1]))