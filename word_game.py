import random

def info_for_user():
    intro = input("Welcome to the Mystery Word game.  This is a game where you will guess the letters to guess a word.  Are you ready to play?")
    print(info_for_user)
    return info_for_user
    
def get_word(word_list):
    random_word = random.choice(word_list)
    word_length = (len(random_word) * ("_ "))
    print(word_length)
    return random_word

def guessing_letter():
    pass
    
def make_list_from_text(words):
    list_of_words = words.split()
    return list_of_words

def read_file(filename):
    with open(filename) as words:
        text = words.read()
        return make_list_from_text(text)

get_word(read_file("words.txt"))
info_for_user()
