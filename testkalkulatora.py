import pytest
from kalkulator import add_numbers, is_even, celsius_to_fahrenheit, factorial, is_prime

def test_add_numbers():
    assert add_numbers(3, 5) == 8
    assert add_numbers(3, -5) == -2
    assert add_numbers(-3, -5) == -8
    assert add_numbers(0, 5) == 5

def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(7) is False

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-10) == 14
    assert celsius_to_fahrenheit(1000) == 1832

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(4) is False
    assert is_prime(0) is False
    assert is_prime(104729) is True
