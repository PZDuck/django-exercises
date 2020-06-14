import random


# Validate whether the input is a string or not
def validate_input(letter):
    if not isinstance(letter, str) or letter.isdigit() or letter == "":
        return False
    return True

# Class for a game instance
class Game():
    def __init__(self):
        self.words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
        self.miss_counter = 0
        self.guessed = []
        self.pick_word()
    
    def pick_word(self):
        self.picked_word = list(random.choice(self.words))
        self.displayed_word = [" _ " for i in range(len(self.picked_word))]
    
    def guess(self, letter):
        if self.check_guessed(letter):
            return None

        if letter.lower() in self.picked_word:    
            self.guessed.append(letter)
            self.reveal_letter(letter)
            return True
        else:
            self.miss_counter += 1
            return False
        
    
    def reveal_letter(self, letter):
        for i in range(len(self.picked_word)):
            if self.picked_word[i] == letter:
                self.displayed_word[i] = letter
    
    def check_guessed(self, letter):
        return True if letter in self.guessed else False


if __name__ == '__main__':
    game = Game()
    print("Guess a word.")
    print(f"{game.displayed_word}")
    
    while True:  
        if " _ " not in game.displayed_word:
            print("You won! Fuck you.")
            quit()

        if game.miss_counter > 4:
            print(f"You lost! The word was: {''.join(game.picked_word)}")
            quit()
                
        user_guess = input("Guess a letter: ")
        
        if not validate_input(user_guess):
            print("Please, provide a valid input.")
            continue
        
        if  game.guess(user_guess) == None:
            print("You have already guessed this letter. Try another one.")
            continue


        print("".join(game.displayed_word))
