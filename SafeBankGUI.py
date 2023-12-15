import tkinter as tk
from tkinter import messagebox
import random

user_accounts = {
    "gian@yahoo.com": {"pin": "2287", "balance": 1000, "credit_score": random.randint(300, 999)},
    "abbey@gmail.com": {"pin": "0228", "balance": 5000, "credit_score": random.randint(300, 999)},
    "ari@yahoo.co.uk": {"pin": "1234", "balance": 400, "credit_score": random.randint(300, 999)},
    "ariadne@yahoo.com": {"pin": "1111", "balance": 2000, "credit_score": random.randint(300, 999)},
    "abigail@yahoo.co.uk": {"pin": "0000", "balance": 10000, "credit_score": random.randint(300, 999)},
    "gianpalmares@gmail.com": {"pin": "2287", "balance": 10000, "credit_score": random.randint(300, 999)}
}

split_email = lambda email: email.split("@")[0].capitalize()

def login():
    while True:
        email = input("\nPlease enter your email address: ").strip()
        pin = input("\nPlease enter your 4-digit PIN number: ").strip()
        if login_check(email, pin):
            return email, pin

def logout():
    while True:
        yes_or_no = input("\nAre you sure you want to log-out? ('yes' or 'no'): ").lower().strip()
        if yes_or_no == "yes":
            print(f"Logging out. Goodbye, {split_email(email)}!")
            return login()
        elif yes_or_no == "no":
            print("Log-out canceled.")
            return email, pin
        else:
            print("Invalid choice! Please select 'yes' or 'no'.")
            continue

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
    print(f"Your account balance is: £ {user_accounts[email]['balance']}")

def check_credit_score(email):
    if 800 <= user_accounts[email]["credit_score"] <= 999:
        print(f"Hi {split_email(email)}! Your credit score is {user_accounts[email]['credit_score']} which is Excellent!")
    elif 740 <= user_accounts[email]["credit_score"] <= 799:
        print(f"Hi {split_email(email)}! Your credit score is {user_accounts[email]['credit_score']} which is Very Good!")
    elif 670 <= user_accounts[email]["credit_score"] <= 739:
        print(f"Hi {split_email(email)}! Your credit score is {user_accounts[email]['credit_score']} which is Good!")
    elif 580 <= user_accounts[email]["credit_score"] <= 669:
        print(f"Hi {split_email(email)}! Your credit score is {user_accounts[email]['credit_score']} which is Fair!")
    elif 300 <= user_accounts[email]["credit_score"] <= 579:
        print(f"Hi {split_email(email)}! Your credit score is {user_accounts[email]['credit_score']} which is Poor!")

def transfer_check():
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
            print(f"ValueError : {e}! Please enter a numerical value.")
            continue
    return transfer_email, amount

def balance_transfer(email, transfer_email, amount, pin):
    if amount <= user_accounts[email]["balance"]:
        while True:
            confirm_pin = input("\nPlease enter your 4-digit PIN number to confirm balance transfer: ").strip()
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

# Function to log out and update login credentials
def handle_logout():
    global email, pin
    result = messagebox.askyesno("Log-out", f"Are you sure you want to log-out, {split_email(email)}?")
    
    if result:
        email, pin = login()
        update_balance_label()  # Update balance label after login

# Initialization
email, pin = login()

# Create main window
root = tk.Tk()
root.title("SafeBank Banking App")

# Tkinter GUI functions

# Function to update the balance label
def update_balance_label():
    balance_label.config(text=f"Your account balance is: £ {user_accounts[email]['balance']}")

# Function to handle the balance transfer
def handle_balance_transfer():
    transfer_email, amount = transfer_check()

    if amount > user_accounts[email]["balance"]:
        messagebox.showinfo("Insufficient Funds", "Insufficient funds! Please make a deposit.")
    else:
        balance_transfer(email, transfer_email, amount, pin)
        update_balance_label()

# Function to log out and update login credentials
def handle_logout():
    global email, pin
    result = messagebox.askyesno("Log-out", f"Are you sure you want to log-out, {split_email(email)}?")
    
    if result:
        email, pin = login()
        update_balance_label()  # Update balance label after login

# Create main window
root = tk.Tk()
root.title("SafeBank Banking App")

# Create and place widgets
welcome_label = tk.Label(root, text="Welcome to SafeBank Banking App!", font=("Helvetica", 16))
welcome_label.pack(pady=10)

balance_label = tk.Label(root, text="")
balance_label.pack(pady=10)

button_check_balance = tk.Button(root, text="Check Balance", command=lambda: check_balance(email))
button_check_balance.pack()

button_balance_transfer = tk.Button(root, text="Balance Transfer", command=handle_balance_transfer)
button_balance_transfer.pack()

button_logout = tk.Button(root, text="Log-out", command=handle_logout)
button_logout.pack()

root.mainloop()
