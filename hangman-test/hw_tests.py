import pytest, random
from hw_app import Game, validate_input

word_list = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']

# Test utility function
def test_validate_input():
    assert validate_input("a")
    assert validate_input("A")
    assert not validate_input("")
    assert not validate_input("1")

# Test initial Game state
def test_game_instance():
    game = Game()
    assert game.words == word_list
    assert game.miss_counter == 0
    assert game.guessed == []
    assert "".join(game.picked_word) in word_list
    assert len(game.displayed_word) == len(game.picked_word)

# Test if a user guessed a correct letter
def test_game_guess_correct():
    game = Game()
    game.guess(game.picked_word[0])
    assert len(game.guessed) == 1
    assert game.miss_counter == 0
    assert game.guessed[0] in game.displayed_word

# Test if a user did not guess a correct letter
def test_game_guess_wrong():
    game = Game()

    # generate random character not present in our word
    wrong_char = "a"
    while wrong_char in game.picked_word:
        wrong_char = chr(random.randrange(97, 97 + 26))

    game.guess(wrong_char)
    assert len(game.guessed) == 0
    assert game.miss_counter == 1
    assert wrong_char not in game.displayed_word

# Test if a user repeated a letter that had already been guessed and revealed
def test_game_guess_repeated():
    game = Game()
    game.guess(game.picked_word[0])
    game.guess(game.picked_word[0])
    assert len(game.guessed) == 1
    assert game.miss_counter == 0

# Test if a user guessed right and a correct letter was revealed
def test_reveal_letter_if_correct():
    game = Game()
    game.guess(game.picked_word[0])
    # terrible logic, but it works
    assert game.displayed_word.count(" _ ") == len(game.picked_word) - game.picked_word.count(game.picked_word[0])

# Test if a user guessed wrong and nothing was revealed 
def test_reveal_letter_if_incorrect():
    game = Game()
    
    wrong_char = "a"
    while wrong_char in game.picked_word:
        wrong_char = chr(random.randrange(97, 97 + 26))

    game.guess(wrong_char)
    assert game.displayed_word.count(" _ ") == len(game.picked_word)

# Test if a user guessed the same letter and it is in the list of already guessed letters
def test_check_guessed_if_guessed():
    game = Game()
    game.guess(game.picked_word[0])
    assert game.picked_word[0] in game.guessed

# Test if a user did not guess a correct letter and it was not added to the list of already guessed letters
def test_check_guessed_if_missed():
    game = Game()

    wrong_char = "a"
    while wrong_char in game.picked_word:
        wrong_char = chr(random.randrange(97, 97 + 26))

    game.guess(wrong_char)
    assert len(game.guessed) == 0
    
    
