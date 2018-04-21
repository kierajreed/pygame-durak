import pygame
import random
from card import Card

# CONSTANTS #
SCREEN_SIZE = WIDTH, HEIGHT = 800, 600
BACKGROUND = 64, 64, 64

RANKS = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

CARD_SIZE = (150, 228)


# Helper functions used to make code cleaner. #
def loadImage(filename):
    return pygame.image.load('assets/images/' + filename)

def loadCard(card):
    image = pygame.image.load('assets/images/cards/' + card.filename)
    return pygame.transform.scale(image, CARD_SIZE)

def loadTrumpCard(card):
    return pygame.transform.rotate(loadCard(card), 270)

def loadCardBack():
    return pygame.transform.scale(loadImage('cards/back.png'), CARD_SIZE)


def getDeckArray(revealedCard):
    deck = []

    for suit in SUITS:
        for rank in RANKS:
            if(revealedCard != None):
                if(revealedCard.suit == suit):
                    if(revealedCard.rank == rank):
                        continue
                    else:
                        deck.append(Card(rank, suit, True))
                else:
                    deck.append(Card(rank, suit, False))
            elif(revealedCard == None):
                deck.append(Card(rank, suit, False))

    random.shuffle(deck)
    return deck

#def renderHand(hand, hidden):
