import csv

#Return a dictionnary with {k = username, v = user balance}
def calc_balance():
    #Liste des utilisateurs pour les clefs
    user_list = []
    #Dictionnaire pour la balance
    user_balance = {}

    with open('users.csv', 'r') as user_file :
        users_reader = csv.reader(user_file, delimiter=';')
        for row in users_reader :
            user_list.append(row[0])
    
    #Initialisation de la balance 
    for user in user_list :
        user_balance[user] = 0

    with open('expense_report.csv', 'r', newline='') as expense_file : # Open with append to prevent erasing content + adding new expanses at the end.
        expense_reader = csv.reader(expense_file, delimiter=';')
        next(expense_reader) #Skipping header
        for row in expense_reader :
            #Get expense line data.
            amount = int(row[0])
            spender = row[2]
            debtor = []
            if len(row) > 3 : #If someone add an expense with no debtor
                for i in range(3, len(row)) :
                    debtor.append(row[i])
                    share = amount / (len(row) - 3) 
                for user in user_list :
                    if user in debtor :
                        user_balance[user] -= share
                # Account the spender for the money spent
                user_balance[spender] += amount

    print("Balance Calculated !")
    return user_balance, user_list

def status_report() :
    balance, user_list = calc_balance()
    print('There are ' + str(len(user_list)) + 'users')
    positive = []
    negative = []
    for user in user_list :
        if balance[user] < 0 :
            negative.append(user)
        elif balance[user] > 0 :
            positive.append(user)
    
    while not(len(negative) == 0) :
        balance[positive[0]] -= balance[negative[0]]
        print('User ' + negative[0] + ' owes ' + str(-balance[negative[0]]) + ' to ' + positive[0])
        negative.pop(0)
        if balance[positive[0]] < 0 :
            negative.append(positive.pop(0))
        elif balance[positive[0]] == 0 :
            positive.pop(0)
    return

