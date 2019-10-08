import random

# intro = input("Welcome to the Mystery Word game.  This is a game where you will guess the letters to guess a word.  Are you ready to play?")

# def get_length(sorted_word):
#     word_length = len(random_word)
#     print(word_length)
#     return word_length

def get_word(word_list):
    random_word = random.choice(word_list)
    word_length = len(random_word)
    print(word_length)
    print(random_word)
    return random_word
    
def make_list_from_text(words):
    list_of_words = words.split()
    return list_of_words

def read_file(filename):
    with open(filename) as words:
        text = words.read()
        return make_list_from_text(text)

# get_length(read_file(sorted_word))

get_word(read_file("words.txt"))

#with open("words.txt") as words: for word of words pass