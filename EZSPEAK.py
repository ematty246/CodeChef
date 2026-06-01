# cook your dish here
n=int(input())
a=['a','A','e','E','i','I','o','O','u','U']
for i in range(n):
    count=0
    max_count=0
    l=int(input())
    s=input()
    for j in range(len(s)):
        if s[j] not in a:
            count+=1
            max_count=max(count,max_count)
        else:
            count=0
    if(max_count>4):
        print("NO")
    else:
        print("YES")
            
            