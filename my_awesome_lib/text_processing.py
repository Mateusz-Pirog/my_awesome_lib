# my_awesome_lib/text_processing.py

"""
Moduł do przetwarzania tekstu.
"""


def count_words(text):
    """
    Liczy słowa w tekście.

    Args:
        text (str): Tekst wejściowy.

    Returns:
        int: Liczba słów.
    """
    return len(text.split())


def remove_punctuation(text):
    """
    Usuwa znaki interpunkcyjne z tekstu.

    Args:
        text (str): Tekst wejściowy.

    Returns:
        str: Tekst bez interpunkcji.
    """
    import string
    return text.translate(str.maketrans("", "", string.punctuation))
