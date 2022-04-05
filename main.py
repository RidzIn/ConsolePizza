"""
This is my first console project written in Python. In there I will try to
practice the basics of Python and using GIT.
"""
from model.drink.drink import Drink
from model.item import Item
from model.pizza.pizza import Pizza


def show_menu():
    Pizza.showmenu()
    Drink.showmenu()


Pizza.instantiate_from_csv()
Drink.instantiate_from_csv()

order = []
print("\t\t\tWelcome to my console application called: 'Ridz Pizza'")
while True:
    x = input('''
Press the number:
    1. If you want to get whole menu
    2. If you want to get only drink menu
    3. If you want to get only pizza's menu
    0. If you want to exit the application
    
''')
    if x == '0':
        break
    elif x == '1':
        show_menu()
        break
    elif x == '2':
        Drink.showmenu()
        break
    elif x == '3':
        Pizza.showmenu()
        break
    else:
        print("Please input the number {0,1,2,3}")

print('''
(You can see the number at the start of each item. 
Write there numbers to add position to your order.
''')


while True:
    answer = input("Print 'exit' to finish your order: ")
    if answer == 'exit':
        break
    answer = int(answer)
    if answer < 0 or answer > Item.count:
        print("The number which you pressed is invalid")

    order.append(Item.all[answer-1])


print(f"Your order is:")
for i in order:
    print(i)






