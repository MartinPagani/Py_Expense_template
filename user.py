from PyInquirer import prompt

user_questions = [
    {
        "type":"input",
        "name":"username",
        "message":"Username: ",
    },
]

def add_user():
    infos = prompt(user_questions)


    # This function should create a new user, asking for its name
    print("User Added !")
    return True