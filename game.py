import pygame
import utils
import sys

# Initialize pygame and make the window. #
pygame.init()
#pygame.display.set_icon(utils.loadImage('logo.png'))
pygame.display.set_caption('Durak!')
screen = pygame.display.set_mode(utils.SCREEN_SIZE)

deck = utils.getDeckArray()

# Start the game loop. #
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(utils.BACKGROUND)
    pygame.display.flip()
