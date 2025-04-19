# This is a Command Line Card Game
# Test

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

    def onPlay(self):
        print(f"{self.name} was played.")

    def onPlayerTurnStart(self):
        pass

    def onPlayerTurnEnd(self):
        pass

    def onThisTurnEnd(self):
        pass


class CharacterClassification(Enum):
    STORYBORN = "Storyborn"
    DREAMBORN = "Dreamborn"
    FLOODBORN = "Floodborn"
    ALIEN = "Alien"
    ALLY = "Ally"
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

    @property
    def shortened(self):
        match self.value:
            case "Storyborn":
                return "Storyb"
            case "Dreamborn":
                return "Dreamb"
            case "Floodborn":
                return "Floodb"
            case "Alien":
                return "Alien"
            case "Ally":
                return "Ally"
            case "Broom":
                return "Broom"
            case "Captain":
                return "Cptn"
            case "Deity":
                return "Deity"
            case "Detective":
                return "Dtctv"
            case "Dragon":
                return "Dragon"
            case "Fairy":
                return "Fairy"
            case "Hero":
                return "Hero"
            case "Hyena":
                return "Hyena"
            case "Inventor":
                return "Invt"
            case "King":
                return "King"
            case "Knight":
                return "Knght"
            case "Madrigal":
                return "Mdrgl"
            case "Mentor":
                return "Mentor"
            case "Musketeer":
                return "Msktr"
            case "Pirate":
                return "Pirat"
            case "Prince":
                return "Prnc"
            case "Princess":
                return "Prncs"
            case "Puppy":
                return "Puppy"
            case "Queen":
                return "Queen"
            case "Seven Dwarfs":
                return "7Dwfs"
            case "Sorcerer":
                return "Sorcr"
            case "Tigger":
                return "Tiggr"
            case "Titan":
                return "Titan"
            case "Villain":
                return "Villn"
            case _:
                return self.value


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
        # Properties related to gameplay
        doNotReadyNextTurn: bool = False,
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


def printCard(card: Card):
    # This function will print a card in a formatted way
    nameAndCost = f"   >>>  {card.name}. C:{card.cost}{'i' if card.inkable else ''}, "
    stats = ""
    match card.card_type:
        case CardType.CHARACTER:
            classifications = ", ".join([c.shortened for c in card.classifications])
            stats = f"S:{card.strength}, W:{card.willpower}, L:{card.lore}, {classifications}"
        case CardType.LOCATION:
            stats = f"M:{card.moveCost}, W:{card.willpower}, L:{card.lore}"
        case CardType.ITEM:
            stats = "Item"
        case CardType.ACTION:
            stats = "Action"
        case CardType.SONG:
            stats = "Song"
    abilities = ". " + card.abilities if card.abilities else ""
    fullText = nameAndCost + stats + abilities
    print(fullText)
