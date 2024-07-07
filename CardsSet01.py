# Classes representing the models of the cards in the game. 
# Each of these card model classes are subclasses of one of the Card subclassess: Character, Location, Action, Song, and Item.

from MainClasses import *


class Card_01_001(Character):
    def __init__(self):
        super().__init__(
            name="Ariel - On Human Legs",
            color=CardColor.AMBER,
            cost=4,
            inkable=True,
            baseName="Ariel",
            version="On Human Legs",
            classifications=[
                CharacterClassification.STORYBORN,
                CharacterClassification.HERO,
                CharacterClassification.PRINCESS,
            ],
            strength=3,
            willpower=4,
            lore=2,
            abilities="VOICELESS This character can't exert to sing songs.",
        )


class Card_01_002(Character):
    def __init__(self):
        super().__init__(
            name="Ariel - Spectacular Singer",
            color=CardColor.AMBER,
            cost=3,
            inkable=True,
            baseName="Ariel",
            version="Spectacular Singer",
            classifications=[
                CharacterClassification.STORYBORN,
                CharacterClassification.HERO,
                CharacterClassification.PRINCESS,
            ],
            strength=2,
            willpower=3,
            lore=1,
            abilities="Singer 5. MUSICAL DEBUT When you play this character, look at the top 4 cards of your deck. You may reveal a song card and put it into your hand. Put the rest on the bottom of your deck in any order.",
        )

class Card_01_025(Song):
    def __init__(self):
        super().__init__(
            name="Be Our Guest",
            color=CardColor.AMBER,
            cost=2,
            inkable=True,
            abilities="",
        )

class Card_01_066(Item):
    def __init__(self):
        super().__init__(
            name="Beast's Mirror",
            color=CardColor.AMETHYST,
            cost=2,
            inkable=False,
            abilities="When you play this item, choose a character. That character gains 2 strength until the end of the turn.",
        )

class Card_03_170(Location):
    def __init__(self):
        super().__init__(
            name="Motunui - Island Paradise",
            color=CardColor.SAPPHIRE,
            cost=2,
            inkable=True,
            baseName="Motunui",
            version="Island Paradise",
            willpower=5,
            lore=1,
            moveCost=1,
            abilities="REINCARNATION Whenever a character is banished while here, you may put that card into your inkwell facedown and exerted.",
        )