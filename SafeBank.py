

'''Banking app with a solid UI (user interface)
- Checking Balances
- Transferring Funds
- Depositing Money
- Withdrawing Money
- Checking Account limits
- Confirmation Prompts
'''

user_accounts = {"gian@yahoo.com": "2287",
                "abbey@gmail.com": "0228",
                "ari@yahoo.co.uk": "1234",
                "ariadne@yahoo.com": "1111",
                "abigail@yahoo.co.uk": "0000",
                "gianpalmares@gmail.com": "2222"
                }

def login(email, pin):

    if email not in user_accounts.keys():
        print("Email account not valid! Please try again.")

    elif pin not in user_accounts[email]:
        print("Incorrect PIN! Please trye again.")

    else:
        username = email.split("@")
        print(f"Welcome back {username[0].capitalize()}!")


print("\n\t\t\tWelcome to SafeBank Banking App!")
print("\n\t\t\tPlease enter your details below.")



email = input("\nPlease enter your email address: ").strip()

pin = input("\nPlease enter your 4-digit PIN number: ").strip()

login(email, pin)

