"""
In this program you can list products and make an order.
"""
from typing import Tuple, List

from products import Product
from store import Store


def get_menu_option() -> str:
    """
    Returns user input menu option as a string
    :return: user input menu option (str)
    """
    return input("""
    Store Menu
    ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number: """)


def get_order(best_buy: Store) -> str:
    """
    Returns the total payment of order statement
    :param best_buy: Store
    :return: total payment of order statement (str)
    """
    shopping_list = get_shopping_list(best_buy)
    try:
        if shopping_list:
            return f"********\n" \
                   f"Order made! Total payment: ${best_buy.order(shopping_list)}"
    except ValueError as err:
        print(err)
    return ''


def start(best_buy: Store) -> str:
    """
    Get the store object as a parameter,
    and will show the user the store menu
    """
    store_menu = {
        "1": best_buy.show_all_products,
        "2": lambda: f"Total of {best_buy.get_total_quantity()} items in store",
        "3": lambda: get_order(best_buy),
    }

    menu_choice = ''
    while menu_choice != '4':
        menu_choice = get_menu_option()
        if menu_choice not in store_menu:
            continue

        print(store_menu[menu_choice]())


def user_input_product_quantity() -> Tuple[str, str]:
    """
    Returns the product_option and order_quantity
    :return: product_option, order_quantity (Tuple[str, str])
    """
    product_option = input("Which product # do you want? ")
    order_quantity = input("What amount do you want? ")

    return product_option, order_quantity


def get_shopping_list(best_buy: Store) -> List[Tuple[Product, int]]:
    """
    Get a list of shopping list
    of products and order quantities
    from user input.
    :param best_buy: Store
    :return: shopping_list (List[Tuple[Product, int]])
    """
    shopping_list = []
    print(best_buy.show_all_products())
    print("When you want to finish order, enter empty text.")

    while True:
        product_option, order_quantity = user_input_product_quantity()

        if product_option == '' and order_quantity == '':
            break
        try:
            if not product_option.isdigit() or not order_quantity.isdigit():
                raise ValueError()

            option = int(product_option)
            quantity = int(order_quantity)

            if option <= 0 or quantity <= 0 or \
                    option > len(best_buy.get_all_products()):
                raise ValueError()

            order_product = best_buy.get_all_products()[option - 1]

            shopping_list.append((order_product, quantity))
            print("Product added to list!\n")
        except ValueError:
            print("Error adding product!\n")
        continue

    return shopping_list


def main():
    """
    The main program that creates a store object from a list of products,
    and making orders from user input products information.
    """
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
