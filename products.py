"""
The Products class represents has a
Product class and its methods.
"""


class Product:
    """
    The Product class encapsulates information
    about its name and price.
    It includes an attribute to keep track of
    the total quantity and purchase amount of
    the product.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity),
        raises an exception.
        :param name: str
        :param price: float
        :param quantity: int
        """
        if not name:
            raise ValueError(f'{name} cannot be empty.')
        if price < 0:
            raise ValueError(f'{price} cannot be negative.')
        if quantity < 0:
            raise ValueError(f'{quantity} cannot be negative.')

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Getter function for quantity.
        :return: quantity (int)
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Setter function for quantity.
        If quantity reaches 0, deactivates the product.
        """
        self.quantity += quantity

        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """
        Getter function for active.
        :return: True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self):
        """
        :return: a string that represents the product
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        :param quantity: int
        :return: the total price (float) of the purchase.
        """
        if quantity > self.quantity:
            raise ValueError("Error while making order! Quantity larger than what exists")

        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return self.price * quantity
