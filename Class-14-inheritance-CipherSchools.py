def __init__(self, brand,model_name, price):
    self.brand = brand
    self.model_name = model_name
    self._price = max(price,0)

def full_name(self):
    return f"{self.brand} {self.model_name}"

def make_a_call(self,number):
    return f"calling{number}...."

class Smartphone():
     def__init__(self, brand, model_name, price, ram, internet_memory, rear_camera):

        self.brand = brand
        self.model_name = model_name
        self.price = max(price,0)
        self.ram = ram
        self.internet_memory = internet_memory
        self.rear_camera = rear_camera

     def full_name(self):
         return f"{self.brand} {self.model_name}"

     def make_a_call(self,number):
         return f"calling {number}....."
     

