import database

#bank operations
def bank_operations(acct_number, user):
    print('What would you like to do? \n')
    print('1. Deposit')
    print('2. Withdrawal')
    print('3. Check account balance')
    print('4. Logout')
 

    selected_option = int(input('Select an option \n'))

    if(selected_option == 1):
        deposit(acct_number, user) 
    elif(selected_option == 2):
        withdraw(acct_number, user)
    elif(selected_option == 3):
        check_balance(acct_number, user)
    elif(selected_option == 4):
        print('Thank you for banking with us')
        exit()
    else:
        print('Invalid option, try again')
        bank_operations(acct_number, user)


def withdraw(acct_number, user):
    amount = int(input('How much would you like to withdraw? \n'))
    balance = int(user[-1])
    if amount >= balance:
        print('Insufficient Funds')
        retry = int(input('Would you like to try again or deposit funds? \n 1. Retry 2. Deposit 3. exit \n'))
        if(retry == 1):
            withdraw(acct_number, user)
        if(retry == 2):
            deposit(acct_number, user)
        else:
            print('Thank you for banking with us')
            exit()

    else:
        balance -= amount #subtracts amount from user_balance
        user[-1] = str(balance)
        database.update_balance(acct_number, user)

        print('Take your cash')
        print('Do you want to make another transaction?')
        option = int(input(' 1.Yes 2.No \n'))

        

        if(option == 1):
            bank_operations(acct_number, user)
        elif(option == 2):
            print('Thank you for banking with us')
            exit()

def deposit(acct_balance, user):
    amount = int(input('How much do you want to deposit? \n'))
    balance = int(user[-1])
    balance += amount #subtracts amount from user_balance
    user[-1] = str(balance)
    database.update_balance(acct_balance, user)

    print('Deposit successful')
    print('Your current account balance is %s' %balance)
    print('Do you want to make another transaction?')
    option = int(input(' 1.Yes 2.No \n'))

    if(option == 1):
        bank_operations(acct_balance, user)
    else:
        print('Thank you for banking with us')
        exit()

def check_balance(acct_balance, user):
    acct_balance = int(user[-1])
    print('Your account balance is %s' %acct_balance)

    print('Do you want to make another transaction?')
    option = int(input(' 1.Yes 2.No \n'))

    if(option == 1):
        bank_operations(acct_balance, user)
    else:
        print('Thank you for banking with us')
        exit()


