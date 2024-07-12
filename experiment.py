from game import *


"""
3 Ariel - On Human Legs; 5 Ariel - Spectacular Singer; 4 Be Our Guest; 5 Beast's Mirror; 1 Gaston; 5 Motunui - Island Paradise 
"""
# game = Game()
# game.run()

a = parseDeckList(
    "1 Ariel - On Human Legs; 1 Ariel - Spectacular Singer; 1 Be Our Guest; 1 Beast's Mirror; 1 Motunui - Island Paradise"
)
for card in a:
    printCard(card)
