import csv

from model.item import Item


class Drink(Item):
    drink_menu = []

    def __init__(self, name, price, index=Item.count, kind='DRINK', size='0.5L', ):
        super().__init__(
            name, price, kind, index
        )
        self.size = size

        Drink.drink_menu.append(self)

    def __repr__(self):
        return f"{self.index} '{self.name}', '{self.size}', '{self.price}'"

    @classmethod
    def showmenu(cls):
        print(f"\t\t\t\t\t\t\t\tDrinks Menu")
        for i in Drink.drink_menu:
            print(i)

    @classmethod
    def instantiate_from_csv(cls):
        with open('model/drink/drink_menu.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for i in items:
            Drink(
                name=i.get('name'),
                price=float(i.get('price')),
            )
