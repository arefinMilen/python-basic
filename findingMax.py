a=[32,54,12,56,867,545,34,234,8657,534543,233432,23,54,134]
max=0
max2=0
index=0
index2=0

for i in range(len(a)):
    if a[i]>max:
        max2=max
        max =a[i]
        index2=index
        index = i
    elif a[i] > max2:
         max2 = a[i]
         index2 =i


print(f"your largest number is {max} at index {index}")
print(f"your 2nd largest number is {max2} at 2nd index {index2}")



