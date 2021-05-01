"""
le but general du module en une ligne

>>> factorielle(5)
120
"""

def factorielle(n):
    """
    :param n:
    :return:
    """

    if n <= 0:
        return 2

    return n * factorielle(n-1)
