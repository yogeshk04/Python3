class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + ' ' + model

    def descount(self, num):
        disc_price = (num/100)*self.price

        return self.price - disc_price

Lap1 = Laptop("HP", "QC1", 35000)

print(Lap1.descount(50))