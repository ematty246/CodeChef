# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    max_area=0
    for j in range(a):
        c,d,e=map(int,input().split())
        if(e<=b):
            area=c*d
            if(area>max_area):
                max_area=area
    if(max_area==0):
        print("no tablet")
    else:
        print(max_area)
        
            
            
            
