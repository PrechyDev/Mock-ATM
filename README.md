# Mock-ATM
Following the Zuri.team video tutorials, I have been able to update the mock_atm project i was working on to include 
several functions, features and modules

## Features
1. A `register` function connected to a local file system that creates a new user with a generated account number and saves the user details to a new txt file.

2. A `login` function that authenticates if the user input is a valid account number and if user exists. If password is correct, the user gets sent
to `bank operations`, else they try again.

3. A `banking` module  which has several banking operation functions connected to the local database, reading details from it and updating the account 
balance for every transaction.

4. A `validation` module that checks if the inputed account number is valid based on a few checks.

5. A `database` module that has basic `CRUD` functionalities for creating a new user, reading data from a user_file, updating a user account balance
and checking if a user exists before creating a new one.

#### Original repository - https://github.com/PrechyDev/Zuri
You'd find some other cool stuffs there. This is the beginning of my backend path 😎😎.
