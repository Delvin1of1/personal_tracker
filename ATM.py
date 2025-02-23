#Welcome message
print("---Welcome to the Lavender ATM---")

#Class for the Electronic Wallet
class ElectronicWallet:
    def __init__(self):   
        self.account_pin = 1234
        self.balance = 1000000
        self.transaction_history = []
        
    def authenticate(self):
        attempts = 3
        while attempts > 0:
            pin = int(input("Enter your 4-digit pin: "))
            if pin == self.account_pin:
                print("Pin Authenticated")
                return True
            else:
                attempts -= 1
                print(f"Incorrect pin. {attempts} attempts remaining.")
        print("Too many incorrect attempts.Exiting....Goodbye!")
        return False


#Function to display the menu
    def display_menu(self):
        print("\n---Menu---")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Show Transaction History")
        print("5. Exit")

    #Function to check balance
    def check_balance(self):    
        print(f"Your balance is: {self.balance}")  

#Function to withdraw money
    def withdraw(self):
        self.balance
        amount = int(input("\nEnter amount to withdraw: "))
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"You withdrew: {amount}")
                print(f"Transaction successful! Your new balance is: {self.balance}") 
            else:
                print("Insufficient balance")
        else:
            print("Invalid amount. Please enter an amount greater than 0")

#Function to deposit money
    def deposit(self):
        self.balance
        amount = int(input("\nEnter deposit amount: "))
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"You deposited: {amount}")
            print(f"Transaction successful! Your new balance is: {self.balance}")  
        else:
            print("Invalid amount. Please enter an amount greater than 0")

#Function to view transaction history
    def view_transaction_history(self):
        if self.transaction_history:
            print("\n---Transaction History---")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet") 

#Main ATM Function
    def atm(self):
        if not self.authenticate():
            return #Early exit if authentication fails at the beginning
    
        while True:
            self.display_menu()
            option = int(input("\nEnter option: "))
            if option == 1:
                self.check_balance()
            elif option == 2:
                self.withdraw()
            elif option == 3:
                self.deposit()
            elif option == 4:
                self.view_transaction_history()
            elif option == 5:
                print("Exiting...Goodbye!")
                break
            else:
                print("\nInvalid option. Please try again")

#Calling Main
if __name__ == "__main__":
    # ElectronicWallet()         
    wallet = ElectronicWallet() 
    wallet.atm()  
