from shop_items import shop_items


# ---------------------------------- Backend --------------------------------- #


# --------------------------------- Frontend --------------------------------- #
def add_item_to_cart():
    print("\nYou are in the add to Cart Menu")
    print("\nMenu")
    for id, item in shop_items.items():
        print(f"{id}) {item['name']} - {item['price']}")


def remove_cart_item():
    print("remove item")


def view_cart():
    print("viewing cart")


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
