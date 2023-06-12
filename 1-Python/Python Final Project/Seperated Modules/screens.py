import tkinter as tk
from tkinter import messagebox
from transaction import withdraw_cash, balance_inquiry, change_password, recharge_service

# Global variables
current_screen = None

def return_to_home():
    global current_account
    current_account = None  # Reset the current account
    password_attempts = 0  # Reset the password attempts counter
    show_home_screen()  # Display the home screen

    # Add code to display the home screen

def show_password_screen():
    global current_screen
    clear_screen()
    current_screen = "password"
    # Add code to display the password entry screen

def show_options_screen():
    global current_screen
    clear_screen()
    current_screen = "options"
    # Add code to display the options screen

def show_withdraw_screen():
    global current_screen
    clear_screen()
    current_screen = "withdraw"
    # Add code to display the withdrawal screen

def show_password_change_screen():
    global current_screen
    clear_screen()
    current_screen = "password_change"
    # Add code to display the password change screen

def show_fawry_screen():
    global current_screen
    clear_screen()
    current_screen = "fawry"
    # Add code to display the Fawry service screen

def clear_screen():
    global current_screen
    if current_screen is not None:
        # Add code to clear the current screen

def return_to_home():
    global current_screen
    clear_screen()
    current_screen = "home"
    # Add code to return to the home screen
