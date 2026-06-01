# cook your dish here
n=int(input())
for i in range(n):
    a=int(input())
    s=list(str(a))
    count=0
    for j in range(len(s)):
        if(s[j]=='4'):
            count+=1
    print(count)