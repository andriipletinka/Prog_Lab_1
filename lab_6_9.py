import random

def generate_grid():
    """
    Generate a list of 5 unique letters of ukrainian alphabet.
    >>> print(generate_grid())
    ['р', 'ю', 'й', 'і', 'ш']
    """
    alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    letters = []
    while len(letters) < 5:
        letter = random.choice(alphabet)
        if letter not in letters:
            letters.append(letter)
    return letters
