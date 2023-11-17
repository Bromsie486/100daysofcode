import random

class Blackjack_Game():

    def main(self):
        deck = []
        deck = self.load_deck(deck)
        while input("Do you want to play a round of Blackjack? (y/n) ") != "n":
            generated_cards = self.generate_hand(deck)
            print(f"Your hand: {generated_cards[0]}, {generated_cards[1]}")
            print(f"Cards remaining in the deck: {len(deck)}")


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


if __name__ == "__main__":
    blackjack = Blackjack_Game()
    blackjack.main()



#todo
#handle when the deck runs out of cards