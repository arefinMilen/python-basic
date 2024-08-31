list=[]
positive=[]
negative=[]

a=int(input("enter how many numbers you want to check :"))

for i in range(a):
    z=int(input("enter numbers and press enter :"))
    list.append(z)


for num in list:
 if num >= 0:
  positive.append(num)
 else:
  negative.append(num)

print(list)

print(f"your positive elements are {positive}\nand your negative number are {negative}")