class car:
    #constructor
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def displayMSG(self):
        print(f"Car is {self.make} and {self.model}")

#inherit

class Mercedes(car):
    def __init__(self,color,price,make,model):
        self.color = color
        self.price = price
        super().__init__(make,model)

    def displayMSG(self):
        super().displayMSG()
        print(f"Car is {self.color}")
        print(f"car price is {self.price}")

carObj = Mercedes("Blue", "25,000", "mercedes", "XYZ")
carObj.displayMSG()


     