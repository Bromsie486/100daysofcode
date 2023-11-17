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
        self.number_of_player_aces = 0
        self.number_of_computer_aces = 0


    def main(self):
        self.load_deck()
        while input("Do you want to play a game of Blackjack?(y/n) ").lower() != "n":
            #generate player and computer hand
            os.system("clear")
            player_hand = self.generate_hand("player")
            print(f"This is your hand: {player_hand[0]}, {player_hand[1]}")
            computer_hand = self.generate_hand("computer")
            print(f"This is the computer's hand: {computer_hand[0]}, ?")

            #user can ask for as many cards as he wants before reaching 21
            try:
                while input("Do you want another card? (y/n) ").lower() != "n":
                    os.system("clear")
                    player_hand.append(self.generate_hand("player", 1)[0])
                    output_text = self.generate_output(player_hand)
                    print(f"This is your new hand: {output_text}")
                    print(f"This is the computer's hand: {computer_hand[0]}, ?")
                    if self.player_hand_value > 21:
                        print("You lost, you went over 21. Game over!")
                        self.reset_variables_to_default()
                        raise Exception("Game Over")
                
                #computer drawing until above 16
                if self.computer_hand_value < 16:
                    while self.computer_hand_value < 16:
                        computer_hand.append(self.generate_hand("computer", 1)[0])
                        if self.computer_hand_value > 21:
                            output_text_for_computer = self.generate_output(computer_hand)
                            print(f"This is the computer's final hand: {output_text_for_computer}")
                            print("You win, the computer went over 21!")
                            self.reset_variables_to_default()
                            raise Exception("Game won")
                    self.determine_final_result()
                      
                else:

            except:
                continue
    
    
    def determine_final_result(self, player_hand, computer_hand):
        #calculate final score for computer
        if self.number_of_computer_aces > 0:
            if self.computer_hand_value + 10 > 21:
                final_computer_result = self.computer_hand_value
            else:
                final_computer_result = self.computer_hand_value + 10
        else:
            final_computer_result = self.computer_hand_value
        
        #calculate final score for player
        if self.number_of_player_aces > 0:
            if self.player_hand_value + 10 > 21:
                final_player_result = self.player_hand_value
            else:
                final_player_result = self.player_hand_value + 10
        else:
            final_player_result = self.player_hand_value
        

        #calculate result
        output_text_for_player = self.generate_output(player_hand)
        output_text_for_computer = self.generate_output(computer_hand)
        print(f"This is the player's final hand: {output_text_for_player}")
        print(f"This is the computer's final hand: {output_text_for_computer}")
        print(f"Final player score: {final_player_result}")
        print(f"Final computer score: {final_computer_result}")
        if final_computer_result > final_player_result:
            print("You have lost.")
        elif final_player_result == final_computer_result:
            print("This is a draw!")
        else:
            print("You have won!")



    
    def reset_variables_to_default(self):
        self.player_hand_value = 0
        self.computer_hand_value = 0
        self.number_of_player_aces = 0
        self.number_of_computer_aces = 0


    def generate_hand(self, hand_owner, amount_to_generate = 2):
        generated_cards = []
        for _ in range(amount_to_generate):
            card = random.choice(self.deck)
            self.deck.pop(self.deck.index(card))
            generated_cards.append(card)
            if card != "A":
                if hand_owner == "player":
                    self.player_hand_value += self.value_table[card]
                else:
                    self.computer_hand_value += self.value_table[card]
            else: 
                if hand_owner == "player":
                    self.number_of_player_aces += 1
                    self.player_hand_value += 1
                else:
                    self.number_of_computer_aces += 1
                    self.computer_hand_value += 1
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