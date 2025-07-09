class Snake:
    def __init__(self,start, end):
        self.snake_start = start 
        self.snake_end = end 
    
    def set_snake_start(self, snake_start):
        self.snake_start = snake_start

    def set_snake_end(self, snake_end):
        self.snake_end = snake_end 

    def to_dict(self):
        return {"snake_start" : self.snake_start,  "snake_end" : self.snake_end}
