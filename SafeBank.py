import random

'''Banking app with a solid UI (user interface)
- Checking Balances
- Transferring Funds
- Depositing Money
- Withdrawing Money
- Checking Account limits
- Confirmation Prompts
'''


user_accounts = {"gian@yahoo.com": {"pin": "2287", "balance": 1000, "crdt_score": random.randint(300, 999)},
                "abbey@gmail.com": {"pin": "0228", "balance": 5000, "crdt_score": random.randint(300, 999)},
                "ari@yahoo.co.uk": {"pin": "1234", "balance": 400, "crdt_score": random.randint(300, 999)},
                "ariadne@yahoo.com": {"pin": "1111", "balance": 2000, "crdt_score": random.randint(300, 999)},
                "abigail@yahoo.co.uk": {"pin": "0000", "balance": 10000, "crdt_score": random.randint(300, 999)},
                "gianpalmares@gmail.com": {"pin": "2287", "balance": 10000, "crdt_score": random.randint(300, 999)}
                }


split_email = lambda email : email.split("@")[0].capitalize()


def login():
    while True:

        email = input("\nPlease enter your email address: ").strip()

        pin = input("\nPlease enter your 4-digit PIN number: ").strip()

        if login_check(email, pin):
            return email, pin


def login_check(email, pin):

    if email not in user_accounts.keys():
        print("Email account not valid! Please try again.")
        return False

    elif pin not in user_accounts[email]["pin"]:
        print("Incorrect PIN! Please try again.")
        return False

    else:
        username = split_email(email)
        print(f"Login successful! Welcome back {username}")
        return True


def check_balance(email):
    return user_accounts[email]["balance"]


def check_credit_score(email):

    if 800 <= user_accounts[email]["crdt_score"] <= 999:
        print(f"Hi {split_email(email)}! Your credit score is {user_accounts[email]['crdt_score']} which is Excellent!")

    elif  740 <= user_accounts[email]["crdt_score"] <= 799:
        print(f"Hi {split_email(email)}! Your credit score is {user_accounts[email]['crdt_score']} which is Very Good!")

    elif  670 <= user_accounts[email]["crdt_score"] <= 739:
        print(f"Hi {split_email(email)}! Your credit score is {user_accounts[email]['crdt_score']} which is Good!")

    elif  580 <= user_accounts[email]["crdt_score"] <= 669:
        print(f"Hi {split_email(email)}! Your credit score is {user_accounts[email]['crdt_score']} which is Fair!")

    elif  300 <= user_accounts[email]["crdt_score"] <= 579:
        print(f"Hi {split_email(email)}! Your credit score is {user_accounts[email]['crdt_score']} which is Poor!")


def balance_transfer(email, transfer_email, amount, pin):

    if amount <= user_accounts[email]["balance"]:

        while True:

            confirm_pin = input("\nPlease enter your 4-digit PIN number to confirm transfer: ").strip()

            if confirm_pin == pin:

                user_accounts[transfer_email]["balance"] += amount
                user_accounts[email]["balance"] -= amount
                username = split_email(transfer_email)
                
                print(f"You have transferred £ {amount} to {username}.")
                break

            else:
                print("Invalid PIN number! Please try again")
                continue

    else:
        print("Insufficient funds! Please make a deposit.")


print("\t\t\t__________________________________")
print("\n\t\t\t Welcome to SafeBank Banking App!")
print("\n\t\t\t Please enter your details below.")
print("\t\t\t__________________________________")

email, pin = login()

while True:

    print("\t\t\t__________________________________")
    print("\n\t\t\t Please select and option\n")
    print("\t\t\t 1. Check Balance")
    print("\t\t\t 2. Balance Transfer")
    print("\t\t\t 3. Deposit Money")
    print("\t\t\t 4. Withdraw Money")
    print("\t\t\t 5. Check Credit Score")
    print("\t\t\t 6. Log-out")
    print("\t\t\t 7. Exit")
    print("\t\t\t__________________________________")


    choice = input("\nPlease choose an option (1 - 7): ").strip()

    if choice == "1":
        print(f"Your account balance is: £ {check_balance(email)}")

    elif choice == "2":

        while True:

            transfer_email = input("\nPlease enter email you wish to make a balance transfer: ")

            if transfer_email in user_accounts.keys() and transfer_email != email:
                break

            else:
                print(f"Invalid email to transfer! Please try again.")
                continue

        while True:

            try:
                amount = float(input("\nPlease enter amount you wish to transfer: "))
                break

            except ValueError as e:
                print(f"Error : {e}! Please enter a numerical value.")
                continue

        balance_transfer(email, transfer_email, amount, pin)

    elif choice == "3":
        None

    elif choice == "4":
        None

    elif choice == "5":
        check_credit_score(email)

    elif choice == "6":
        email, pin = login()

    elif choice == "7":
        print("Exiting the banking application. Thank you!\n")
        break

    else:
        print("Invalid choice. Please choose a number from 1 to 7.")