import random
class Hangman():

    def __init__(self):
        self.player_lives = 6


    def greet_player(self):
        print("Welcome to Hangman!")


    def choose_random_word(self):
        possible_words = ["mouse", "snake", "zebra"]  
        word = random.choice(possible_words)
        self.correct_choices_to_win = len(word)
        return word


    def generate_blank_lines(self, word):
        blank_lines = []
        for _ in range(len(word)):
            blank_lines.append("_")
        print(''.join(blank_lines))
        return blank_lines


    def guess_word(self, blank_lines, word):
        #ask for input
        guess = input("Guess a letter! ")
        while len(guess) != 1:
            guess = input("You have to guess exactly 1 letter. Please try again: ")

        guessed_right = False

        for i, letter in enumerate(word):
            if guess == letter:
                blank_lines[i] = letter
                guessed_right = True
        
        if guessed_right:
            print("You guessed a letter!")
            print("".join(blank_lines))
            self.correct_choices_to_win -= 1
        else:
            self.player_lives -= 1
            print(f"You have lost a life. You have {self.player_lives} lives remaining.")
        

    def main(self):
        self.greet_player()
        word = self.choose_random_word()
        print(word)
        blank_lines = self.generate_blank_lines(word)
        while self.player_lives > 0 and self.correct_choices_to_win > 0:
            self.guess_word(blank_lines, word)
        if self.player_lives == 0:
            print("Game over")
        else:
            print("You win!")


if __name__ == "__main__":
    hangman = Hangman()
    hangman.main()