from .dice import Dice

class Player:
    dice = Dice()
    def __init__(self, id, name):
        self.id = id
        self.name = name 

    def get_name(self):
        return self.name 
    
    def get_id(self):
        return self.id 
    
    def roll_dice(self):
        return self.dice.roll_dice()
    
    def to_dict(self):
        return {"name" : self.name , "id" : self.id}
    

