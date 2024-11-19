from services.account_manager import AccountManager
from services.transaction_manager import TransactionManager
from repositories.account_repository import AccountRepository
from exceptions.exceptions import AccountDoesNotExistException
from exceptions.exceptions import AccountAlreadyActiveException
from exceptions.exceptions import AccountAlreadyDeactivatedException

class AccountUI:
    def start(self):
        while True:
            print('\nWelcome to Global Digital Bank')
            print('\nSelect an option')
            print('1. Open Account')
            print('2. Close Account')
            print('3. Withdraw Funds')
            print('4. Deposit Funds')
            print('5. Transfer Funds')
            print('6. Activate account')
            print('7. Deactivate account')
            print('8. Edit account')
            print('9.Exit')

            choice =int(input('Enter your choice: '))
            if choice ==1:
                self.open_account()
            elif choice== 2:
                self.close_account()
            elif choice== 3:
                self.withdraw_funds()
            elif choice== 4:
                self.deposit_funds()
            elif choice== 5:
                self.transfer_funds()
            elif choice== 6:
                self.activate_account()
            elif choice== 7:
                self.deactivate_account()
            elif choice== 8:
                self.edit_account()

            elif choice== 9:
                break
            else:
                print('Invalid choice .Please try again')

    def open_account(self):
        account_type = input('Enter account type (Saving/Current):').strip().lower()
        name=input('Enter your name :')
        amount =float(input('Enter the initial deposit amount :'))
        pin_number = int(input('Enter your pin number :'))
        privilege =input('Enter account privilege (PREMIUM/GOLD/SILVER): ').strip().upper()

        if account_type =='savings':
            date_of_birth = input("Enter your date of birth (YYYY-MM-DD):")
            gender = input("enter your gender (M/F):")
            account =AccountManager().open_account(account_type ,name=name, balance =amount,
            date_of_birth =date_of_birth ,gender=gender ,pin_number =pin_number ,privilege =privilege)

        elif account_type =="current":
            registration_number =input("Enter your registration number :")
            website_url =input("Enter your website URL :")
            account =AccountManager().open_account(account_type ,name=name ,balance=amount,
            registration_number=registration_number ,website_url=website_url ,pin_number=pin_number,privilege=privilege)

        else:
            print("Invalid account type ,Please try again")
            return

        print(account_type.capitalize(),"account opened successfully .Account number :",account.account_number)
    

    def close_account(self):
        account_number = int(input("Enter the account number :"))
        account = next((acc for acc in AccountRepository.account if acc.account_number==account_number),None)

        if account:
            try:
                AccountManager().close_account(account)
                print("Account closed succesfully")
            except Exception as e:
                print("Error :",e)
        else:
            print("account not found, Plese try again")
                


    def withdraw_funds(self):
        account_number = int(input("Enter the account number :"))
        amount =float(input("Enter amount to withdraw :"))
        pin_number = int(input("Enter pin number :"))
        account = next ((acc for acc in AccountRepository.account if acc.account_number==account_number),None)

        if account:
            try:
                AccountManager().withdraw(account,amount,pin_number)
                print("Account withdrawn succesfully")
            except Exception as e:
                print("Error :",e)
        else:
            print("account not found, Plese try again")

    def deposit_funds(self):
        account_number = int(input("Enter the account number :"))
        amount =float(input("Enter amount to deposit :"))
        account = next ((acc for acc in AccountRepository.account if acc.account_number==account_number),None)
        
        if account:
            try:
                AccountManager().deposit(account,amount)
                print("Account deposited succesfully")
            except Exception as e:
                print("Error :",e)
        else:
            print("account not found, Plese try again")
        
    def transfer_funds(self):
        from_account_number =int(input("Enter from account number :"))
        to_account_number = int(input("Enter reciers account number :"))
        amount = float(input("Enter the amount to be transferred :"))
        pin_number = int(input("Enter pin number :"))
        from_account = next ((acc for acc in AccountRepository.account if acc.account_number==from_account_number),None)
        to_account = next ((acc for acc in AccountRepository.account if acc.account_number==to_account_number),None)

        if from_account and to_account:
            try:
                AccountManager().transfer(from_account,to_account,amount,pin_number)
                print("Account diposited succesfully")
            except Exception as e:
                print("Error :",e)
        else:
            print("account not found, Plese try again")
    
    
    def activate_account(self):
        try:
            account_number = int(input("Enter the account number :"))
            account = next((acc for acc in AccountRepository.account if acc.account_number==account_number),None)
            if account is None:
                raise AccountDoesNotExistException('Account does not exist')
            AccountManager().activate_account(account)
        except AccountDoesNotExistException as e:
            print("Error :",e)
        except AccountAlreadyActiveException as e:
            print("Error :",e)


    def deactivate_account(self):
        try:
            account_number = int(input("Enter the account number :"))
            account = next((acc for acc in AccountRepository.account if acc.account_number==account_number),None)
            if account is None:
                raise AccountDoesNotExistException('Account does not exist')
            AccountManager().deactivate_account(account)
        except AccountDoesNotExistException as e:
            print("Error :",e)
        except AccountAlreadyDeactivatedException as e:
            print("Error :",e)


    def edit_account(self):
        try:
            account_number = int(input("Enter the account number :"))
            existing_pin=int(input("Enter the pin number :"))
            account = next((acc for acc in AccountRepository.account if acc.account_number==account_number),None)
            if not account:
                raise AccountDoesNotExistException('Account does not exist')
            AccountManager().validate_pin(account, existing_pin)
            AccountManager().edit_account(account)

        except Exception as e:
            print("Error :",e)
