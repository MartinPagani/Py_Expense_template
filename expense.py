from PyInquirer import prompt
import csv

# Fetching user list for expense_questions
def user_options() :
    user_options_list = []
    with open('users.csv', 'r', newline='') as user_file :
        user_reader = csv.reader(user_file, delimiter=';')
        for row in user_reader :
            user_options_list.append(row[0]) #Elseway adding list of list, breaking the engine.
    return user_options_list
  


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"Which user is the spender ? ",
        "choices": user_options(),
    },

]




def new_expense(*args):
    infos = prompt(expense_questions)

    with open('expense_report.csv', 'a', newline='') as save_file : # Open with append to prevent erasing content + adding new expanses at the end.
        expense_writer = csv.writer(save_file, delimiter=';')
        expense_writer.writerow([infos['amount']] +  [infos['label']] + [infos['spender']])
    print("Expense Added !")
    return True


