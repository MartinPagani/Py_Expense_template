from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense
from user import user_questions,add_user
from balance import  status_report

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User","Print Status Report"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()
    elif (option['main_options']) == "New User":
        add_user()
        ask_option()
    elif (option['main_options']) == "Print Status Report":
        status_report()
        ask_option()
        return


def main():
    ask_option()

main()