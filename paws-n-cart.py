from shop_items import shop_items

from tabulate import tabulate

# ---------------------------------- CONSTANTS --------------------------------- #
TABULATE_HEADER_OPTION = "firstrow"

# ---------------------------------- Backend --------------------------------- #
cart = {
    "items": [],
    "total": 0,
}


def _add_to_cart(item):
    cart["total"] += item["price"]
    cart["items"].append(item)
    return cart


# --------------------------------- Frontend --------------------------------- #
def add_item_to_cart():
    print("\nYou are in the add to Cart Menu")
    print("\nMenu")
    for id, item in shop_items.items():
        print(f"{id}) {item['name']} - {item['price']}")

    while True:
        user_option = input("Please select the item you'd like to add to cart:\n")
        if user_option in shop_items.keys():
            _add_to_cart(shop_items[user_option])
            view_cart()

        else:
            print("please choose a valid option")


def remove_cart_item():
    print("remove item")


def view_cart():
    cart_data = {}
    cart_table = [["item", "count", "unit price", "subtotal"]]
    cart_total = round(cart["total"], 2)

    # Combine common items and show count
    for item in cart["items"]:
        if item["id"] not in cart_data:
            cart_data[item["id"]] = {**item, "count": 1}
        else:
            cart_data[item["id"]]["count"] += 1

    # Only show name, unit price and total price
    for id, item in cart_data.items():
        item_subtotal = item["count"] * item["price"]
        cart_table.append([item["name"], item["count"], item["price"], item_subtotal])

    # Printing result
    print("\n  Current Cart")
    print(tabulate(cart_table, headers=TABULATE_HEADER_OPTION))
    print(f"Cart Total: {cart_total} - total items: {len(cart['items'])}")
    print("\n")


site_functions = {
    "1": {"name": "Add Item to Cart", "function": add_item_to_cart},
    "2": {"name": "Remove Item From Cart", "function": remove_cart_item},
    "3": {"name": "View Cart", "function": view_cart},
}


def main():
    # 1 - add item to cart
    # 2 - remove item from cart
    # 3 - view cart
    print("Welcome to the Pet store")
    for key, value in site_functions.items():
        print(f"{key}) {value['name']}")

    while True:
        print("\n")
        user_option = input("Please select what you want to do from the options: ")
        if user_option in list(site_functions.keys()):
            site_functions[user_option]["function"]()


main()
