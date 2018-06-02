import pygame, sys
import utils
import random
from ai import AiPlayer
from human import HumanPlayer

# Initialize pygame and make the window. #
pygame.init()
pygame.display.set_caption('Durak!')
screen = pygame.display.set_mode(utils.SCREEN_SIZE)


deck = utils.getDeckArray(None)
trump_card = deck.pop(0)
trump_suit = trump_card.suit

deck = utils.getDeckArray(trump_card)
discard = []

players = [HumanPlayer(), AiPlayer()]
currentStarterIndex = random.randint(0, 1)
currentPlayerIndex = currentStarterIndex

# Deal the cards. #
for index in range(0, 12):
    if index % 2 == 0:
        players[0].hand.append(deck.pop(index))
    else:
        players[1].hand.append(deck.pop(index))

attackingCard = None
cardsInPlay = []

turnInit = False
turnComplete = False

# Start the game loop. #
while True:
    # Check for events. #
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print 'click'
        elif event.type == pygame.QUIT:
            sys.exit()

    # Initialize the status. #
    if not turnInit:
        if players[currentPlayerIndex].isHuman:
            if currentPlayerIndex == currentStarterIndex:
                utils.setStatus('Choose a card to attack!')
            else:
                utils.setStatus('Choose a card to defend the {}!'.format(str(attackingCard)))

        turnInit = True

    # The AI chooses cards. #
    if not players[currentPlayerIndex].isHuman:
        if currentPlayerIndex == currentStarterIndex:
            attackingCard = players[currentPlayerIndex].chooseCardToAttack(cardsInPlay)
            cardsInPlay.append(attackingCard)

            currentPlayerIndex = not currentPlayerIndex
            turnInit = False
        else:
            pass
            #cardsInPlay.append(players[currentPlayerIndex].chooseCardToDefend(attackingCard))

            #attackingCard = None
            #currentPlayerIndex = not currentPlayerIndex


    # Render the game. #
    screen.fill(utils.BACKGROUND)

    if(trump_card != None):
        screen.blit(utils.loadTrumpCard(trump_card), utils.TRUMP_POSITION)
    if(len(deck) > 0):
        screen.blit(utils.loadCardBack(), utils.DECK_POSITION)
    if len(discard) > 0:
        screen.blit(utils.loadCard(discard[len(discard) - 1]), utils.DISCARD_POSITION)

    for index in range(0, len(players[0].hand)):
        screen.blit(utils.loadCard(players[0].hand[index]), utils.getCardPosition(index, len(players[0].hand), False))
    for index in range(0, len(players[1].hand)):
        screen.blit(utils.loadCardBack(), utils.getCardPosition(index, len(players[1].hand), True))

    if utils.getStatus() != None:
        screen.blit(utils.getStatusMessage(), utils.STATUS_POSITON)

    pygame.display.flip()
