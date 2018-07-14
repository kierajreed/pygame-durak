import pygame
import sys
import utils
import random
from ai import AiPlayer
from human import HumanPlayer


# Initialize pygame and make the window. #
pygame.init()
pygame.display.set_caption('Durak!')
screen = pygame.display.set_mode(utils.SCREEN_SIZE)

deck = utils.get_deck_array(None)
trump_card = deck.pop(0)
trump_suit = trump_card.suit

deck = utils.get_deck_array(trump_card)
discard = []

players = [HumanPlayer(), AiPlayer()]
currentStarterIndex = random.randrange(0, 2)
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
        if event.type == pygame.MOUSEBUTTONUP:
            if utils.is_click_valid(event):
                if currentPlayerIndex == 0:
                    index = utils.get_clicked_index(event)

                    print 'index: {}, length: {}'.format(index, len(players[0].hand))

                    if currentPlayerIndex == currentStarterIndex:
                        if utils.is_valid_attack(cardsInPlay, players[0].hand[index]):
                            attackingCard = players[0].hand.pop(index)
                            cardsInPlay.append(attackingCard)

                            currentPlayerIndex = not currentPlayerIndex
                            turnInit = False
                    else:
                        pass
        elif event.type == pygame.QUIT:
            sys.exit()

    # Initialize the status. #
    if not turnInit:
        if players[currentPlayerIndex].isHuman:
            if currentPlayerIndex == currentStarterIndex:
                utils.set_status('Choose a card to attack!')
            else:
                utils.set_status('Choose a card to defend the {}!'.format(str(attackingCard)))

        utils.set_player_card_rects(players[0].hand)
        turnInit = True

    # The AI chooses cards. #
    if not players[currentPlayerIndex].isHuman:
        if currentPlayerIndex == currentStarterIndex:
            attackingCard = players[currentPlayerIndex].choose_card_to_attack(cardsInPlay)
            cardsInPlay.append(attackingCard)

            currentPlayerIndex = not currentPlayerIndex
            turnInit = False
        else:
            if utils.can_player_defend(players[1], attackingCard, trump_card.suit):
                cardsInPlay.append(players[1].choose_card_to_defend(attackingCard, trump_card.suit))

                attackingCard = None
                currentPlayerIndex = not currentPlayerIndex
                turnInit = False
            else:
                turnInit = False

    # Render the game. #
    screen.fill(utils.BACKGROUND)

    if trump_card is not None:
        screen.blit(utils.load_trump_card(trump_card), utils.TRUMP_POSITION)
    if len(deck) > 0:
        screen.blit(utils.load_card_back(), utils.DECK_POSITION)
    if len(discard) > 0:
        screen.blit(utils.load_card(discard[len(discard) - 1]), utils.DISCARD_POSITION)

    if len(cardsInPlay) > 0:
        for index in range(0, len(cardsInPlay)):
            screen.blit(utils.load_card(cardsInPlay[index]), utils.get_play_position(index, len(cardsInPlay)))

    for index in range(0, len(players[0].hand)):
        screen.blit(utils.load_card(players[0].hand[index]), utils.get_card_position(index, len(players[0].hand), False))
    for index in range(0, len(players[1].hand)):
        screen.blit(utils.load_card_back(), utils.get_card_position(index, len(players[1].hand), True))

    if utils.get_status() is not None:
        screen.blit(utils.get_status_message(), utils.STATUS_POSITION)

    pygame.display.flip()
