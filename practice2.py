# d=181,178,187,182,192,189,202
# b=[]
# b.append(d)
# print(b)

# class ChatGPT:
#     def __init__(self):
#         self.user_name = ""
#
#     def greet(self):
#         print("Hi!")
#
#     def ask_user(self):
#         self.user_name = input("What's your name? ")
#         print(f"Nice to meet you, {self.user_name}!")
#
#     def chat(self):
#         self.greet()
#         self.ask_user()
#         print("What can I do for you today?")
#
#
# # Create an instance of ChatGPT
# demo_chatgpt = ChatGPT()
# # Start the conversation
# demo_chatgpt.chat()

# Given string
# given_string = "This is the 5th example sentence."
#
# # Replace "5th" with "7th"
# modified_string = given_string.replace("5th", "7th")
#
# print(modified_string)

# def create_user_dict():
#     user_dict = {}
#     while True:
#         user_id = input("Enter user ID (press Enter to stop): ")
#         if not user_id:
#             break
#         name = input("Enter user's name: ")
#         plan = input("Enter user's preferred plan (Basic/Standard/Premium): ")
#         user_dict[user_id] = {"name": name, "plan": plan}
#     return user_dict
#
# def calculate_payment(user_dict):
#     for user_id, user_info in user_dict.items():
#         plan = user_info["plan"]
#         if plan == "Basic":
#             payment = 9.99
#         elif plan == "Standard":
#             payment = 15.99
#         elif plan == "Premium":
#             payment = 19.99
#         else:
#             payment = None
#         if payment is not None:
#             print(f"{user_info['name']}'s payment amount for the {plan} plan is ${payment} per month")
#
# # Create nested dictionary of users and their plans
# user_dict = create_user_dict()
#
# # Calculate and print payment amounts
# calculate_payment(user_dict)

# value=[1,2,3,4,5,6,7,8,9]
# value2=[1,2,3]
# for item in value:
#     if item == 5:
#         continue
#     print("break")
#     for item2 in value2:
#        print(item,item2)
# def calculate_waiver(cgpa, semester_fee):
#     if cgpa > 3.50:
#         waiver_percent = 20
#     elif 3.00 <= cgpa <= 3.50:
#         waiver_percent = 10
#     else:
#         waiver_percent = 5
#
#     waiver_amount = (waiver_percent / 100) * semester_fee
#     return waiver_amount
#
#
# # Take user input for semester fee and CGPA
# semester_fee = float(input("Enter semester fee: "))
# cgpa = float(input("Enter CGPA: "))
#
# # Calculate and print net waiver amount
# net_waiver = calculate_waiver(cgpa, semester_fee)
# print(f"Net waiver amount: ${net_waiver}")


# Initialize an empty list to store odd numbers
# odd_numbers = []
#
# # Start with the first odd number, which is 1
# number = 1
#
# # Iterate using a while loop until number reaches 100
# while number <= 100:
#     # Check if the number is odd
#     if number % 2 != 0:
#         # If the number is odd, append it to the list
#         odd_numbers.append(number)
#     # Increment number by 1 for the next iteration
#     number += 1
#
# # Display the list of odd numbers
# print("List of odd numbers from 1 to 100:")
# print(odd_numbers)


# def find_common_element(list1,list2):
#     set1=set(list1)
#     set2=set(list2)
#     common_elements = list(set1.intersection(set2))
#     return common_elements
# list1=[1,6,3]
# list2=[2,4,5]
# common_elements = find_common_element(list1,list2)
# if common_elements:
#
#  print(common_elements)
# else:
#     print("no common elements")




a=int(input("enter number:"))
list=[]
for i in range (a):
  z=int(input("dial number and press enter:"))
  list.append(z)

if len(list)<3:
    print("not possible")
else:
    new_list = list[1:-1]
    print(new_list)