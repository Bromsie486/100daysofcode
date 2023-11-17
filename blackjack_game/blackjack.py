import random
import os

class Blackjack_Game():

    def main(self):
        value_table = {
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
        deck = []
        deck = self.load_deck(deck)
        while input("Do you want to play a round of Blackjack? (y/n) ") != "n":
            os.system("clear")
            player_hand = self.generate_hand(deck)
            print(f"Your hand: {player_hand[0]}, {player_hand[1]}")
            computer_hand, computer_hand_value = self.generate_computer_hand(deck, value_table)
            print(f"Computer hand: {computer_hand[0]}, ?")
            if input("Do you want another card? (y/n) ").lower() == "y":
                player_hand.append(self.generate_hand(deck, 1)[0])
                output_string = ""
                for i in range(len(player_hand)):
                    output_string += player_hand[i]
                    if i != len(player_hand)-1:
                        output_string += ", "
                print(f"Your new hand: {output_string}")
                    

    def load_deck(self, deck):
        type_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for i in range(32):
            for card_type in type_of_cards:
                deck.append(card_type)
        return deck


    def generate_hand(self, deck, amount_to_generate = 2):
        generated_cards = []
        for i in range(amount_to_generate):
            card = random.choice(deck)
            deck.pop(deck.index(card))
            generated_cards.append(card)
        return generated_cards
    

    def generate_computer_hand(self, deck, value_table):
        generated_cards = []
        hand_value = 0
        while hand_value <= 16:
            card = random.choice(deck)
            deck.pop(deck.index(card))
            generated_cards.append(card)
            if card != "A":
                hand_value += value_table[card]
            else:
                if hand_value + 11 > 21:
                    hand_value += 11
                else:
                    hand_value += 1
        return generated_cards, hand_value


if __name__ == "__main__":
    blackjack = Blackjack_Game()
    blackjack.main()



#todo
#handle when the deck runs out of cards