# ATM Machine program with account balances
pins = {'Mazen': {'pin': '1234', 'balance': 10000},
        'Z3bola': {'pin': '5678', 'balance': 20000},
        'Zaabola': {'pin': '9988', 'balance': 5000}}
transactions = []  # list of transactions

# function to validate PIN and return account balance
def validate_pin(name, pin):
    if name in pins and pins[name]['pin'] == pin:
        return True, pins[name]['balance']
    else:
        return False, 0

# function to withdraw money
def withdraw(name, amount):
    if amount <= pins[name]['balance']:
        pins[name]['balance'] -= amount
        transactions.append((name, 'withdraw', amount))
        return True
    else:
        return False

# function to deposit money
def deposit(name, amount):
    pins[name]['balance'] += amount
    transactions.append((name, 'deposit', amount))

# main program
while 1:
    name = input('Enter your name: ')
    pin = input('Enter your PIN: ')
    valid, balance = validate_pin(name, pin)
    if valid:
        print('Welcome,', name)
        while True:
            print('1. Withdraw')
            print('2. Deposit')
            print('3. Check balance')
            print('4. Exit')
            choice = input('Enter your choice (1-4): ')
            if choice == '1':
                amount = int(input('Enter amount to withdraw: '))
                if withdraw(name, amount):
                    print('Withdrawal successful. New balance is', pins[name]['balance'])
                else:
                    print('Withdrawal failed. Insufficient funds.')
            elif choice == '2':
                amount = int(input('Enter amount to deposit: '))
                deposit(name, amount)
                print('Deposit successful. New balance is', pins[name]['balance'])
            elif choice == '3':
                print('Your balance is', pins[name]['balance'])
            elif choice == '4':
                print('Thank you for using our ATM. Goodbye!')
                break
            else:
                print('Invalid choice. Please try again.')
        break
    else:
        print('Invalid name or PIN. Please try again.')
