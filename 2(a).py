list =["shikha","Hauna","Muzam",'01971700130']
total_character=''.join(list)

print(f"Number of Character : {len(total_character)}")

def count_vowel(string):
    vowel="aeiouAEIOU"
    count=0
    for char in string:
        if char in vowel:
         count+=1

    return count
num_vowels=count_vowel(total_character)
print(f"Number of vowels: {num_vowels}")





# # Define the list of strings
# names_list = ["Shikha", "Haua", "Muzam", "01971700130"]
#
# # Join all strings in the list into a single string
# all_names = ''.join(names_list)
#
# # Count the total number of characters
# num_characters = len(all_names)
#
# # Define a function to count vowels
# def count_vowels(string):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count
#
# # Count the number of vowels in the combined string
# num_vowels = count_vowels(all_names)
#
# # Print the results
# print("Number of Characters:", num_characters,"\n" "Number of Vowels:", num_vowels)
