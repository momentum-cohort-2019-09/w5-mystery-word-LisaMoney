import random

def read_file(filename):
    with open(filename) as words:
        text = words.read()
        return make_list_from_text(text)

def make_list_from_text(words):
    list_of_words = words.split()
    return list_of_words
    
def get_word(word_list):
    random_word = random.choice(word_list)
    word_length = (("_ ") * len(random_word))
    print(word_length)
    return random_word
    
def guessed_letter():
    correct_guesses = []
    incorrect_guesses = []
    request = input("\nPlease enter one letter that you think is in the word, and then press Enter.\n")
    if request in word(get_word):
        correct_guesses.append(request)
        print("Awesome!  Guess again!")
    else: 
        incorrect_guesses.append(request)
        print("Sorry, try again.")

def playing_game(word):
    gameon = True
    while gameon and len(incorrect_guesses)<8:
        check_correct_guesses(word, correct_guesses, incorrect_guesses)
    print(correct_guesses)
    return correct_guesses

print("\nWelcome to the Mystery Word game. This is a game where you will guess the letters to spell a word. Let's start!\n")

get_word(read_file("words.txt"))
guessed_letter()
playing_game()

# return input where you ask it 
# var = function(input)
#     and then the response to the input is that var