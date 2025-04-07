def add_numbers(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def factorial(n):
    if n < 0:
        raise ValueError("liczba nie moze byc ujemna")
    elif n == 0 or n == 1:
        return 1
    else:
        wynik = 1
        for i in range(2, n + 1):
            wynik *= i
        return wynik

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
