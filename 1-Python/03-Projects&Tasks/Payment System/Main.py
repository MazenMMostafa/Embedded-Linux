import tkinter as tk
from tkinter import messagebox

# Sample account data
account_data = {
    "215321701332": {
        "name": "Ahmed Abdelrazek Mohamed",
        "password": "1783",
        "balance": 3500166
    },
    "203659302214": {
        "name": "Salma Mohamed Foaad",
        "password": "1390",
        "balance": 520001
    },
    # Add other account data here...
}

# Global variables
current_account = None
password_attempts = 0

# GUI Setup
window = tk.Tk()
window.title("ATM Software")


# Helper functions
def validate_account(account_number):
    global current_account  # Access the global variable current_account
    if account_number in account_data:  # Check if the account number exists in the account_data dictionary
        current_account = account_number  # Set the current_account to the validated account number
        return True  # Return True to indicate successful validation
    else:
        messagebox.showerror("Invalid Account", "Account number is not identified.")  # Display an error message box
        return False  # Return False to indicate failed validation


def validate_password(password):
    global password_attempts, current_account  # Access the global variables password_attempts and current_account
    if account_data[current_account][
        "password"] == password:  # Check if the entered password matches the stored password
        password_attempts = 0  # Reset the password_attempts counter
        return True  # Return True to indicate successful password validation
    else:
        password_attempts += 1  # Increment the password_attempts counter
        if password_attempts == 3:  # Check if the maximum attempts limit has been reached
            messagebox.showerror("Account Locked",
                                 "Account locked. Please go to the branch.")  # Display an error message box
            current_account = None  # Reset the current_account
        else:
            messagebox.showerror("Incorrect Password",
                                 "Incorrect password. Please try again.")  # Display an error message box
        return False  # Return False to indicate failed password validation


def withdraw_cash(amount):
    if amount % 100 != 0:  # Check if the withdrawal amount is not a multiple of 100
        messagebox.showerror("Invalid Amount",
                             "Withdrawal amount must be a multiple of 100.")  # Display an error message box
    elif amount > account_data[current_account][
        "balance"]:  # Check if the withdrawal amount exceeds the account balance
        messagebox.showerror("Insufficient Balance", "No sufficient balance.")  # Display an error message box
    elif amount > 5000:  # Check if the withdrawal amount exceeds the maximum limit
        messagebox.showerror("Maximum Limit Exceeded",
                             "Maximum allowed value per transaction is 5000 L.E.")  # Display an error message box
    else:
        account_data[current_account]["balance"] -= amount  # Deduct the withdrawal amount from the account balance
        messagebox.showinfo("Withdrawal Successful",
                            f"Withdrawal of {amount} L.E. successful.")  # Display a success message box
        return_to_home()  # Return to the home screen


def balance_inquiry():
    balance = account_data[current_account]["balance"]  # Get the account balance
    name = account_data[current_account]["name"]  # Get the account holder's name
    messagebox.showinfo("Balance Inquiry",
                        f"Name: {name}\nBalance: {balance} L.E.")  # Display the account holder's name and balance
    return_to_home()  # Return to the home screen


def change_password(new_password1, new_password2):
    if new_password1 == new_password2 and len(
            new_password1) == 4:  # Check if the new passwords match and have a length of 4
        account_data[current_account]["password"] = new_password1  # Update the account's password
        messagebox.showinfo("Password Change Successful",
                            "Password changed successfully.")  # Display a success message box
        return_to_home()  # Return to the home screen
    else:
        messagebox.showerror("Invalid Password",
                             "New passwords do not match or have invalid length.")  # Display an error message box


def recharge_service(service):
    # Implementation for Fawry service recharge
    messagebox.showinfo("Recharge Service",
                        f"Recharging {service} service.")  # Display a message indicating the service recharge
    return_to_home()  # Return to the home screen


def return_to_home():
    global current_account
    current_account = None  # Reset the current account
    password_attempts = 0  # Reset the password attempts counter
    show_home_screen()  # Display the home screen


def show_home_screen():
    home_screen = tk.Frame(window)  # Create a frame for the home screen
    home_screen.pack(pady=20)  # Set the padding for the frame

    account_label = tk.Label(home_screen, text="Enter Account Number:")  # Create a label for the account number entry
    account_label.pack()  # Display the account label
    account_entry = tk.Entry(home_screen, width=30)  # Create an entry field for the account number
    account_entry.pack(pady=10)  # Display the account entry field

    def enter_account():
        account_number = account_entry.get()  # Get the entered account number
        if validate_account(account_number):  # Validate the account number
            home_screen.pack_forget()  # Hide the home screen
            show_password_screen()  # Display the password screen

    enter_button = tk.Button(home_screen, text="Enter", command=enter_account)  # Create a button to enter the account
    enter_button.pack()  # Display the enter button


def show_password_screen():
    password_screen = tk.Frame(window)  # Create a frame for the password screen
    password_screen.pack(pady=20)  # Set the padding for the frame

    password_label = tk.Label(password_screen, text="Enter Password:")  # Create a label for the password entry
    password_label.pack()  # Display the password label
    password_entry = tk.Entry(password_screen, show="*", width=30)  # Create an entry field for the password
    password_entry.pack(pady=10)  # Display the password entry field

    def submit_password():
        password = password_entry.get()  # Get the entered password
        if validate_password(password):  # Validate the password
            password_screen.pack_forget()  # Hide the password screen
            show_options_screen()  # Display the options screen

    submit_button = tk.Button(password_screen, text="Submit",
                              command=submit_password)  # Create a button to submit the password
    submit_button.pack()  # Display the submit button


def show_options_screen():
    options_screen = tk.Frame(window)  # Create a frame for the options screen
    options_screen.pack(pady=20)  # Set the padding for the frame

    withdraw_button = tk.Button(options_screen, text="Cash Withdraw",
                                command=show_withdraw_screen)  # Create a button for cash withdrawal
    withdraw_button.pack(pady=5)  # Display the cash withdrawal button

    balance_button = tk.Button(options_screen, text="Balance Inquiry",
                               command=balance_inquiry)  # Create a button for balance inquiry
    balance_button.pack(pady=5)  # Display the balance inquiry button

    password_button = tk.Button(options_screen, text="Password Change",
                                command=show_password_change_screen)  # Create a button for password change
    password_button.pack(pady=5)  # Display the password change button

    fawry_button = tk.Button(options_screen, text="Fawry Service",
                             command=show_fawry_screen)  # Create a button for Fawry service
    fawry_button.pack(pady=5)  # Display the Fawry service button

    exit_button = tk.Button(options_screen, text="Exit",
                            command=window.destroy)  # Create a button to exit the application
    exit_button.pack(pady=5)  # Display the exit button


def show_withdraw_screen():
    withdraw_screen = tk.Frame(window)  # Create a frame for the withdraw screen
    withdraw_screen.pack(pady=20)  # Set the padding for the frame

    amount_label = tk.Label(withdraw_screen, text="Enter Amount to Withdraw:")  # Create a label for the amount entry
    amount_label.pack()  # Display the amount label
    amount_entry = tk.Entry(withdraw_screen, width=30)  # Create an entry field for the amount
    amount_entry.pack(pady=10)  # Display the amount entry field

    def withdraw():
        amount = int(amount_entry.get())  # Get the entered amount
        withdraw_cash(amount)  # Call the withdraw_cash function

    withdraw_button = tk.Button(withdraw_screen, text="Withdraw", command=withdraw)  # Create a button to withdraw cash
    withdraw_button.pack()  # Display the withdraw button


def show_password_change_screen():
    password_change_screen = tk.Frame(window)  # Create a frame for the password change screen
    password_change_screen.pack(pady=20)  # Set the padding for the frame

    new_password1_label = tk.Label(password_change_screen,
                                   text="Enter New Password:")  # Create a label for the new password entry
    new_password1_label.pack()  # Display the new password label
    new_password1_entry = tk.Entry(password_change_screen, show="*",
                                   width=30)  # Create an entry field for the new password
    new_password1_entry.pack(pady=5)  # Display the new password entry field

    new_password2_label = tk.Label(password_change_screen,
                                   text="Confirm New Password:")  # Create a label for confirming the new password
    new_password2_label.pack()  # Display the confirm new password label
    new_password2_entry = tk.Entry(password_change_screen, show="*",
                                   width=30)  # Create an entry field for confirming the new password
    new_password2_entry.pack(pady=5)  # Display the confirm new password entry field

    def change_password():
        new_password1 = new_password1_entry.get()  # Get the entered new password
        new_password2 = new_password2_entry.get()  # Get the entered confirm new password
        change_password(new_password1, new_password2)  # Call the change_password function

    change_button = tk.Button(password_change_screen, text="Change Password",
                              command=change_password)  # Create a button to change the password
    change_button.pack()  # Display the change password button


def show_fawry_screen():
    fawry_screen = tk.Frame(window)  # Create a frame for the Fawry screen
    fawry_screen.pack(pady=20)  # Set the padding for the frame

    service_label = tk.Label(fawry_screen, text="Select Fawry Service:")  # Create a label for the service selection
    service_label.pack()  # Display the service label

    orange_button = tk.Button(fawry_screen, text="Orange Recharge",
                              command=lambda: recharge_service("Orange"))  # Create a button for Orange recharge
    orange_button.pack(pady=5)  # Display the Orange recharge button

    etisalat_button = tk.Button(fawry_screen, text="Etisalat Recharge",
                                command=lambda: recharge_service("Etisalat"))  # Create a button for Etisalat recharge
    etisalat_button.pack(pady=5)  # Display the Etisalat recharge button

    vodafone_button = tk.Button(fawry_screen, text="Vodafone Recharge",
                                command=lambda: recharge_service("Vodafone"))  # Create a button for Vodafone recharge
    vodafone_button.pack(pady=5)  # Display the Vodafone recharge button

    we_button = tk.Button(fawry_screen, text="We Recharge",
                          command=lambda: recharge_service("We"))  # Create a button for We recharge
    we_button.pack(pady=5)  # Display the We recharge button


# Initial Screen
show_home_screen()  # Display the home screen

# Start the GUI event loop
window.mainloop()  # Start the mainloop of the GUI
