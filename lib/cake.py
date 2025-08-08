class Cake():
    def __init__(self):
        self.flavour = ""
        self.size = 100
    
    def set_flavour(self, flavour):
        self.flavour = flavour
    
    def take_slice(self, slice):
        self.size -= slice
        print(f"You have taken a {slice} sized slice. \n There is {self.size} percent cake remaining.")