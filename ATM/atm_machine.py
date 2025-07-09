'''

Bank -> ATM 

USER:
a. Customer (us)
    1. put atm card in (~ put pin and atm card number ) - Authentication stage
    2. query balance 
    3. deposit amount 
    4. withdraw amount (if any)


b. ATM Operater.
    0. init ATM()
    1. can add cash, with denomination 
    2. retrieve cash 
    3. retrive checq [*]
    4. check log[*]

'''
from bank import Bank

class ATM:
    IS_INIT = False 
    BANK_OBJ = Bank()
    def __init__(self):
        self.machin_id = "1234"
        self.machine_location = "abc road"
        

    def put_atm_card(self, atm_card_id, pin):
        atm_card_details = self.BANK_OBJ.get_account_details(atm_card_id)
        print(type(atm_card_details))

