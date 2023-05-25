"""
Unit tests for Product class.
"""
import pytest

from products import Product


def test_creating_product():
    """
    Test that creating a normal product works.
    """
    assert Product('MacBook Pro', 2500.0, 100)


def test_creating_product_with_empty_name():
    """
    Test that creating a product
    with empty name
    invokes an exception.
    """
    with pytest.raises(ValueError):
        assert Product("", 100.0, 2)


def test_creating_product_with_negative_price():
    """
    Test that creating a product
    with negative price
    invokes an exception.
    """
    with pytest.raises(ValueError):
        assert Product("MacBook Pro", -100.0, 2)


def test_creating_product_negative_quantity():
    """
    Test that creating a product
    with negative quantity
    invokes an exception.
    """
    with pytest.raises(ValueError):
        assert Product("MacBook Pro", 100.0, -2)


def test_product_becomes_inactive():
    """
    Test that when a product reaches 0 quantity,
    it becomes inactive.
    """
    product = Product("MacBook Pro", 100.0, 10)
    product.buy(10)
    assert not product.is_active()


def test_buy_modifies_quantity():
    """
    Test that product purchase modifies the quantity.
    """
    product = Product("MacBook Pro", 100.0, 10)
    product.buy(2)
    assert product.get_quantity() == 8


def test_buy_return_total_price():
    """
    Test that product purchase returns the right output.
    """
    product = Product("MacBook Pro", 100.0, 10)
    assert product.buy(2) == 200.0


def test_buy_over_stock():
    """
    Test that buying a larger quantity than exists invokes exception.
    """
    product = Product("MacBook Pro", 100.0, 10)
    with pytest.raises(ValueError):
        assert product.buy(50)
