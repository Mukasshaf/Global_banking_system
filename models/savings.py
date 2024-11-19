from models.account import Account

class Savings(Account):
    def __init__(self,name,balance,privilege,date_of_birth,gender,pin_number):
        super().__init__(name,balance,pin_number,privilege)
        self.date_of_birth=date_of_birth
        self.gender=gender