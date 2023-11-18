import random
import os
import sys

from art import logo

class Number_Guessing_Game():

    def greet(self):
        os.system("clear")
        print(logo)
        print("Welcome to the Number guessing game!")
        print("I'm thinking of a number between 1 and 100")
        difficulty = input("Would you like to play on easy or hard? ").lower()
        return difficulty
    

    def should_play_another_round(self):
        should_continue = input("Would you like to play another round? (y/n) ").lower()
        if should_continue == "y":
            self.main()
        else:
            print("Okay, see you soon!")
            sys.exit()


    def generate_number(self):
        return random.randint(0,101)
    

    def check_if_player_is_out_of_lives(self):
        if self.player_lives == 0:
            return True
        return False
    

    def main(self):
        difficulty = self.greet()
        
        if difficulty == "easy":
            self.player_lives = 10
        else:
            self.player_lives = 5

        number = self.generate_number()
        guess = int(input("Guess a number: ").replace(" ",""))
        while True:
            if guess == number:
                print("You have guessed the number! You win!")
                self.should_play_another_round()
                break
            else:
                self.player_lives -= 1
                if self.check_if_player_is_out_of_lives():
                    print(f"You are out of lives. The number was {number}")
                    self.should_play_another_round()
                if guess > number:
                    guess = int(input(f"Lower! Remaning lives: {self.player_lives}\n Guess again! ").replace(" ",""))
                else:
                    guess = int(input(f"Higher! Remaning lives: {self.player_lives}\n Guess again! ").replace(" ",""))
                

if __name__ == "__main__":
    number_guessing_game = Number_Guessing_Game()
    number_guessing_game.main()