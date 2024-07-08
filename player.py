from card import *
from set01 import *

class Deck:
    def __init__(self, playerName: str):
        self.cards = []
        self.playerName = playerName

    def __str__(self):
        return f"{self.playerName}'s deck with {len(self.cards)} cards"

    def parseDeckList(self, deckList: str):
        # This function will parse a string of card quantities and names
        # and will add instances of the corresponding cards to the deck.cards
        # The deckList string should have the format "quantity cardName; quantity cardName; ..."
        # An example of a deckList string would be:
        # "2 Ariel - On Human Legs; 1 Ariel - Spectacular Singer; 4 Be Our Guest"
        # The card names should match the names of instances of the card subclasses in the CardsSet01.py file
        # When complete, it should print the number of cards added to the deck and the names of cards which were not found in the CardsSet01.py file
        deckListCards = deckList.split(";")  # Split the single decklist string into a list of strings
        # Remove leading and trailing whitespace from each string in the list
        cardsNotFound = []
        cardsAdded = 0
        for card in deckListCards:
            card = card.strip() # Remove leading and trailing whitespace in case the deckList is not formatted correctly
            #If the card is empty (likely extra semicolons), skip it
            if not card:
                continue
            card = card.split(" ")
            quantity = int(card[0])
            cardName = " ".join(card[1:])
            cardFound = False
            for cardTypeClass in Card.__subclasses__():
                for cardClass in cardTypeClass.__subclasses__():
                    if cardClass().name == cardName:
                        for i in range(quantity):
                            self.cards.append(cardClass())
                            cardsAdded += 1
                        cardFound = True
                        break
            if not cardFound:
                cardsNotFound.append(cardName)
        print(f"{cardsAdded} cards added to {self.playerName}'s deck.")
        if cardsNotFound:
            print("The following cards were not found:")
            for card in cardsNotFound:
                print(card)
        print("\n")

    def shuffle(self):
        random.shuffle(self.cards)
        print(f"Shuffled {self.playerName}'s deck.")

    # Deck.getTop will return the top card(s) of the deck and remove them from the deck
    # if asked to get more cards than are in the deck, it will print an error message and return all the cards in the deck
    def getTop(self, num: int = 1, print: bool = True):
        if num > len(self.cards):
            print(
                f"{self.playerName} attempted to get {num} cards from the deck, but it only has {len(self.cards)}."
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


# Create a function called printListOfCards which takes a list of cards as input and prints the name of each card
# separated by semicolons and one space "; "
def printListOfCards(cards: list[Card]):
    cardNames = []
    for card in cards:
        cardNames.append(card.name)
    print("; ".join(cardNames))


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

    # This function will draw a number of cards from the player's deck and add them to the player's hand
    # If the player tries to draw more cards than are in the deck, it will print an message and terminate the game
    def draw(self, num: int = 1):
        if len(self.deck) < num:
            print(
                f"{self.name} tried to draw {num} cards, but the deck only has {len(self.deck)} cards."
            )
            print(f"{self.name} lost the game.")
        else:
            self.hand += self.deck.getTop(num, print=False)
            print(f"{self.name} drew {num} cards.")
