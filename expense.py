from PyInquirer import prompt
import csv

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
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]



  #  with open('eggs.csv', 'w', newline='') as csvfile:
   #     spamwriter = csv.writer(csvfile, delimiter=' ',
    #                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
     #   spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
      #  spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

def new_expense(*args):
    infos = prompt(expense_questions)

    with open('expense_report.csv', 'a', newline='') as save_file : # Open with append to prevent erasing content + adding new expanses at the end.
        expense_writer = csv.writer(save_file, delimiter=';')
        expense_writer.writerow([infos['amount']] +  [infos['label']] + [infos['spender']])
    print("Expense Added !")
    return True


