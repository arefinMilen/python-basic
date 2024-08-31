n = int(input("enter a number : "))
sum = 0
for i in range(1,n):
    if n%i == 0 :
        sum = sum +i
        print(i)


if sum == n:
    print("yes this is strong number ")
else:
    print("Is not strong number ")

# 8 . find prime and composite number
#
# n = int(input("enter a number : "))
# count =0
# for i in range(1,n+1):
#     if n%i == 0:
#         count = count +1
# if count == 2:
#  print("prime number ")
#
# else:
#  print("composite number ")


#9. separate each digit of a num and print new line

# a = int (input ("Please tell your number :"))
# while a>0:
#     print(a%10)
#     a=a//10

# #10 . check palindrome or not   ex -- 12321 reverse --12321
#
# n = int(input("enter your number :"))
#
# copy = n
# rev =0
# while n> 0:
#     z = n % 10
#     rev = rev * 10 + z
#     n = n // 10
# if copy == rev :
#     print("polindrome number ")
# else:
#     print("Not a palindrome number ")


# a= int(input("enter number :"))
# while a>0:
#  print(a%10)
#  a=a//10
# print(a%10)
# a=a//10
# print(a%10)