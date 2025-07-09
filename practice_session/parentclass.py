
class ParentClass:
    def __init__(self):
        self._test = 5 

    
    def get_test(self):
        return self.__test 
    

class Child(ParentClass):
    def __init__(self):
        super().__init__()

obj = ParentClass()
# res = obj.get_test()
child_obj = Child()
res = child_obj._test

print(res)