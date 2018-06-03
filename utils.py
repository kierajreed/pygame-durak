import pygame
import random
from card import Card

# Constants and a few global variables. #
SCREEN_SIZE = WIDTH, HEIGHT = 1200, 840
BACKGROUND = 64, 64, 64

RANKS = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

CARD_SIZE = (150, 228)

DECK_POSITION = (10, (HEIGHT - 228) / 2)
DISCARD_POSITION = (1040, (HEIGHT - 228) / 2)
TRUMP_POSITION = (43, (HEIGHT - 150) / 2)

HAND_WIDTH = 1160
HAND_POSITION = HAND_X, HAND_Y = ((WIDTH - HAND_WIDTH) / 2 + 100, HEIGHT - 160)
AI_HAND_POSITION = AI_HAND_X, AI_HAND_Y = ((WIDTH - HAND_WIDTH) / 2 + 100, - 100)

STATUS = None
STATUS_POSITON = (300, 600)

PLAYER_CARD_RECTS = []

# Helper functions used to make code cleaner. #
def loadCard(card):
    image = pygame.image.load('assets/images/cards/' + card.filename)
    return pygame.transform.scale(image, CARD_SIZE)

def loadTrumpCard(card):
    return pygame.transform.rotate(loadCard(card), 270)

def loadCardBack():
    return pygame.transform.scale(pygame.image.load('assets/images/cards/back.png'), CARD_SIZE)


def getDeckArray(revealedCard):
    deck = []

    for suit in SUITS:
        for rank in RANKS:
            if revealedCard != None:
                if revealedCard.suit == suit:
                    if revealedCard.rank == rank :
                        continue
                    else:
                        deck.append(Card(rank, suit, True))
                else:
                    deck.append(Card(rank, suit, False))
            elif revealedCard == None :
                deck.append(Card(rank, suit, False))

    random.shuffle(deck)
    return deck


def getCardPosition(index, num_cards, opponent):
    if opponent:
        if index == 0:
            return AI_HAND_POSITION
        else:
            return (AI_HAND_X + ((HAND_WIDTH - 150) / num_cards) * index, AI_HAND_Y)
    else:
        if index == 0:
            return HAND_POSITION
        else:
            return (HAND_X + ((HAND_WIDTH - 150) / num_cards) * index, HAND_Y)


def getStatus():
    return STATUS

def setStatus(status):
    global STATUS
    STATUS = status

def getStatusMessage():
    if pygame.font.get_init() == False:
        pygame.font.init()

    font = pygame.font.SysFont('Arial', 30)
    return font.render(STATUS, False, (0, 0, 0))


def addTuples(a, b):
    return (a[0] + b[0], a[1] + b[1])

def setPlayerCardRects(hand):
    global PLAYER_CARD_RECTS
    pass


def checkEvent(event):
    print event.pos

    for rect in PLAYER_CARD_RECTS:
        if rect.collidepoint(event.pos):
            return True

    return False







#
