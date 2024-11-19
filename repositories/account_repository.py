class AccountRepository:
    account=[]
    account_counter = 1000


    #method to generate a new acc no.
    @classmethod
    # classmethod can access and midify the class level attributes 
    # changes made by one intance will be reflected in all
    def generate_account_number(cls):
        # classmethod takes cls as first arguments 
        # regular def (method) takes self as first arguments
        cls.account_counter+=1
        return cls.account_counter

    @classmethod
    def save_account(cls,account):
        cls.account.append(account)

    # get all acc
    def get_all_account(self):
        return self.account