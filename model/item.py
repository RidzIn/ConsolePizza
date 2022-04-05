

class Item:
    all = []
    count = 1

    def __init__(self, name, price, kind, index):
        assert price >= 0, f"Price {price} can not be less then zero"

        self.index = Item.count
        self.name = name
        self.price = price
        self.kind = kind

        Item.all.append(self)
        Item.count += 1

    def __repr__(self):
        return f"{self.index}Item('{self.name}', '{self.price}', '{self.kind}')"




