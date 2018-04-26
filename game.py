import pygame, sys
import utils
import random
from ai import AiPlayer
from human import HumanPlayer

if __name__ == '__main__':
        # Initialize pygame and make the window. #
        pygame.init()
        pygame.display.set_caption('Durak!')
        screen = pygame.display.set_mode(utils.SCREEN_SIZE)


        deck = utils.getDeckArray(None)
        trump_card = deck.pop(0)
        trump_suit = trump_card.suit

        deck = utils.getDeckArray(trump_card)

        players = [HumanPlayer(), AiPlayer()]
        currentPlayerIndex = random.randrange(0, 1)

        # Deal the cards. #
        for index in range(0, 12):
            if index % 2 == 0:
                players[0].hand.append(deck.pop(index))
            else:
                players[1].hand.append(deck.pop(index))

        game_state = {}

        # Start the game loop. #
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            screen.fill(utils.BACKGROUND)

            screen.blit(utils.loadTrumpCard(trump_card), utils.TRUMP_POSITION)
            screen.blit(utils.loadCardBack(), utils.DECK_POSITION)

            for index in range(0, len(players[0].hand)):
                screen.blit(utils.loadCard(players[0].hand[index]), utils.getCardPosition(index, len(players[0].hand), False))
            for index in range(0, len(players[1].hand)):
                screen.blit(utils.loadCardBack(), utils.getCardPosition(index, len(players[1].hand), True))
            if utils.STATUS != None:
                screen.blit(utils.getStatusMessage(), utils.STATUS_POSITON)

            pygame.display.flip()
