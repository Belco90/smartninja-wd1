print "Welcome to the best restaurant in the city"

menu = {}
more = True
new_dish = 'yes'

while more:
    if new_dish == 'yes':
        name = raw_input("Enter the name of the dish: ")
        price = raw_input("Enter the price for {}: ".format(name))

        menu[name] = price

    new_dish = raw_input("Enter new dish? (yes/no) ").lower()

    more = new_dish != 'no'

print "Menu: {}".format(menu)

print "Saving menu into menu.txt file"

with open("menu.txt", "w+") as menu_file:
    menu_file.write("MENU\n")
    for dish_name in menu:
        dish_price = menu[dish_name]
        menu_file.write("{}: {} EUR\n".format(dish_name, dish_price))

print "Menu saved into menu.txt file. See you!"
