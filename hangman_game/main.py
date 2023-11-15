
class Hangman():

    def __init__(self):
        self.player_lives = 6

    def greet_player(self):
        print("Welcome to Hangman!")

    def main(self):
        self.greet_player()

if __name__ == "__main__":
    hangman = Hangman()
    hangman.main()