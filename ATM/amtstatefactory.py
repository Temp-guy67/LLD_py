
from abc import ABC, abstractmethod
from LLD_py.ATM.atm_machine import ATMManager
from transactions.transactions import Transactions


class ATMMachineStatesFactory(ABC):
    @abstractmethod
    def insertCard(self):
        pass 

    @abstractmethod
    def verifyCard(self):
        pass 

    @abstractmethod
    def ejectCard(self):
        pass 

    @abstractmethod
    def transaction(self, trans : Transactions): # type: ignore
        pass 

    

class IdleState(ATMMachineStatesFactory):
    __atm = None
    def __init__(self, atm : ATMManager):
        self.__atm = atm

    def insertCard(self):
        print("Insert Your Card ") 
        self.__atm.set_state(HasCardState()) 

    def verifyCard(self):
        pass 

    def ejectCard(self):
        pass 

    def transaction(self, trans : Transactions):
        pass 



class HasCardState(ATMMachineStatesFactory):
    __atm = None
    def __init__(self, atm : ATMManager):
        self.__atm = atm

    def insertCard(self):
        pass

    def verifyCard(self):
        print("Enter Your Pin : ")  
        self.__atm.set_state(OperationState()) 

    def ejectCard(self):
        pass

    def transaction(self, trans : Transactions):
        pass 


class OperationState(ATMMachineStatesFactory):
    __atm = None
    def __init__(self, atm : ATMManager):
        self.__atm = atm
        
    def insertCard(self):
        pass

    def verifyCard(self):
        pass 

    def ejectCard(self):
        pass 

    def transaction(self, trans : Transactions):
        if trans.

        print("Transaction started " , trans)  


class DispenseState(ATMMachineStatesFactory):
    __atm = None
    def __init__(self, atm : ATMManager):
        self.__atm = atm


    def insertCard(self):
        print("Insert Your Card") 

    def verifyCard(self):
        pass 

    def ejectCard(self):
        pass 

    def transaction(self, trans : Transactions):
        pass 

    def dispense(self):
        pass


class InsufficientCashState(ATMMachineStatesFactory):
    __atm = None
    def __init__(self, atm : ATMManager):
        self.__atm = atm


    def insertCard(self):
        pass 

    def verifyCard(self):
        pass 

    def ejectCard(self):
        print("Insufficient Cash in the Machine, Ejecting your card")  

    def transaction(self, trans : Transactions):
        pass
