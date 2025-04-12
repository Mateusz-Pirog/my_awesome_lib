# my_awesome_lib/math_tools.py

"""
Moduł z funkcjami matematycznymi.
"""


def factorial(n):
    """
    Oblicza silnię liczby.

    Args:
        n (int): Liczba nieujemna.

    Returns:
        int: Silnia n.
    """
    if n < 0:
        raise ValueError("Liczba musi być nieujemna")
    return 1 if n == 0 else n * factorial(n - 1)


def is_prime(n):
    """
    Sprawdza, czy liczba jest pierwsza.

    Args:
        n (int): Liczba całkowita.

    Returns:
        bool: True jeśli pierwsza, False w przeciwnym wypadku.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
