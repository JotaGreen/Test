from player import *
from helperfunctions import *


class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.firstTurn = True
        self.turn = None

    # This function will start the game
    # First it will ask for the deck list of each player and parse it into the player's deck
    # Then it will shuffle each player's deck and draw 7 cards for each player
    # Then it will ask each player how which cards they want to mulligan
    # The cards they want to mulligan will be placed on the bottom of their deck and they will draw that many cards
    # Then shuffle the deck again
    # The function should print a description of each step done
    # When asking for player input, the function should use the command line input function or
    # alternatively, you can pass a list of strings to the function which will be used as input
    def start(self):
        print("Starting the game.")
        # Decide the first player randomly, shuffling the players list
        random.shuffle(self.players)
        print(f"{self.players[0].name} will go first.")

        for player in self.players:
            print("\n")
            deckList = input(f"{player.name}, enter your deck list: ")
            print("\n")
            player.deck.cards = parseDeckList(deckList)
            player.deck.shuffle()
            player.hand += player.deck.getTop(num=7, print=False)
            print(f"{self.name} drew 7 cards.")
        for player in self.players:
            print(f"\n{player.name}'s hand:")
            for card in player.hand:
                printCard(card)
            mulligan = input(
                f"{player.name}, which cards do you want to mulligan? Enter the card names separated by semicolons and space '; ' "
            )
            mulligan = mulligan.split(";")
            # Remove leading and trailing whitespace from each card name, in case the user added extra spaces
            mulligan = [card.strip() for card in mulligan]
            # Remove empty strings from the mulligan list, in case the user added extra semicolons
            mulligan = list(filter(None, mulligan))
            mulliganCards = []
            for card in mulligan:
                for i in range(len(player.hand)):
                    if player.hand[i].name == card:
                        mulliganCards.append(player.hand.pop(i))
                        break
                # If the card is not found in the player's hand, print an error message
                else:
                    print(f"{card} was not found in {player.name}'s hand.")

            print(f"{player.name} will mulligan {len(mulliganCards)} cards.")
            player.deck.placeOnBottom(mulliganCards)
            player.hand += player.deck.getTop(num=len(mulliganCards), print=False)
            print(f"{self.name} drew {len(mulliganCards)} cards.")
            player.deck.shuffle()

    def run(self):
        self.start()

        while self.players[0].lore < 20 and self.players[1].lore < 20:
            try:
                for player in self.players:
                    self.turn = Turn(activePlayer=player, game=self)
                    self.turn.run()
            except PlayerDeckedOut as e:
                print(e)
                print("Game over")
                break


class Turn:
    def __init__(self, activePlayer: Player, game: Game):
        self.player = activePlayer
        self.game = game
        self.playerInked = False

    def run(self):
        self.beginningPhase()
        self.mainPhase()
        self.endPhase()

    def beginningPhase(self):
        print(f"Beginning {self.player.name}'s turn.")
        # Unexert all cards in play
        print(f"Readying all {self.player.name}'s characters, items, and ink in play.")
        self.player.inkExerted = 0
        for card in self.player.playZone:
            match card.type:
                case CardType.LOCATION:
                    continue
                case CardType.ITEM:
                    card.exerted = False
                case CardType.CHARACTER:
                    # If character was affected by an ability that prevents it from being readied,
                    # do not ready it and reset the flag
                    if card.doNotReadyNextTurn == True:
                        card.doNotReadyNextTurn = False
                        print(f"{card.name} was not readied.")
                    else:
                        card.exerted = False
        # Trigger the start of turn effects for all cards in play
        for card in self.player.playZone:
            card.onPlayerTurnStart()
        # Dry the ink
        for card in self.player.playZone:
            if card.type == CardType.CHARACTER and card.dry == False:
                card.dry = True
                print(f"{card.name} is now dry.")
        # Gain lore from locations
        for card in self.player.playZone:
            if card.type == CardType.LOCATION:
                self.player.lore += card.lore
                print(f"{self.player.name} gained {card.lore} lore from {card.name}.")
        # Resolve the bag
        self.resolveBag()
        # Draw a card
        if self.game.firstTurn:
            self.game.firstTurn = False
            print(f"{self.player.name} did not draw.")
        else:
            self.player.draw(1)
        # Resolve the bag again
        self.resolveBag()

    def mainPhase(self):
        self.player.lore += 1
        print(f"{self.player.name} gained 1 lore.")

    def endPhase(self):
        # Trigger the end of turn effects for all cards in play
        # The rules separate the end of turn effects into two steps:
        # First, effects reading "At the end of your turn" trigger and are resolved
        # Then effects that finish "this turn" end
        for card in self.player.playZone:
            card.onPlayerTurnEnd()
        self.resolveBag()
        for card in self.player.playZone:
            card.onThisTurnEnd()
        self.resolveBag()

    def resolveBag(self):
        pass
