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
    displayed_letters = ["_"] * len(random_word)
    # lower_word = lower.random_word()
    print(" ".join(displayed_letters))
    print(random_word)
    return random_word, displayed_letters
    
def guessed_letter(random_word, displayed_letters, correct_guesses, incorrect_guesses):
    guess = input("\nType a letter that you think is in the word, and then press Enter.\n")
    if guess in random_word:
        for index, letter in list(enumerate(random_word)):
            if letter == guess:
                displayed_letters[index] = letter
        print(f"{' '.join(displayed_letters)} \nGood job!")
    else: 
        incorrect_guesses.append(guess)
        print("Sorry, guess again.")
        print(incorrect_guesses)

def playing_game(word, displayed_letters):
    game_on = True
    correct_guesses = []
    incorrect_guesses = []
    while game_on and len(incorrect_guesses)<8:
        guessed_letter(word, displayed_letters, correct_guesses, incorrect_guesses)
        if "_" not in displayed_letters:
            game_on = False
            print("You won, sucka!!")
    return correct_guesses

print("\nWelcome to the Mystery Word game! This is a game where you will guess the letters to spell a word. Let's start!\n")

word, displayed_letters = get_word(read_file("words.txt"))
playing_game(word, displayed_letters)
