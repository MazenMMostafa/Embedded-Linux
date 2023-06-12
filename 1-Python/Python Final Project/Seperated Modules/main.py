import tkinter as tk
from tkinter import messagebox
from account_validation import validate_account, validate_password
from transaction import withdraw_cash, balance_inquiry, change_password, recharge_service
from screens import show_home_screen, show_password_screen, show_options_screen, show_withdraw_screen, show_password_change_screen, show_fawry_screen

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

# Initial Screen
show_home_screen()  # Display the home screen

# Start the GUI event loop
window.mainloop()  # Start the mainloop of the GUI
