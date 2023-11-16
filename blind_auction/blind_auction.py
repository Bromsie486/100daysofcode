import os 

class Blind_Auction():

    def __init__(self) -> None:
        self.bidders = []


    def get_user_input(self):
        want_to_quit = ""
        while want_to_quit != "n":
            name = input("What's your name? ")
            bid = input("How much do you want to bid? ")
            self.bidders.append({"name": name, "bid": bid})
            want_to_quit = input("Are there any more bidders? (y/n) ")
            os.system('clear')
    

    def select_winner(self):
        winner = self.bidders[0]
        for bidder in self.bidders:
            if bidder["bid"] > winner["bid"]:
                winner = bidder
        print("The winner is {}".format(winner["name"]))



    def main(self):
        self.get_user_input()
        self.select_winner()
        

if __name__ == "__main__":
    blind_auction = Blind_Auction()
    blind_auction.main()