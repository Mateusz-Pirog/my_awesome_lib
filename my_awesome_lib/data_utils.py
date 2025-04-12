# my_awesome_lib/data_utils.py

"""
Moduł narzędziowy do operacji na danych.
"""


def flatten(nested_list):
    """
    Spłaszcza listę zagnieżdżoną.

    Args:
        nested_list (list): Lista mogąca zawierać listy.

    Returns:
        list: Spłaszczona lista.
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk_list(data, chunk_size):
    """
    Dzieli listę na mniejsze fragmenty.

    Args:
        data (list): Lista wejściowa.
        chunk_size (int): Rozmiar fragmentu.

    Returns:
        list: Lista fragmentów.
    """
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
