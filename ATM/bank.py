
class Bank:
    # atm machine 
    atm_machine_map = {}
    customer_account_details_map = {"ac_12345" : {"name" : "ABC", "amount" : 12000}}
    atm_card_vs_account_map = {12345 : {"acc_id" : "ac_12345", "validity" : 2025, "hashed_pin" : "fake_pin" }}
    def __init__(self):
        pass 

    def get_account_details(self, atm_card_number:int):
        if self.atm_card_vs_account_map.get(atm_card_number):
            return self.atm_card_vs_account_map.get(atm_card_number)

        else:
            raise Exception("Not a valid ATM card")


            