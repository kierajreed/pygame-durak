import pygame, sys
import utils

if __name__ == '__main__':
        # Initialize pygame and make the window. #
        pygame.init()
        pygame.display.set_caption('Durak!')
        screen = pygame.display.set_mode(utils.SCREEN_SIZE)

        deck = utils.getDeckArray(None)
        trump_card = deck.pop(0)
        trump_suit = trump_card.suit

        deck = utils.getDeckArray(trump_card)

        player_hand = []
        ai_hand = []

        # Deal the cards. #
        for index in range(0, 12):
            if index % 2 == 0:
                player_hand.append(deck.pop(index))
            else:
                ai_hand.append(deck.pop(index))


        # Start the game loop. #
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                screen.fill(utils.BACKGROUND)

                screen.blit(utils.loadTrumpCard(trump_card), utils.TRUMP_POSITION)
                screen.blit(utils.loadCardBack(), utils.DECK_POSITION)

                pygame.display.flip()
