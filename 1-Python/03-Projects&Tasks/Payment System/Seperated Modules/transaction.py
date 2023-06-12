from tkinter import messagebox
from screens import return_to_home

def withdraw_cash(amount):
    if amount % 100 != 0:
        messagebox.showerror("Invalid Amount", "Withdrawal amount must be a multiple of 100.")
    elif amount > account_data[current_account]["balance"]:
        messagebox.showerror("Insufficient Balance", "No sufficient balance.")
    elif amount > 5000:
        messagebox.showerror("Maximum Limit Exceeded", "Maximum allowed value per transaction is 5000 L.E.")
    else:
        account_data[current_account]["balance"] -= amount
        messagebox.showinfo("Withdrawal Successful", f"Withdrawal of {amount} L.E. successful.")
        return_to_home()


def balance_inquiry():
    balance = account_data[current_account]["balance"]
    name = account_data[current_account]["name"]
    messagebox.showinfo("Balance Inquiry", f"Name: {name}\nBalance: {balance} L.E.")
    return_to_home()


def change_password(new_password1, new_password2):
    if new_password1 == new_password2 and len(new_password1) == 4:
        account_data[current_account]["password"] = new_password1
        messagebox.showinfo("Password Change Successful", "Password changed successfully.")
        return_to_home()
    else:
        messagebox.showerror("Invalid Password", "New passwords do not match or have an invalid length.")

