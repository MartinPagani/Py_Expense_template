from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"username",
        "message":"Username: ",
    },
]

# On vérifie si l'utilisateur existe pour ne pas avoir des noms en doublon
# Mode r avec catch => ne pas planter si le ficher n'existe pas, il faut le créer dans ce cas ce qui est fait en ouverture a après.
def user_exist(name):
    try :
        with open('users.csv', 'r') as save_file :
            users_reader = csv.reader(save_file, delimiter=';')
            for row in users_reader :
                if row[0] == name :
                    return True
    except :
        return False


def add_user():
    infos = prompt(user_questions)

    if not(user_exist(infos['username'])) :
        with open('users.csv', 'a', newline='') as save_file :
            user_writer = csv.writer(save_file, delimiter=';')
            user_writer.writerow([infos['username']])
            print("User Added !")
            return True
    print ("Operation aborted - Username already exist")
    return False