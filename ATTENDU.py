# cook your dish here
n=int(input())
total_w=120
p=75
for i in range(n):
    count_0=0
    count_1=0
    n=int(input())
    s=input()
    for i in s:
        if '0'==i:
            count_0+=1
        else:
            count_1+=1
    attend = count_1 + (total_w - n)
    p_attend=attend/total_w
    p_attend_total=p_attend*100
    if(p_attend_total>=p):
        print("YES")
    else:
        print("NO")
    