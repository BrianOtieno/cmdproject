action = input("Enter Action: ")

comments = {}
    

data = {
    'username' : {'username' : 'Ian',
                    'password' : '1234',
                    'user_id' : 1
                    }
}

username = input("Enter username: ")
if action =="3":
    for username in data['username']:
        comment = input("Enter Comment: ")

        comments[len(comments)] = {
            'id' : len(comments)+1,
            'comment' : comment,
            'username' : data['username']['username']
        }
        

        print(comments)
