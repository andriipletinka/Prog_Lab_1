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


def get_words(path, letters):
    with open(path, 'r') as vocabulary:
        lines = vocabulary.readlines()
        words = {}
        for line in lines:
            line = line.strip()
            add_condition = True
            if line[0] not in letters:
                add_condition = False
            line_lst = line.split()
            if len(line_lst[0]) > 5:
                add_condition = False
            if add_condition:
                if line_lst[1].startswith('intj') or line_lst[1].startswith('noninfl'):
                    add_condition = False
                elif line_lst[1].startswith('/n') or line_lst[1].startswith('n'):
                    value = 'noun'
                elif line_lst[1].startswith('/v') or line_lst[1].startswith('v'):
                    value = 'verb'
                elif line_lst[1].startswith('/adj') or line_lst[1].startswith('adj'):
                    value = 'adjective'
                elif line_lst[1].startswith('adv'):
                    value = 'adverb'
                if add_condition:
                    words[line_lst[0]] = value
        return words
