from enum import Enum

class Size(Enum):
    SMALL =1 
    MEDIUM = 2
    LARGE = 3

class Locker():
    def __init__(self, size : Size) :
        self.id = 