a="Bangladesh Is My Mother Land"
b=""
# b=a.split() this is use for every word count as a list 
# print(b)
for i in a:
    if i.islower():
        b+=i
for i in a:
    if i.isupper():
        b+=i
print(b)

