# cook your dish here
n=int(input())
for i in range(n):
    s=input()
    l=len(s)
    if(l%2==0):
        a=l//2
        h1=s[:a]
        h2=s[a:]
        if sorted(list(h1))==sorted(list(h2)):
            print("YES")
        else:
            print("NO")
    elif(l%2!=0):
        a=l//2
        h1=s[:a]
        h2=s[a+1:]
        if sorted(list(h1))==sorted(list(h2)):
            print("YES")
        else:
            print("NO")
            