# cook your dish here
n=int(input())
for i in range(n):
    bs=int(input())
    if(bs<1500):
        hra=(0.10)*bs
        da=(0.90)*bs
    elif(bs>=1500):
        hra=500
        da=(0.98)*bs
    
    gross=bs+hra+da
    print(gross)
