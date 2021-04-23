import random
import validation
import banking
import database
from getpass import getpass ## this makes the password invisible on the terminal

#database = {7201519084: ['Prechy', 'Okafor', 'prechy@gmail.com', 'prechy', 0]}
 
#initializating the system
def init():
    print('Welcome to Bank P')
    
    have_account = int(input('Do you have an account with us? \n 1 (yes) 2 (no) \n'))

    if(have_account == 1):
        login()
    elif(have_account == 2):
        register()
    else:
        print('You have selected an invalid option')
        init()


#login
# - enter acct_number and password
def login():
    print('***Login to your account***')
    user_acct = input('Enter your account number \n')
    is_valid_account = validation.account_number_validation(user_acct)

    if is_valid_account:
        user_pwd = getpass('Enter your password \n')
        user_details = database.read(int(user_acct))

        if user_pwd == user_details[3]:
            print('Welcome %s %s' %(user_details[0], user_details[1]))
            banking.bank_operations(user_acct, user_details)
        else:
            print('invalid password')
            login()

    else:
        init()


#register
# - create email, f_name, l_name, password
# - generate user_account
def register():
    print('********Register******')
    email = input('Enter your email address: \n')
    f_name = input('Enter your first name: \n')
    l_name = input('Enter your last name: \n')
    password = getpass('Create a strong password: \n') 

    acct_number = generate_acct_number()
    balance = 0
    user_details = f_name + ',' + l_name + ',' + email + ',' + password + ',' + str(balance)

    user_created = database.create(acct_number, user_details) 
    
    if user_created:
        print('Welcome %s, your account has been created \n' %f_name)
        print('Your account number is %s \n' %acct_number)
        print('Ensure your keep your account number and password safe')
        login()
    else:
        print('something happened')
        init()


## generating account number for new user
def generate_acct_number():
    return random.randrange(1111111111,9999999999)


### ACTUAL BANKING SYSTEM ### 
init()
