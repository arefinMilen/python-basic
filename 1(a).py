sum = 0
n = int(input("How many test case: "))
for i in range(n):
    x,y=input("Enter 2 integer: ").split()
    x=int(x); y = int(y)
    for j in range (x,(x+(y*2))):
        if j%2!=0:
            sum+=j
    print(sum)        