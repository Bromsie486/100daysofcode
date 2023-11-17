
class Blackjack_Game():

    def main(self):
        deck = []
        deck = self.load_deck(deck)
        print(deck)
        #while input("Do you want to play a round of Blackjack? (y/n) ") != "n":


    def load_deck(self, deck):
        type_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for i in range(32):
            for card_type in type_of_cards:
                deck.append(card_type)
        return deck




if __name__ == "__main__":
    blackjack = Blackjack_Game()
    blackjack.main()

