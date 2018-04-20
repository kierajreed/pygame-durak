import pygame
import utils
import sys

def main():
    # Initialize pygame and make the window. #
    pygame.init()
    #pygame.display.set_icon(utils.loadImage('logo.png'))
    pygame.display.set_caption('Durak!')
    screen = pygame.display.set_mode(utils.SCREEN_SIZE)

    deck = utils.getDeckArray(None)
    trump_card = deck.pop(0)
    trump_suit = trump_card.suit

    deck = utils.getDeckArray(trump_card)

    # DEBUG #
    print(deck)
    print('trump_card: ' + str(trump_card))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            screen.fill(utils.BACKGROUND)
            pygame.display.flip()

# Start the game loop. #
if __name__ == '__main__':
        main()
