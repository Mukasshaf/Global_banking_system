
from repositories.account_repository import AccountRepository

class Account:
    def __init__(self,name,balance,pin_number,privilege):
        self.account_number =AccountRepository.generate_account_number()
        self.name=name
        self.pin_number=pin_number
        self.privilege=privilege
        self.balance=balance
        self.is_active=True
        self.closed_date=None