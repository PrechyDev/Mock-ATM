
#********* CRUD OPERATIONS ************
#create records
#read records
#update records
#delete record
#search for user

#create a file for each user as acct_number.txt
#add user_details to file and save to folder 'data/user_records' and return True
#if saving to file fails, delete created file, print error and return false

import os
from getpass import getpass
user_db_path = 'data/user_record/'

def create(acct_number, user_details):
    completion_state = False

    if user_exists(acct_number):
        return False

    try:
        f = open(user_db_path + str(acct_number) + '.txt', 'x')
            
    except FileExistsError:
        print('user already exists')
       
    else:
        f.write(str(user_details))
        completion_state = True
    
    finally:
        f.close()
        return completion_state
    
#find user_file with acct_number and fetch user_details
def read(acct_number):
    try:
        f = open(user_db_path + str(acct_number) + '.txt', 'r')
        details = (f.readline()).split(',')
        f.close()
        return details

    except FileNotFoundError:
        print('User does not exist')

#find user_file with acct_number 
#change user_details to a string and overwrite the content of the user_file
def update_balance(acct_number, user_details):
    f = open(user_db_path + str(acct_number) + '.txt', 'w')
    string_details = ','.join(user_details)
    f.write(string_details)
    f.close()

#find user_file with acct_number and delete file
def delete(acct_number):
    is_deleted = False

    try:
        os.remove(user_db_path + str(acct_number) + '.txt')
        print('User record deleted')
        is_deleted = True

    except FileNotFoundError:
        print('User does not exist')

    except TypeError:
        print('Invalid account number format')

    finally:
        return is_deleted
    
def user_exists(acct_number):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == (str(acct_number) + '.txt'):
            return True
    return False


def search_email(email):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        file = open(user_db_path + user, 'r')
        details = (file.readline()).split(',')
        if email in details:
            return True
    return False
        

#update_balance(3035267131,['prechy@gmail.com', 'Prechy', 'Okafor', 'prechy', '500'])
#read(3035267131)

