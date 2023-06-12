from tkinter import messagebox

def validate_account(account_number):
    global current_account
    if account_number in account_data:
        current_account = account_number
        return True
    else:
        messagebox.showerror("Invalid Account", "Account number is not identified.")
        return False


def validate_password(password):
    global password_attempts, current_account
    if account_data[current_account]["password"] == password:
        password_attempts = 0
        return True
    else:
        password_attempts += 1
        if password_attempts == 3:
            messagebox.showerror("Account Locked", "Account locked. Please go to the branch.")
            current_account = None
        else:
            messagebox.showerror("Incorrect Password", "Incorrect password. Please try again.")
        return False
