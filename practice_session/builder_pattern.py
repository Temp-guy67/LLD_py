class Burger:

    class BurgerBulder:
        onion = False
        garlic_bread = False
        sauce = False 
        mayonese = False

        def add_sauce(self):
            self.sauce = True

        def add_garlic_bread(self):
            self.garlic_bread = True

        def add_onion(self):
            self.onion = True

        def add_mayonese(self):
            self.mayonese = True

        def build(self):
            return Burger(self)
        
    def __init__(self, bb : BurgerBulder):
        