#Aim: WAP to simulate an ATM machine. create the following functions and then use it to show the working of the program.
#Coder: Zain Mohamed Saeed Kazi

passwords = {
    "zain" : {"password":"zain","balance": 2000},
    "shibu" : {"password":"shibu","balance": 8000}
}

def authenticate(pin):
    if pin == passwords[username]['password']:
        return True
    else:
        return"""Wrong Password!!
        Try again"""

def check_balance():
    print(f"Your current balance is {passwords[username]['balance']}")

def deposit(amount):
    passwords[username]['balance'] = amount + passwords[username]['balance']

def withdraw(amount):
    passwords[username]['balance'] = passwords[username]['balance'] - amount

print("****ATM Machine****\n")
username = input("Please enter username:").strip().lower()

print(f"Hello {username}")
password = input("Please input your password:").strip().lower()

if authenticate(password) == True:
    while True:
        print("""\n\t\t***Menu***
            1.Check Balance
            2.Deposit Amount
            3.Withdraw Cash
            4.Exit""")
    
        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()
            
        if choice == 2:
            deposit_amount = int(input("Enter the amount to be deposited: "))
            
            deposit(deposit_amount)

            print(f"The new balance is {passwords[username]['balance']}")
            break

        if choice == 3:
            withdraw_amount = int(input("Enter the amount to be withdrawn: "))

            if withdraw_amount > passwords[username]['balance']:
                print("The balance is too low.")

            else:
                withdraw(withdraw_amount)
                print(f"The new balance is {passwords[username]['balance']}")

        if choice == 4:
            break

    print("Thank you for using the ATM.")
    exit()
else:
    print("Wrong password")
