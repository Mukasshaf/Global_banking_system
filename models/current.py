from models.account import Account

class Current(Account):
    def __init__(self,name,balance,privilege,website_url,pin_number,registration_number):
        super().__init__(name,balance,pin_number,privilege)
        self.website_url=website_url
        self.registration_number=registration_number