# cook your dish here
n=int(input())
for i in range(n):
    a=int(input())
    s=input()
    l=list(s)
    count_a=0
    count_b=0
    for i in range(len(l)):
    
        if(l[i]=='a'):
            count_a+=1
        elif(l[i]=='b'):
            count_b+=1
    print(count_a,count_b)