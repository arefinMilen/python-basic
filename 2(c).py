# user_name=["healthMin","reliefMin","FoodMin"]
# password = ['123health','456relief','789food']
# admin = {'imadmin': '123'}
#
# user_pairs=dict(zip(user_name,password))
# # print(user_pairs)
# def authinticate_user(username,pwd):
#     if username in user_pairs and user_pairs[username] ==pwd:
#         return True
#     else:
#         return False
# def authenticate_admin(username,pwd):
#     if username in admin and admin[username] == pwd:
#         return  True
#     else:
#         return False
# def user_login():
#   username = input("Enter your user name ")
#   password = input("Enter your password ")
#   if authinticate_user(username,pwd):
#      print("")


# Predefined information
user_name = ["healthMin", "reliefMin", "FoodMin"]
password = ['123health', '456 relief', '789food']
admin = {'imadmin': '123'}

# Convert items of user_name and password list into pairs
user_credentials = dict(zip(user_name, password))

# Function to authenticate users
def authenticate_user(username, pwd):
    if username in user_credentials and user_credentials[username] == pwd:
        return True
    else:
        return False

# Function to authenticate admin
def authenticate_admin(username, pwd):
    if username in admin and admin[username] == pwd:
        return True
    else:
        return False

# User login
def user_login():
    username = input("Enter your username: ")
    pwd = input("Enter your password: ")
    if authenticate_user(username, pwd):
        print("User login successful!")
    else:
        print("Invalid username or password. User login denied.")

# Admin login
def admin_login():
    username = input("Enter admin username: ")
    pwd = input("Enter admin password: ")
    if authenticate_admin(username, pwd):
        print("Admin login successful!")
        # Allow admin to add new user
        new_user = input("Enter new username to add: ")
        new_pwd = input("Enter password for the new user: ")
        user_credentials[new_user] = new_pwd
        print("New user added successfully!")
    else:
        print("Invalid admin username or password. Admin login denied.")

# Main program
def main():
    user_login()
    admin_login()

if __name__ == "__main__":
    main()
