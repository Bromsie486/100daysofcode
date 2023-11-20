import random
import os
import sys

from art import main_logo, vs_logo
from database import comparisons


class Higher_Lower_Game():

    def __init__(self) -> None:
        self.player_score = 0


    def check_if_choice_is_right(self, choice, comparison_a, comparison_b):
        if choice.upper() == "A":
            return True if comparison_a["number_of_followers"] > comparison_b["number_of_followers"] else False
        else:
            return True if comparison_b["number_of_followers"] > comparison_a["number_of_followers"] else False
        
    
    def check_if_play_again(self):
        print(main_logo)
        if input("Do you want to play another round? (y/n) ").lower() == "y":
            self.player_score = 0
            self.main()
        else:
            print("Thanks for playing!")
            sys.exit()


    def main(self):
        while True:
            os.system("clear")
            print(main_logo)
            if self.player_score > 0:
                print(f"You're right! Current score: {self.player_score}")
                comparison_a = comparison_b
            else:
                comparison_a = random.choice(comparisons)
            
            comparisons.remove(comparison_a)
            comparison_b = random.choice(comparisons)
            comparisons.append(comparison_a)

            print("Compare A: {} - {}".format(comparison_a["name"], comparison_a["description"]))
            print(vs_logo)
            print("Against B: {} - {}".format(comparison_b["name"], comparison_b["description"]))
            choice = input("Who has more followers on Instagram? Type 'A' or 'B': ")

            if not self.check_if_choice_is_right(choice, comparison_a, comparison_b):
                os.system("clear")
                print(f"Sorry, that's wrong. Final score: {self.player_score}")
                self.check_if_play_again()
            else:  
                self.player_score += 1


if __name__ == "__main__":
    higher_lower_game = Higher_Lower_Game()
    higher_lower_game.main()