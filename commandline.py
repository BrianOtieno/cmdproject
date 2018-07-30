import re

data = {}
Comments = {"id": 1, "comment": "Some comment"}

print("==> Select Action To Continue")
print("1: Create User 2: Login 3: Add Comments 4: Edit Comments 5:\
Delete Comments")

action = input("Enter Action: ")

if action ==1:
    firstname = raw_input("Enter First Name: ")
    lastname = raw_input("Enter Last Name: ")
    username = raw_input("Enter Username: ")
    email = raw_input("Enter Email: ")
    password = raw_input("Enter password: ")
    password = raw_input("Enter password: ")
    role = raw_input("Enter role: ")

    if not firstname or not lastname or not username or not email or not password:
        print("All user datails are required!")

    if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",
        email):
        print("Invalid Email")

    def add_user(firstname, lastname, username, email):
        def__init__(self, firstname, lastname, username, email)
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password

    data['username'] = {"firstname": firstname, "lastname": lastname,
    "email": email, "username": username}
    print(data)

if action == 5:
    print("Provide Details for Deletion")
    username = raw_input("Enter Username: ")
    comment_id = raw_input("Enter Comment ID: ")

    if not username or not comment_id:
        print("Both username and password are required")
    if Comments:
        if data[username]['username'] == username:
            data.pop(Comments['id'], None)
            print("Comment Deleted Successfully!")
        print("An error occured! Check if ID exists.")
