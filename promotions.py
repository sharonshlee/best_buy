"""
Promotion Abstract Class with subclasses:
SecondHalfPrice Class
ThirdOneFree Class
PercentDiscount Class
"""

from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    An interface Promotion class.
    Promotions are applied on a single product only.
    """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        This is an abstract method to be inherited by its subclasses
        that gets 2 parameters - a product instance and a quantity,
        and returns the discounted price after promotion was applied.
        :param product: Product
        :param quantity: int
        :return: discounted price (float)
        """


class SecondHalfPrice(Promotion):
    """
    Second item at half price.
    """

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Apply second item at half price promotion
        :param product: Product
        :param quantity: int
        :return: discounted price (float)
        """
        if quantity > 1:
            return product.price / 2
        return 0


class ThirdOneFree(Promotion):
    """
    Buy 2, get 1 free.
    """

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Apply buy 2 get 1 free promotion.
        :param product: Product
        :param quantity: int
        :return: discounted price (float)
        """
        if quantity > 2:
            return product.price
        return 0


class PercentDiscount(Promotion):
    """
    Percentage discount (i.e. 20% off).
    """

    def __init__(self, name: str, percent: int):
        super().__init__(name)
        self._percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Apply a percentage discount promotion.
        :param product: Product
        :param quantity: int
        :return: discounted price (float)
        """
        return product.price * quantity * self._percent / 100
