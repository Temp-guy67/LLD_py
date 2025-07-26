

from abc import ABC,abstractmethod 
from enum import Enum 

class TransactionType(Enum):
    GET_BALANCE_ENQUIRY = 1
    DEPOSIT_CASH = 2
    WITHDRAW_CASH = 3



class Transactions(ABC):
    @abstractmethod
    def process(self):
        pass 

    def get_type(self):
        pass




class DepositeCash(Transactions):

    def process(self):
        pass 



class WithdrawCash(Transactions):


    def process(self):
        pass 



class checkBalance(Transactions):
    def process(self):
        pass 