'''
This is a Command Line Card Game
'''

from enum import Enum

class CardType(Enum):
    CHARACTER = "Character"
    LOCATION = "Location"
    ACTION = "Action"
    SONG = "Song"

class CardColor(Enum):
    AMBER = "Amber"
    AMETHYST = "Amethyst"
    EMERALD = "Emerald"
    RUBY = "Ruby"
    SAPPHIRE = "Sapphire"
    STEEL = "Steel"


class Card:
    def __init__(self, name: str, card_type: CardType, color: CardColor, cost: int, inkwell: bool):
        self.name = name
        self.card_type = card_type
        self.color = color
        self.cost = cost
        self.inkwell = inkwell

    def __str__(self):
        return f'Card {self.name} ({self.color} {self.card_type}, inkwell symbol {self.inkwell}, cost {self.cost})'
    

