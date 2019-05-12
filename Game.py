from Card import Card
from Deck import Deck
from Player import Player

class Game:
    def __init__(self, initialChips):
        self.player = Player(initialChips)
        self.dealer = Player(0)
        self.deck = Deck()
        self.deck.shuffle()

    def Start(self):
        print("Game Start! Deal card!")
        cardToDeal = self.deck.nextCard()
        self.dealer.Hit(cardToDeal)
        print(f"Dealer hit card {str(cardToDeal)}")
        cardToDeal = self.deck.nextCard()
        self.dealer.Hit(cardToDeal)

        cardToDeal = self.deck.nextCard()
        self.player.Hit(cardToDeal)
        print(f"player hit card {str(cardToDeal)}")
        cardToDeal = self.deck.nextCard()
        self.player.Hit(cardToDeal)
        print(f"player hit card {str(cardToDeal)}")

        while input("Do you want to hit? (Y/N)") == 'Y':
            cardToDeal = self.deck.nextCard()
            print(f"You got card {str(cardToDeal)}")
            self.player.Hit(cardToDeal)

            if (self.player.CalculateCardValue() > 21):
                print("U lose U dumb ass!")
                quit()

        while(self.dealer.CalculateCardValue() < 17):
            cardToDeal = self.deck.nextCard()
            self.dealer.Hit(cardToDeal)

            if (self.dealer.CalculateCardValue() > 21):
                print("U win U dumb ass!")
                quit()
        
        if (self.player.CalculateCardValue() > self.dealer.CalculateCardValue()):
            print('U win! YEEEEE!')
            print(f'Dealer Cards: ')
            self.dealer.ShowCard()
        else:
            print('U lose!')
            print(f'Dealer Cards: ')
            self.dealer.ShowCard()

if __name__ == "__main__":
    game = Game(100)
    game.Start()