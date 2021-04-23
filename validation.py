def account_number_validation(acct_number):
    #check if acct number is not empty
    #check if account number is 10 digits
    #check if acct number is an integer
    if acct_number:
        try:
            int(acct_number)
            if len(str(acct_number)) == 10:
                return True
            else:
                print('Account number cannot be less than or more than 10 digits')
                return False
        except ValueError:
            print('Invalid account number, must be an integer')
            return False
    else:
        print('Account Number is required')
        return False