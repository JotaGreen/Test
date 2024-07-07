# This is a Command Line Card Game

from enum import Enum
import random
import uuid


class CardType(Enum):
    CHARACTER = "Character"
    LOCATION = "Location"
    ACTION = "Action"
    SONG = "Song"
    ITEM = "Item"


class CardColor(Enum):
    AMBER = "Amber"
    AMETHYST = "Amethyst"
    EMERALD = "Emerald"
    RUBY = "Ruby"
    SAPPHIRE = "Sapphire"
    STEEL = "Steel"


class Card:
    def __init__(
        self, name: str, card_type: CardType, color: CardColor, cost: int, inkable: bool
    ):
        self.name = name
        self.card_type = card_type
        self.color = color
        self.cost = cost
        self.inkable = inkable
        self.id = str(uuid.uuid4())

    def __str__(self):
        return f"{self.name}, id: {self.id}"

    def onPlay(self):
        print(f"{self.name} was played.")


class CharacterClassification(Enum):
    STORYBORN = "Storyborn"
    DREAMBORN = "Dreamborn"
    FLOODBORN = "Floodborn"
    ALIEN = "Alien"
    ALLY ="Ally"
    BROOM = "Broom"
    CAPTAIN = "Captain"
    DEITY = "Deity"
    DETECTIVE = "Detective"
    DRAGON = "Dragon"
    FAIRY = "Fairy"
    HERO = "Hero"
    HYENA = "Hyena"
    INVENTOR = "Inventor"
    KING = "King"
    KNIGHT = "Knight"
    MADRIGAL = "Madrigal"
    MENTOR = "Mentor"
    MUSKETEER = "Musketeer"
    PIRATE = "Pirate"
    PRINCE = "Prince"
    PRINCESS = "Princess"
    PUPPY = "Puppy"
    QUEEN = "Queen"
    SEVENDWARFS = "Seven Dwarfs"
    SORCERER = "Sorcerer"
    TIGGER = "Tigger"
    TITAN = "Titan"
    VILLAIN = "Villain"


class Character(Card):
    def __init__(
        self,
        name: str,
        color: CardColor,
        cost: int,
        inkable: bool,
        baseName: str,
        version: str,
        classifications: list[CharacterClassification],
        strength: int,
        willpower: int,
        lore: int,
        abilities: str,
        dry: bool = False,
        exterted: bool = False,
        damageCounters: int = 0,
    ):
        super().__init__(name, CardType.CHARACTER, color, cost, inkable)
        self.baseName = baseName
        self.version = version
        self.classifications = classifications
        self.strength = strength
        self.willpower = willpower
        self.lore = lore
        self.abilities = abilities
        self.dry = dry
        self.exterted = exterted
        self.damageCounters = damageCounters


class Location(Card):
    def __init__(
        self,
        name: str,
        color: CardColor,
        cost: int,
        inkable: bool,
        baseName: str,
        version: str,
        willpower: int,
        lore: int,
        moveCost: int,
        abilities: str,
        damageCounters: int = 0,
    ):
        super().__init__(name, CardType.LOCATION, color, cost, inkable)
        self.baseName = baseName
        self.version = version
        self.willpower = willpower
        self.lore = lore
        self.moveCost = moveCost
        self.abilities = abilities
        self.damageCounters = damageCounters


class Action(Card):
    def __init__(
        self,
        name: str,
        color: CardColor,
        cost: int,
        inkable: bool,
        abilities: str,
    ):
        super().__init__(name, CardType.ACTION, color, cost, inkable)
        self.abilities = abilities


class Song(Card):
    def __init__(
        self,
        name: str,
        color: CardColor,
        cost: int,
        inkable: bool,
        abilities: str,
    ):
        super().__init__(name, CardType.SONG, color, cost, inkable)
        self.abilities = abilities


class Item(Card):
    def __init__(
        self,
        name: str,
        color: CardColor,
        cost: int,
        inkable: bool,
        abilities: str,
        exerted: bool = False,
    ):
        super().__init__(name, CardType.ITEM, color, cost, inkable)
        self.abilities = abilities
        self.exerted = exerted


class Deck:
    def __init__(self, player: str, cards: list[Card]):
        self.player = player
        self.cards = cards

    def __str__(self):
        return f"{self.player}'s deck"

    def parseDeckList(self, deckList: str):
        #This function will parse a multiline string of card quantities and names and will add instances of the corresponding cards to the deck.cards
        #An example of a deckList string would be:
        # 2 Ariel - On Human Legs
        # 1 Ariel - Spectacular Singer
        # 4 Be Our Guest
        # The card names should match the names of instances of the card subclasses in the CardsSet01.py file
        # When complete, it should print the number of cards added to the deck and the names of cards which were not found in the CardsSet01.py file
        deckList = deckList.split("\n") #Split the multiline string into a list of strings 
        cardsNotFound = []
        cardsAdded = 0
        for card in deckList:
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
        print(f"{cardsAdded} cards added to the deck.")
        if cardsNotFound:
            print("The following cards were not found:")
            for card in cardsNotFound:
                print(card)

    def shuffle(self):
        self.cards = random.shuffle(self.cards)

    def getTop(self, num: int = 1):
        return self.cards[:num]
