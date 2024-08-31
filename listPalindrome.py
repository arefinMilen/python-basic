x=[1,2,2,3,2,2,1]
b=[]
for i in range(len(x)-1,-1,-1):
    b.append(x[i])
if b == x:
    print("palindrome")
else :
    print("not palindrome")


# using set for remove repeating in the list
# n=[1,1,1,1,2,2,4,4,5,5,3,3,3,7,7,6,6,5,5]
# b=[]
# b=set(n)
# print(b)