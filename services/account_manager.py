from models.savings import Savings
from models.current import Current
from repositories.account_repository import AccountRepository
from exceptions.exceptions import AccountNotActiveException
from exceptions.exceptions import InsufficientFundsException
from exceptions.exceptions import InvalidPinException
from exceptions.exceptions import TransferLimitExceededException
from services.transaction_manager import TransactionManager
from services.account_privilege_manager import AccountPrivilegemanger
from exceptions.exceptions import AccountAlreadyActiveException
from exceptions.exceptions import AccountAlreadyDeactivatedException

class AccountManager:
    def open_account(self,account_type,**kwargs):
        if account_type== 'savings':
            new_account=Savings(**kwargs)
        elif account_type== 'current':
            new_account=Current(**kwargs)
        else:
            raise ValueError('Invalid account type')

        AccountRepository.save_account(new_account)
        return new_account
    
    def check_account_active(self,account):
        if not account.is_active:
            raise AccountNotActiveException('Account is not Active')
    
    def validate_pin(self,account,pin_number):
        if account.pin_number != pin_number:
            raise InvalidPinException('Invalid Pin')

    def withdraw(self,account,amount,pin_number):
        self.check_account_active(account)
        self.validate_pin(account,pin_number)
        if account.balance< amount:
            raise InsufficientFundsException('Insuffiecient funds')

        account.balance -= amount
        TransactionManager.log_transaction(account.account_number,amount,'withdraw')  

    def deposit(self,account,amount):
        self.check_account_active(account)

        account.balance +=amount
        TransactionManager.log_transaction(account.account_number,amount,'deposit')

    def transfer(self,from_account,to_account,amount,pin_number):
        self.check_account_active(from_account)
        self.check_account_active(to_account)
        self.validate_pin(from_account,pin_number)

        if from_account.balance <amount:
            raise InsufficientFundsException("Insufficient funds")

        limit = AccountPrivilegemanger.get_transfer_limit(from_account.privilege)
        if amount > limit:
            raise TransferLimitExceededException('Transfer limit exceeded')

        from_account.balance -= amount
        to_account.balance +=amount
        TransactionManager.log_transaction(from_account.account_number,amount,'transfer',to_account.account_number)

    def close_account(self,account):
        if not account.is_active:
            raise AccountNotActiveException('Account is already deactivated')
        else:
            account.is_active = False
            
    def activate_account(self,account):
        if account.is_active:
            raise AccountAlreadyActiveException('Account is already activated')
        else:
            account.is_active = True
            print("Account activated succesfully")


    def deactivate_account(self,account):
        if (account.is_active == False):
            raise AccountAlreadyDeactivatedException('Account is already deactivated')
        else:
            account.is_active = False
            print("Account deactivated succesfully")


    def edit_account(self,account):
        self.check_account_active(account)
        new_name = input("Enter the new name :")
        new_pin = int ( input("Enter the new PIN :"))

        account.name=new_name
        account.pin_number=new_pin
        print("Account details updated successfully")