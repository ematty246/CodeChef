# cook your dish here
n=int(input())
for i in range(n):
    ch=input()
    if(ch=='B' or ch=='b'):
        print("BattleShip")
    elif(ch=='c' or ch=='C'):
        print("Cruiser")
    elif(ch=='d' or ch=='D'):
        print("Destroyer")
    elif(ch=='f' or ch=='F'):
        print("Frigate")