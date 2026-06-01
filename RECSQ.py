# cook your dish here
n=list(map(int,input().split()))
i=0
if(n[i]*n[i+1]==pow(n[i+2],2)):
    print("Yes")
else:
    print("No")