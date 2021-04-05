from datetime import datetime
from collections import defaultdict
import random, re

database = {'0267962177': ['Seyi', 'Michael', 'seyi.michael@gmail.com', 'passwordSeyi', 24197],
            '0117562516': ['Mike', "Eneramo", 'mike.eneramo@yahoo.com', 'passwordMike', 45144],
            '0856081168': ['Love', 'Manuel', 'love.manuel@gmail.com', 'passwordLove', 38048],
            '0670876132': ['John', 'Samuel', 'john.samuel@gmail.com', 'passwordJohn', 86069]}

complaint_log = defaultdict(list)


def response(acc_num):
    print("\nWould You Like To Perform Another Transaction?")

    try:
        response = int(input(" 1 (Yes) or 2 (No): \n"))
        if response == 1:
            transaction(acc_num)
        else:
            exit()
    except ValueError:
        print("You have entered an invalid number")
        exit()


def withdrawalOperation(accountNumberFromUser):
    acc_num = accountNumberFromUser
    withdraw = float(input("How Much Would You Like To Withdraw? \n"))

    if withdraw <= database[acc_num][4]:
        database[acc_num][4] -= withdraw
        print('Please Take Your Cash!')
        response(acc_num)

    else:
        print('You Have Insufficient Funds To Complete This Transaction \n')
        response(acc_num)


def depositOperation(accountNumberFromUser):
    acc_num = accountNumberFromUser
    deposit = float(input("How Much Would You Like To Deposit? \n"))
    database[acc_num][4] += deposit
    print(f"Deposit of ${deposit} was successful! \nYour Current Balance is ${database[acc_num][4]}")
    response(acc_num)


def submitComplaint(accountNumberFromUser):
    acc_num = accountNumberFromUser
    complaint = input("What issue will you like to report? \n")
    complaint_log[acc_num].append(complaint)
    print("\nThank you for contacting us!")
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
    option = int(input("Please select an option: \n"))

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


def login():
    print("********* Welcome to AIG Bank Login Portal ***********")

    accountNumberFromUser = input("Enter Your Account Number: \n")
    passwordFromUser = input("Enter your password: \n")

    if accountNumberFromUser in database and passwordFromUser == database[accountNumberFromUser][3]:
        name = " ".join([database[accountNumberFromUser][0], database[accountNumberFromUser][1]])
        today = datetime.now().strftime("%d %B, %Y: %H:%M:%S")
        print(f"\nWelcome {name}, Logged in on {today} ")
        transaction(accountNumberFromUser)
    else:
        print('Invalid account or password')
        init()


def checkEmail(email_addr):
    p = re.compile('\S+@\S+\.?')
    if re.search(p, email_addr):
        return True
    else:
        print('Please Enter a valid email eg example@email.com \n')
        register()
        return False


def register():
    print("****** Welcome, To Create A New Account Enter Your Details: ******* \n")

    email = input("What is your email address? eg example@email.com \n")

    if checkEmail(email):
        first_name: str = (input("What is your first name? \n")).capitalize()
        last_name = (input("What is your last name? \n")).capitalize()
        password = input("Enter your password \n")

        accountNumber = generateAccountNumber()
        database[accountNumber] = [first_name, last_name, email, password, 0]

        print("Your Account Has been created successfully!")
        print("===================" * 3)
        print(f"Your account number is: {accountNumber}")
        print("===================" * 3)
        print("Make sure you keep it safe\n")

        login()


def init():
    print("============== Welcome to AIG Bank ==============")
    try:
        haveAccount = int(input("Do you have an account with us?: 1 (yes) 2 (no) \n"))

        if haveAccount == 1:
            login()

        elif haveAccount == 2:
            register()

        else:
            print("You have selected an invalid option")
            init()
    except ValueError:
        print("Please enter a valid number (1 or 2)")
        init()


if __name__ == "__main__":
    init()
