import random
import sys
from hangman_database import words
from hangman_art import logo
class Hangman():
    def __init__(self):
        self.player_lives = 6
        self.guessed_words = []


    def greet_player(self):
        print(logo)


    def choose_random_word(self):
        possible_words = words 
        word = random.choice(possible_words)
        return word


    def generate_blank_lines(self, word):
        blank_lines = []
        for _ in range(len(word)):
            blank_lines.append("_")
        print(''.join(blank_lines))
        return blank_lines


    def guess_word(self, blank_lines, word):
        guess = input("Guess a letter! ").lower()
        while len(guess) != 1 or guess in self.guessed_words:
            if len(guess) != 1:
                guess = input("You have to guess exactly 1 letter. Please try again: ")
            else:
                print(f"You already guessed the letter {guess}, please try a different one.")
                guess = input("Guess a letter! ").lower()

        self.guessed_words.append(guess)
        guessed_right = False

        for i, letter in enumerate(word):
            if guess == letter:
                blank_lines[i] = letter
                guessed_right = True
        
        if guessed_right:
            print("You guessed a letter!")
            print("".join(blank_lines))
            if "_" not in blank_lines:
                print("You win!")
                sys.exit()
        else:
            self.player_lives -= 1
            print(f"You have lost a life. You have {self.player_lives} lives remaining.")
        

    def main(self):
        self.greet_player()
        word = self.choose_random_word()
        blank_lines = self.generate_blank_lines(word)
        while self.player_lives > 0:
            self.guess_word(blank_lines, word)
        if self.player_lives == 0:
            print(f"Game over\nThe word was {word}")


if __name__ == "__main__":
    hangman = Hangman()
    hangman.main()