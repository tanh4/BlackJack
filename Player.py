from Card import Card

class Player:
    def __init__(self, initialChip):
        self.chip = initialChip
        self.bet = 0
        self.cards = []

    def CalculateCardValue(self):

        totalValue = 0
        hasAce = False

        for card in self.cards:
            if card.name == 'Ace':
                hasAce = True
                continue
            totalValue += card.value()
        
        if totalValue > 10 and hasAce:
            return totalValue + 1
        else:
            return totalValue + 11

    def Hit(self, card):
        self.cards.append(card)

    def ShowCard(self):
        for card in self.cards:
            print(f"{card.name}")

if __name__ == "__main__":
    player = Player(100)
    player.Hit(Card("Two"))
    player.Hit(Card("Three"))
    player.ShowCard()