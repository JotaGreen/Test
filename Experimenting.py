from MainClasses import *
from CardsSet01 import *

deckP1 = Deck("Player 1", [])

deckP1.parseDeckList(
    """2 Ariel - On Human Legs
1 Ariel - Spectacular Singer
1 Be Our Guestr
1 Beast's Mirror"""
)

for card in deckP1.cards:
    print(card)
