# Function that takes a string and returns a list of cards

from card import *
from set01 import *


def parseDeckList(deckList: str):
    # This function will parse a string of card quantities and names
    # and will add instances of the corresponding cards to the deck.cards
    # The deckList string should have the format "quantity cardName; quantity cardName; ..."
    # An example of a deckList string would be:
    # "2 Ariel - On Human Legs; 1 Ariel - Spectacular Singer; 4 Be Our Guest"
    # The card names should match the names of instances of the card subclasses in the CardsSet01.py file
    # When complete, it should print the number of cards added to the deck and the names of cards which were not found in the CardsSet01.py file

    cardsAdded = []
    cardsNamesNotFound = []

    # Split the single decklist string into a list of strings
    deckListCards = deckList.split(";")

    # Remove leading and trailing whitespace in case the deckList is not formatted correctly
    for card in deckListCards:
        card = card.strip()
        # If the card is empty (likely extra semicolons), skip it
        if not card:
            continue
        cardSplit = card.split(" ")
        try:
            quantity = int(cardSplit[0])
        except ValueError:
            print(f"Error: Invalid quantity format for card '{card}'")
            cardsNamesNotFound.append(card)
            continue
        cardName = " ".join(cardSplit[1:])
        cardFound = False
        for cardTypeClass in Card.__subclasses__():
            for cardClass in cardTypeClass.__subclasses__():
                if cardClass().name == cardName:
                    for i in range(quantity):
                        cardsAdded.append(cardClass())
                    cardFound = True
                    break
        if not cardFound:
            cardsNamesNotFound.append(cardName)

    print(f"{len(cardsAdded)} cards found")
    if cardsNamesNotFound:
        print("The following cards names were not found:")
        for card in cardsNamesNotFound:
            print(card)
    print("\n")

    return cardsAdded

class PlayerDeckedOut(Exception):
    def __init__(self, playerName: str):
        super().__init__(f"{playerName} tryed to draw from an empty deck and lost the game.")
