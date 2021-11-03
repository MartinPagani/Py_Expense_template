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
  
#Used for debtors prompting.
user_list = user_options() + ["No more user"]

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

debtor_question = [
    {
        "type":"list",
        "name":"debtor",
        "message":"Select debtors: ",
        "choices": user_list,
    },
]

def list_to_string(list) :
    ret = ""
    for e in list :
        ret += e + ';'
    return ret


def new_expense(*args):
    infos = prompt(expense_questions)
    debtors = [infos['spender']]
    user_list.remove(infos['spender'])

    debtor_info = prompt(debtor_question)
    while not(debtor_info['debtor'] == 'No more user') :
        debtors += [debtor_info['debtor']]
        user_list.remove(debtor_info['debtor'])
        debtor_info = prompt(debtor_question)

    with open('expense_report.csv', 'a', newline='') as save_file : # Open with append to prevent erasing content + adding new expanses at the end.
        expense_writer = csv.writer(save_file, delimiter=';')
        expense_writer.writerow([infos['amount']] + [infos['label']] + [infos['spender']] + debtors)
    print("Expense Added !")
    return True


