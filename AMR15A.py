# cook your dish here
n=int(input())
w=map(int, input().split())
s=list(w)
even_count=0
odd_count=0
for i in range(len(s)):
    if(s[i]%2==0):
        even_count+=1
    elif(s[i]%2!=0):
        odd_count+=1
if(even_count>odd_count):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
