menu = {
    "Bottle": 60,
    "Burger": 80,
    "Coffee": 40,
    "Pizza": 100,
    "Salad": 70,
}


def find_menu_item(user_input):
    user_input = user_input.strip()
    for item in menu:
        if item.casefold() == user_input.casefold():
            return item
    return None


print("========== WELCOME TO MY RESTURANT ==========")
print("========== BOOK YOUR ORDER FROM MENU ==========")
for item, price in menu.items():
    print(f"{item} : RS {price}")

order_book = 0
ordered_items = []

while True:
    item_name = input("What do you want to order? ").strip()
    matched_item = find_menu_item(item_name)

    if matched_item is not None:
        order_book += menu[matched_item]
        ordered_items.append(matched_item)
        print(f"Your order is {matched_item} added successfully")
    else:
        print(f"{item_name} is not found in menu")

    another_order = input("Do you want another order? (Yes/No): ").strip().casefold()
    if another_order not in ("yes", "y"):
        break

print(f"Your total bill is {order_book}")
if ordered_items:
    print("Items ordered:", ", ".join(ordered_items))
