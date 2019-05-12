CardValue = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
         
class Card:

    def __init__(self, displayName):
        self.name = displayName

    def value(self):
        return CardValue[self.name]

    def __str__(self):
        return self.name


if __name__ == "__main__":
    card = Card("Two")
    print(str(card))