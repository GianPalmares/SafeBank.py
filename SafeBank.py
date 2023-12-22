import random as rd
import math



# User account details stored in a dictionary
user_accounts = {"gian@yahoo.com": {"pin": "2287", "balance": 10000.00, "credit_score": rd.randint(300, 999)},
                "abbey@gmail.com": {"pin": "0228", "balance": 50000.00, "credit_score": rd.randint(300, 999)},
                "ari@yahoo.co.uk": {"pin": "1234", "balance": 4000.00, "credit_score": rd.randint(300, 999)},
                "ariadne@yahoo.com": {"pin": "1111", "balance": 20000.00, "credit_score": rd.randint(300, 999)},
                "abigail@yahoo.co.uk": {"pin": "0000", "balance": 100000.00, "credit_score": rd.randint(300, 999)},
                "gianpalmares@gmail.com": {"pin": "2287", "balance": 100000.00, "credit_score": rd.randint(300, 999)},
                "john.doe@gmail.com": {"pin": "4321", "balance": 15000.00, "credit_score": rd.randint(300, 999)},
                "mary.smith@yahoo.com": {"pin": "9876", "balance": 75000.00, "credit_score": rd.randint(300, 999)},
                "samuel.jones@hotmail.com": {"pin": "5678", "balance": 3000.00, "credit_score": rd.randint(300, 999)},
                "emily.wilson@gmail.com": {"pin": "1357", "balance": 25000.00, "credit_score": rd.randint(300, 999)},
                "olivia.brown@yahoo.co.uk": {"pin": "2468", "balance": 80000.00, "credit_score": rd.randint(300, 999)},
                "william.taylor@gmail.com": {"pin": "7890", "balance": 12000.00, "credit_score": rd.randint(300, 999)},
                "leonardo.dicaprio@gmail.com": {"pin": "1234", "balance": 5000000.00, "credit_score": rd.randint(300, 999)},
                "scarlett.johansson@yahoo.com": {"pin": "5678", "balance": 300000.00, "credit_score": rd.randint(300, 999)},
                "brad.pitt@hotmail.com": {"pin": "9876", "balance": 10000000.00, "credit_score": rd.randint(300, 999)},
                "angelina.jolie@gmail.com": {"pin": "4321", "balance": 800000.00, "credit_score": rd.randint(300, 999)},
                "dwayne.johnson@yahoo.co.uk": {"pin": "2468", "balance": 1500000.00, "credit_score": rd.randint(300, 999)},
                "jennifer.lopez@gmail.com": {"pin": "1357", "balance": 2000000.00, "credit_score": rd.randint(300, 999)},
                "tom.hanks@yahoo.com": {"pin": "0000", "balance": 500000.00, "credit_score": rd.randint(300, 999)},
                "meryl.streep@yahoo.co.uk": {"pin": "1111", "balance": 100000.00, "credit_score": rd.randint(300, 999)},
                }


# Lambda function to split email and capitalize the username
split_email = lambda email : email.split("@")[0].capitalize()

# Lambda function for invalid choice message
invalid_choice_message = lambda : print("Invalid choice! Please select a number from 1 to 7.")



# Function for user login
def login():

    print("\t\t\t__________________________________")
    print("\n\t\t\t Welcome to SafeBank Banking App!")
    print("\n\t\t\t Please enter your details below.")
    print("\t\t\t__________________________________")

    while True:

        email = input("\nPlease enter your email address: ").strip()

        pin = input("\nPlease enter your 4-digit PIN number: ").strip()

        if login_check(email, pin):

            return email, pin


# Function to check if login credentials are valid
def login_check(email, pin):

    if email not in user_accounts.keys():

        print("Email account not valid! Please try again.")
        return False

    elif pin != user_accounts[email]["pin"]:

        print("Incorrect PIN! Please try again.")
        return False

    else:

        username = split_email(email)
        print(f"Login successful! Welcome back {username}.")
        return True
    

# Function for user logout
def logout(email):

    while True:

        yes_or_no = input("\nAre you sure you want to log-out? ('yes' or 'no'): ").lower().strip()

        if yes_or_no == "yes":

            print(f"Logging out. Goodbye, {split_email(email)}!")
            start_banking()

        elif yes_or_no == "no":

            print("Log-out canceled.")
            break

        else:

            print("Invalid choice! Please select 'yes' or 'no'.")
            continue


# Function to check and display account balance
def check_balance(email):

    print(f"Your account balance is: £{round(user_accounts[email]['balance'], 2): ,}")


# Function to check and display credit score
def check_credit_score(email):

    user_score = user_accounts[email]["credit_score"]

    if 800 <= user_score <= 999:

        print(f"Hi {split_email(email)}! Your credit score is {user_score} which is Excellent!")

    elif  740 <= user_score <= 799:

        print(f"Hi {split_email(email)}! Your credit score is {user_score} which is Very Good!")

    elif  670 <= user_score <= 739:

        print(f"Hi {split_email(email)}! Your credit score is {user_score} which is Good!")

    elif  580 <= user_score <= 669:

        print(f"Hi {split_email(email)}! Your credit score is {user_score} which is Fair!")

    elif  300 <= user_score <= 579:

        print(f"Hi {split_email(email)}! Your credit score is {user_score} which is Poor!")


# Function to get transfer details from the user
def transfer_check(email):

        while True:

            transfer_email = input("\nPlease enter email you wish to make a balance transfer: ").strip()

            if transfer_email in user_accounts.keys() and transfer_email != email:

                break

            else:

                print(f"Invalid email to transfer! Please try again.")
                continue

        while True:

            try:

                amount = math.floor(float(input("\nPlease enter amount you wish to transfer: £ ")) * 100) / 100

                if is_positive(amount):

                    break

                continue

            except ValueError as e:

                print(f"ValueError : {e}! Please enter a numerical value.")
                continue

        return transfer_email, amount


# Function to perform balance transfer
def balance_transfer(email, transfer_email, amount, pin):

    attempts = 3

    if amount <= user_accounts[email]["balance"]:

        while True:

            confirm_pin = input("\nPlease enter your 4-digit PIN number to confirm balance transfer: ").strip()

            if confirm_pin == pin:

                user_accounts[transfer_email]["balance"] += amount
                user_accounts[email]["balance"] -= amount

                print(f"You have successfully transferred £{amount: ,} to {split_email(transfer_email)}.")
                break

            else:

                if attempts == 0:

                    print(f"Sorry {split_email(email)}, you have entered your PIN number incorrectly too many times. Logging out!")
                    start_banking()

                else:

                    print(f"Invalid PIN number! Please try again, you have {attempts} attempts left.")
                    attempts -= 1
                    continue

    else:
        print("Insufficient funds! Please make a deposit.")


# Function to complete a balance transfer
def complete_balance_transfer(email, pin):

    transfer_email, amount = transfer_check(email)
    balance_transfer(email, transfer_email, amount, pin)


# Function to check if an amount is positive
def is_positive(amount):

    if amount > 0:

        return True

    else:

        print("Please enter a positive amount.")
        return False


# Function for user deposit
def deposit(email):

    while True:

        try:

            amount = math.floor(float(input("\nPlease enter amount you wish to deposit: £ ")) * 100) / 100

            if is_positive(amount):

                break

            continue

        except ValueError as e:

            print(f"ValueError : {e}! Please enter a numerical value.")
            continue

    user_accounts[email]["balance"] += amount
    username = split_email(email)
    print(f"Hey {username}! Thank you for depositing £{amount: ,} in to your account.")


# Function for user withdrawal
def withdrawal(email, pin):

    attempts = 3
    username = split_email(email)

    while True:

        try:

            amount = int(float(input("\nPlease enter the amount you wish to withdraw(Can only withdraw integers): £ ")))

            if is_positive(amount):

                if amount > user_accounts[email]["balance"]:

                    print("Insufficient funds! Please make a deposit.")
                    break

                else:

                    while True:

                        confirm_pin = input("\nPlease enter your 4-digit PIN number to confirm withdrawal: ").strip()

                        if confirm_pin == pin:

                            user_accounts[email]["balance"] -= amount

                            print(f"You have successfully withdrawn £{amount: ,}. Thank you, {username}!")
                            break

                        else:

                            if attempts == 0:

                                print(f"Sorry {username}, you have entered your PIN number incorrectly too many times. Logging out!")
                                start_banking()

                            else:

                                print(f"Invalid PIN number! Please try again, you have {attempts} attempts left.")
                                attempts -= 1

                    break

        except ValueError as e:

            print(f"ValueError : {e}! Please enter a numerical value.")
            continue 


# Function to exit the application
def exit_application():

    print("Exiting the application. Thank you for using SafeBank!\n")
    exit()



# Main part of the program as a function
def start_banking():

    email, pin = None, None

    # Main menu loop
    while True:

        # Get user login credentials
        if email is None or pin is None:

            email, pin = login()

        print("\n\t\t\t__________________________________")
        print("\n\t\t\t Please select an option\n")
        print("\t\t\t [1]. Check Balance")
        print("\t\t\t [2]. Balance Transfer")
        print("\t\t\t [3]. Deposit Money")
        print("\t\t\t [4]. Withdraw Money")
        print("\t\t\t [5]. Check Credit Score")
        print("\t\t\t [6]. Log-out")
        print("\t\t\t [7]. Exit")
        print("\t\t\t__________________________________")


        # Get user choice
        choice = input("\nPlease select an option (1 - 7): ").strip()

        # Process user choice
        if choice == "1":

            check_balance(email)

        elif choice == "2":

            complete_balance_transfer(email, pin)

        elif choice == "3":

            deposit(email)

        elif choice == "4":

            withdrawal(email, pin)

        elif choice == "5":

            check_credit_score(email)

        elif choice == "6":

            logout(email)

        elif choice == "7":

            exit_application()

        else:

            invalid_choice_message()


# Start the banking application
start_banking()