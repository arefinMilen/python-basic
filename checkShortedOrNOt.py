a=[1,2,3,7,5]
# b=[]
for i in range(len(a)-1):
    if a[i] <= a[i+1]:
        continue
    else:
        print("your element is not shorted ")
        break
else:
    print("your element is shorted!")
# print(f"the shorted elements are {b}")


