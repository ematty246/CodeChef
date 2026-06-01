# cook your dish here
n=int(input())
for i in range(n):
    a=int(input())
    s=input()
    if 'I' in s:
        print("INDIAN")
    elif 'Y' in s:
        print("NOT INDIAN")
    else:
        print("NOT SURE")
