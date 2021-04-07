import random
import re
from collections import defaultdict
from datetime import datetime

database = {'0267962177': ['Seyi', 'Michael', 'seyi.michael@gmail.com', 'passwordSeyi', 24197],
            '0117562516': ['Mike', "Eneramo", 'mike.eneramo@yahoo.com', 'passwordMike', 45144],
            '0856081168': ['Love', 'Manuel', 'love.manuel@gmail.com', 'passwordLove', 38048],
            '0670876132': ['John', 'Samuel', 'john.samuel@gmail.com', 'passwordJohn', 86069]}

complaint_log = defaultdict(list)


def response(acc_num):
    print("\nWould You Like To Perform Another Transaction?")

    try:
        res = int(input(" 1 (Yes) or 2 (No): \n"))
        if res == 1:
            transaction(acc_num)
        if res == 2:
            print("Thank You For Banking With Us, Enjoy The Rest Of Your Day!")
            exit()
        else:
            print("You Have Selected An Invalid Option, Try Again")
            response(acc_num)

    except ValueError:
        print("You Have Entered An Invalid Number")
        response(acc_num)


def withdrawalOperation(accountNumberFromUser):
    acc_num = accountNumberFromUser

    try:
        withdraw = float(input("How Much Would You Like To Withdraw? \n"))

        if withdraw <= database[acc_num][4]:
            database[acc_num][4] -= withdraw
            print('Please Take Your Cash!')
            response(acc_num)

        else:
            print('You Have Insufficient Funds To Complete This Transaction \n')
            response(acc_num)
    except ValueError:
        print("Please Enter a Valid Number \n")
        withdrawalOperation(accountNumberFromUser)




def depositOperation(accountNumberFromUser):
    acc_num = accountNumberFromUser

    try:
        deposit = float(input("How Much Would You Like To Deposit? \n"))
        database[acc_num][4] += deposit
        print(f"Deposit Of ${deposit} Was Successful! \nYour Current Balance Is ${database[acc_num][4]}")
        response(acc_num)

    except ValueError:
        print("Please Enter A Valid Number \n")
        depositOperation(accountNumberFromUser)


def submitComplaint(accountNumberFromUser):
    acc_num = accountNumberFromUser
    complaint = input("What Issue Would You Like To Report? \n")
    complaint_log[acc_num].append(complaint)
    print("\nThank You For Contacting Us!")
    response(acc_num)


def checkBalance(accountNumberFromUser):
    acc_num = accountNumberFromUser
    avail_balance = database[acc_num][4]
    print("===================" * 3)
    print(f"Your Available Balance is ${avail_balance}")
    print("===================" * 3)
    response(acc_num)


def generateAccountNumber():
    acc_num = f'{(random.randrange(1, 999999999)):010d}'
    return acc_num


def logout():
    init()


def transaction(accountNumberFromUser):
    print("\nWhat Would You Like To Do: \n 1. Make A Withdrawal \n 2. Cash Deposit \n 3. Submit A Complaint \n 4. "
          "Check Balance \n 5. Log out \n")

    try:
        option = int(input("Please Select An Option: \n"))

        if option == 1:
            withdrawalOperation(accountNumberFromUser)

        elif option == 2:
            depositOperation(accountNumberFromUser)

        elif option == 3:
            submitComplaint(accountNumberFromUser)

        elif option == 4:
            checkBalance(accountNumberFromUser)

        elif option == 5:
            logout()

        else:
            print("Invalid Option Selected, Please Try Again \n")
            transaction(accountNumberFromUser)

    except ValueError:
        print("You Have Entered An InValid Number, Try Again \n")
        transaction(accountNumberFromUser)


def login():
    print("\n********* Welcome to AIG Bank Login Portal ***********")

    accountNumberFromUser = input("Enter Your Account Number: \n")
    passwordFromUser = input("Enter your password: \n")

    if accountNumberFromUser in database and passwordFromUser == database[accountNumberFromUser][3]:
        name = " ".join([database[accountNumberFromUser][0], database[accountNumberFromUser][1]])
        today = datetime.now().strftime("%d %B, %Y: %H:%M:%S")
        print(f"\nWelcome {name}, Logged in on {today} ")
        transaction(accountNumberFromUser)
    else:
        print('Invalid Account Number or Password')
        init()


def check_email(email):
    p = re.compile('\S+@\S+\.?')

    if re.search(p, email):
        return True

    else:
        return False


def email_caller():
    email = input("Enter Your Email Address? eg example@email.com \n")
    if check_email(email):
        return email
    else:
        return email_caller()


def password_checker(password):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    pat = re.compile(reg)
    match = re.search(pat, password)

    if match:
        return True

    else:
        return False


def password_caller():
    password = input("\nChoose your password\n"
                     "--------------------------------\n"                        
                     "Conditions For A Valid Password: \n"
                     "--------------------------------\n"
                     "1. Should have at least one number.\n"
                     "2. Should have at least one uppercase and one lowercase character. \n"
                     "3. Should have at least one special symbol. \n"
                     "4. Should be between 6 to 20 characters long.\n"
                     "\nEnter your password: \n")

    if password_checker(password):
        return password

    else:
        return password_caller()


def register():
    print("****** Welcome, To Create A New Account Enter Your Details: ******* \n")

    first_name: str = (input("What Is Your First Name? \n")).capitalize()
    last_name = (input("What Is Your Last Name? \n")).capitalize()
    email = email_caller()
    password = password_caller()

    accountNumber = generateAccountNumber()
    database[accountNumber] = [first_name, last_name, email, password, 0]

    print("\nYour Account Has Been Created Successfully!")
    print("===================" * 3)
    print(f"Your Account Number Is: {accountNumber}")
    print("===================" * 3)
    print("Make Sure You Keep It Safe\n")

    login()


def init():
    print("============== Welcome to AIG Bank ==============")

    try:
        haveAccount = int(input("Do You Have An Account With Us?: 1 (yes) 2 (no) \n"))

        if haveAccount == 1:
            login()

        elif haveAccount == 2:
            register()

        else:
            print("You Have Selected An Invalid Option")
            init()

    except ValueError:
        print("Please Enter A Valid Number (1 or 2)")
        init()


if __name__ == "__main__":
    init()
