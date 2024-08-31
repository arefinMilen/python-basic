a=input("enter a word and check it is palindrome or not!:")
b=""
for i in range(len(a)-1,-1,-1):
     b+=a[i]

if a==b:
    print("Palindrome!")
else:
    print("not palindrome")
