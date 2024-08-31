vowel=0
const=0
data="this is my new journey about python learning"

for i in data:
    if i in "aeiouAEIOU":
        vowel+=1
    elif i in " ":
        continue
    else:
        const+=1
print(f"consonent are :{const}\nVowel are :{vowel}")


# solve it using function
# def count(x):
#     vowel = 0
#     const = 0
#     for i in x:
#         if i in "aeiouAEIOU":
#             vowel += 1
#         elif i in " ":
#             continue
#         else:
#             const += 1
#         return vowel,const
#
# a="my name is samsul arefin milen"
# print(count(a))


