

'''Banking app with a solid UI (user interface)
- Checking Balances
- Transferring Funds
- Depositing Money
- Withdrawing Money
- Checking Account limits
- Confirmation Prompts
'''

user_accounts = {"gian@yahoo.com": {"pin": "2287", "balance": 1000},
                "abbey@gmail.com": {"pin": "0228", "balance": 5000},
                "ari@yahoo.co.uk": {"pin": "1234", "balance": 400},
                "ariadne@yahoo.com": {"pin": "1111", "balance": 2000},
                "abigail@yahoo.co.uk": {"pin": "0000", "balance": 10000},
                "gianpalmares@gmail.com": {"pin": "2287", "balance": 10000}
                }

def login(email, pin):

    if email not in user_accounts.keys():
        print("Email account not valid! Please try again.")
        return False

    elif pin not in user_accounts[email]["pin"]:
        print("Incorrect PIN! Please try again.")
        return False

    else:
        username = email.split("@")
        print(f"Login successful!")
        print(f"Welcome back {username[0].capitalize()}!")
        return True

def check_balance(email):
    return user_accounts[email]["balance"]

def balance_transfer(email, transfer_email, amount, pin):

    if amount <= user_accounts[email]["balance"]:

        while True:

            confirm_pin = input("\nPlease enter your 4-digit PIN number to confirm transfer: ").strip()

            if confirm_pin == pin:

                user_accounts[transfer_email]["balance"] += amount
                user_accounts[email]["balance"] -= amount
                username = transfer_email.split("@")
                
                print(f"You have transferred £ {amount} to {username[0].capitalize()}.")
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


while True:

    email = input("\nPlease enter your email address: ").strip()

    pin = input("\nPlease enter your 4-digit PIN number: ").strip()

    if login(email, pin):
        break

while True:

    print("\t\t\t__________________________________")
    print("\t\t\t Please select and option")
    print("\t\t\t 1. Check Balance")
    print("\t\t\t 2. Balance Transfer")
    print("\t\t\t 3. Deposit Money")
    print("\t\t\t 4. Withdraw Money")
    print("\t\t\t 5. Exit")
    print("\t\t\t__________________________________")


    choice = input("\nPlease choose an option (1 - 5): ").strip()

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
        print("Exiting the banking app. Thank you!")
        break

    else:
        print("Invalid choice. Please choose a number between 1 and 5.")