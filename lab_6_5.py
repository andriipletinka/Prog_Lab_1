from typing import List
from string import ascii_uppercase
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    grid = []
    i = 0
    while i<3:
        row = []
        j = 0
        while j<3:
            row.append(random.choice(ascii_uppercase))
            j += 1
        grid.append(row)
        i += 1
    return grid


def get_words(path: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(path, 'r') as file:
        vocabulary = [i.strip() for i in file.readlines()]
        words_lst = []
        for word in vocabulary:
            word = word.lower()
            word_letters = [i for i in word]
            if len(word) >= 4 and letters[4] in word:
                match_rules = True
            else:
                match_rules = False
            for letter in word_letters:
                if word_letters.count(letter) > letters.count(letter):
                    match_rules = False
            if match_rules:
                if word not in words_lst:
                    words_lst.append(word)
        return words_lst


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    pass


def get_pure_user_words(user_words, letters, words_from_dict):
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
