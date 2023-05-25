"""
Store class that hold all products,
and will allow the user to make a purchase
of multiple products at once.
"""
from typing import List, Tuple

from products import Product


class Store:
    """
    The Store class will contain one variable -
    a list of products that exist in the store.
    """

    def __init__(self, products: List[Product]):
        """
        Initiator method that hold all the products.
        :param products: List[Product]
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Add a product to store
        :param product: Product
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from store.
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns how many items are in the store in total.
        :return: quantity (int)
        """
        return sum(product.quantity
                   for product in self.products)

    def get_all_products(self) -> List[Product]:
        """
        Returns all products in the store that are active.
        :return: active products
        """
        return [product
                for product in self.products
                if product.active]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        :param shopping_list: List[Tuple[Product, int]]
        :return: total order price
        """
        return sum(product.buy(quantity)
                   for product, quantity
                   in shopping_list)

    def show_all_products(self) -> str:
        """
        Return a formatted string of active products.
        """
        return "------\n" + \
               "\n".join([f'{i+1}. {product.show()}'
                          for i, product in enumerate(self.get_all_products())]) + \
               "\n------"
