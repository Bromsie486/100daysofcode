import random
import os

from art import main_logo, vs_logo
from database import comparisons


class Higher_Lower_Game():

    def __init__(self) -> None:
        self.player_score = 0


    def main(self):
        while True:
            os.system("clear")
            print(main_logo)

            comparison_a = random.choice(comparisons)
            comparisons.remove(comparison_a)
            comparison_b = random.choice(comparisons)
            comparisons.append(comparison_a)

            print("Compare A: {} - {}".format(comparison_a["name"], comparison_a["description"]))
            print(vs_logo)
            print("Against B: {} - {}".format(comparison_b["name"], comparison_b["description"]))
            break


if __name__ == "__main__":
    higher_lower_game = Higher_Lower_Game()
    higher_lower_game.main()