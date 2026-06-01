# cook your dish here
a,b,c=map(int,input().split())
if(c<50):
    print(a)
elif(c>=50):
    d=(c-50)*b
    print(a+d)