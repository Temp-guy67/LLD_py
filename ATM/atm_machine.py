from threading import Lock

from LLD_py.ATM.amtstatefactory import ATMMachineStatesFactory

class ATMManager:
    
    __ATM_INSTANCE = None
    __lock = Lock()
    __initialised = False
    __cur_state =  


    def __new__(cls, *args, **kargs):
        with cls.__lock:
            if cls.__ATM_INSTANCE is None :
                cls.__ATM_INSTANCE = super().__new__(cls)

        return cls.__ATM_INSTANCE


    def __init__(self):
        if not self.__initialised:
            self.__initialised = True 

        
    def set_state(self, state:ATMMachineStatesFactory):
        self.__cur_state = state 

        
