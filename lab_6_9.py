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
        words = []
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
                    words.append((line_lst[1], value))
        return words


def check_user_words(user_words, language_part, letters, dict_of_words):
    correct_words = []
    missing_words = []
    dict_of_words = dict(dict_of_words)
    for word in user_words:
        correct_condition = True
        if word[0] not in letters:
            correct_condition = False
        if word not in dict_of_words:
            correct_condition = False
        else:
            if dict_of_words[word] != language_part:
                correct_condition = False
        if correct_condition:
            correct_words.append(word)
    for word in dict_of_words:
        if word not in correct_words:
            missing_words.append(word)
    return correct_words, missing_words


def results():
    letters = generate_grid()
    print(letters)
    language_part = random.choice(['noun', 'verb', 'adjective', 'adverb'])
    dict_of_words = get_words('base.lst', letters)
    user_words = input()
    user_words = user_words.split()
    correct_words, missing_words = check_user_words(user_words, language_part, letters, dict_of_words)
    print(correct_words)
    print(missing_words)
