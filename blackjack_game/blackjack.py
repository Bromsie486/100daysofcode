import random
import os

class Blackjack_Game():

    def __init__(self):
        self.value_table = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
        }
        self.deck = []
        self.player_hand_value = 0
        self.computer_hand_value = 0


    def main(self):
        self.load_deck()
        while input("Do you want to play a game of Blackjack?(y/n) ").lower() != "n":
            player_hand = self.generate_player_hand()
            print(f"This is your hand: {player_hand[0]}, {player_hand[1]}")
            while input("Do you want another card? (y/n) ").lower() != "n":
                player_hand.append(self.generate_player_hand(1)[0])
                output_text = self.generate_output(player_hand)
                print(f"This is your new hand: {output_text}")


    def generate_player_hand(self, amount_to_generate = 2):
        generated_cards = []
        for i in range(amount_to_generate):
            card = random.choice(self.deck)
            self.deck.pop(self.deck.index(card))
            generated_cards.append(card)
        return generated_cards


    def load_deck(self):
        type_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for i in range(32):
            for card_type in type_of_cards:
                self.deck.append(card_type)


    def generate_output(self, player_hand):
        output_text = ""
        for i in range(len(player_hand)):
            output_text += player_hand[i]
            if i != len(player_hand)-1:
                output_text += ", "
        return output_text


if __name__ == "__main__":
    blackjack = Blackjack_Game()
    blackjack.main()



#todo
#handle when the deck runs out of cards