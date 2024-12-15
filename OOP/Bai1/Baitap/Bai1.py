class Manufacturer:
    def __init__(self, identity: int, location: str):
        self.iden = identity
        self.location = location 
        
    def describe(self):
        print("identity:", self.iden, "- Location:", self.location)
        
class Device:
    def __init__(self, name: str, price: int, identity: int, location: str):
        self.name = name
        self.price = price 
        self.manufacturer = Manufacturer(identity, location) #tao doi tuong ke thua
        
    def describe(self):
        print("Name:", self.name, "price:", self.price)
        self.manufacturer.describe()
        
#dau vao
device1 = Device(name = "mouse", price = 2, identity = 9725, location = "VietNam" )
device1.describe()
