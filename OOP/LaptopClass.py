class Laptop:
    def __init__(self, brand, size, prise):
        self.brand = brand
        self.size = size
        self.prise = prise

L1 = Laptop("HP", 15.6, 30000)
L2 = Laptop('Dell', 15, 25000)

print(L1.brand, L1.size, L1.prise)
print(L1.brand, L2.size, L2.prise)