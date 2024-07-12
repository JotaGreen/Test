import random
from card import Card
from helperfunctions import PlayerDeckedOut

class Deck:
    def __init__(self, playerName: str):
        self.cards = []
        self.playerName = playerName

    def __str__(self):
        return f"{self.playerName}'s deck with {len(self.cards)} cards"

    def shuffle(self):
        random.shuffle(self.cards)
        print(f"Shuffled {self.playerName}'s deck.")

    # Deck.getTop will return the top card(s) of the deck and remove them from the deck
    # if asked to get more cards than are in the deck, it will print an error message and return all the cards in the deck
    def getTop(self, num: int = 1, print: bool = True):
        if num > len(self.cards):
            print(
                f"{self.playerName} attempted to get {num} cards from the deck, but it only has {len(self.cards)}.\n"
                f"{self.playerName} got all cards in the deck."
            )
            return self.cards
        topCards = self.cards[:num]
        self.cards = self.cards[num:]
        if print:
            print(f"{self.playerName} got {num} cards from the top of the deck.")
        return topCards

    def placeOnTop(self, cards: list[Card]):
        self.cards = cards + self.cards
        print(f"{self.playerName} placed {len(cards)} cards on the top of the deck.")

    def placeOnBottom(self, cards: list[Card]):
        self.cards = self.cards + cards
        print(f"{self.playerName} placed {len(cards)} cards on the bottom of the deck.")

    # Deck.len returns the number of cards in the deck
    def __len__(self):
        return len(self.cards)

class Player:
    def __init__(self, name: str):
        self.name = name
        self.deckList = str
        self.deck = Deck(playerName=name)
        self.hand = []
        self.playZone = []
        self.inkwell = 0
        self.discard = []
        self.lore = 0
        self.inkExerted = 0

    # When checking for equality in players, only the name is checked
    def __eq__(self, other):
        return self.name == other.name

    # When printing a player, only the name is printed
    def __str__(self):
        return self.name

    # This function will draw a card from the top of a player's deck and add it to the player's hand
    # If the player tries to draw from an empty deck, it will raise an exception
    def draw(self):
        if len(self.deck) == 0:
            raise PlayerDeckedOut(self.name)
        else:
            self.hand += self.deck.getTop(print=False)
            print(f"{self.name} drew a card.")

