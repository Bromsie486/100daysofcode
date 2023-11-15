import random
class Hangman():

    def __init__(self):
        self.player_lives = 6


    def greet_player(self):
        print("Welcome to Hangman!")


    def choose_random_word(self):
        possible_words = ["mouse", "snake", "zebra"]
        return random.choice(possible_words)


    def main(self):
        self.greet_player()
        print(self.choose_random_word())


if __name__ == "__main__":
    hangman = Hangman()
    hangman.main()