
class Ladder:
    def __init__(self,start, end):
        self.ladder_start = start 
        self.ladder_end = end 
    
    def set_ladder_start(self, ladder_start):
        self.ladder_start = ladder_start

    def set_ladder_end(self, ladder_end):
        self.ladder_end = ladder_end 

    def to_dict(self):
        return {"ladder_start" : self.ladder_start,  "ladder_end" : self.ladder_end}


