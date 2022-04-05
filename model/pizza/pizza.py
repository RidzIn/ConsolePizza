import csv

from model.item import Item


class Pizza(Item):
    pizza_menu = []

    def __init__(self, name, price, index=Item.count, kind='PIZZA', size='S'):
        super().__init__(
            name, price, kind, index
        )
        self.size = size
        Pizza.pizza_menu.append(self)

    def __repr__(self):
        return f"{self.index} '{self.name}', '{self.size}', '{self.price}'"

    @classmethod
    def showmenu(cls):
        print(f"\t\t\t\t\t\t\t\tPizza's menu")
        for i in Pizza.pizza_menu:
            print(i)

    @classmethod
    def instantiate_from_csv(cls):
        with open('model/pizza/pizza_menu.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for i in items:
            Pizza(
                name=i.get('name'),
                price=float(i.get('price')),
                size=i.get('size'),
            )
