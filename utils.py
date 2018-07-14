import pygame
import random
from card import Card


# Constants and a few global variables. #
SCREEN_SIZE = WIDTH, HEIGHT = 1200, 840
BACKGROUND = 64, 64, 64

RANKS = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

CARD_SIZE = (150, 228)

DECK_POSITION = (10, (HEIGHT - CARD_SIZE[1]) / 2)
DISCARD_POSITION = (1040, (HEIGHT - CARD_SIZE[1]) / 2)
TRUMP_POSITION = (43, (HEIGHT - CARD_SIZE[0]) / 2)

HAND_WIDTH = 1160
HAND_POSITION = HAND_X, HAND_Y = ((WIDTH - HAND_WIDTH) / 2 + 100, HEIGHT - 160)
AI_HAND_POSITION = AI_HAND_X, AI_HAND_Y = ((WIDTH - HAND_WIDTH) / 2 + 100, -100)

PLAY_WIDTH = 960
LEFT_OFFSET = 160
PLAY_TOP_POSITION = TOP_X, TOP_Y = ((WIDTH - PLAY_WIDTH) / 2 + LEFT_OFFSET, (HEIGHT - CARD_SIZE[1]) / 2 - 100)
PLAY_BOTTOM_POSITION = BOTTOM_X, BOTTOM_Y = ((WIDTH - PLAY_WIDTH) / 2 + LEFT_OFFSET + CARD_SIZE[0] / 2, (HEIGHT - CARD_SIZE[1]) / 2 + 100)

STATUS = None
STATUS_POSITION = (300, 600)

PLAYER_CARD_RECTS = []


# Helper functions used to make code cleaner. #
def load_card(card):
    image = pygame.image.load('assets/images/cards/' + card.filename)
    return pygame.transform.scale(image, CARD_SIZE)


def load_trump_card(card):
    return pygame.transform.rotate(load_card(card), 270)


def load_card_back():
    return pygame.transform.scale(pygame.image.load('assets/images/cards/back.png'), CARD_SIZE)


def get_deck_array(revealed_card):
    deck = []

    for suit in SUITS:
        for rank in RANKS:
            if revealed_card is not None:
                if revealed_card.suit == suit:
                    if revealed_card.rank == rank:
                        continue
                    else:
                        deck.append(Card(rank, suit, True))
                else:
                    deck.append(Card(rank, suit, False))
            elif revealed_card is None:
                deck.append(Card(rank, suit, False))

    random.shuffle(deck)
    return deck


def get_card_position(index, num_cards, opponent):
    if opponent:
        if index == 0:
            return AI_HAND_POSITION
        else:
            return AI_HAND_X + ((HAND_WIDTH - CARD_SIZE[0]) / num_cards) * index, AI_HAND_Y
    else:
        if index == 0:
            return HAND_POSITION
        else:
            return HAND_X + ((HAND_WIDTH - CARD_SIZE[0]) / num_cards) * index, HAND_Y


def get_play_position(index, num_cards):
    if index % 2 == 0:
        if index == 0:
            return PLAY_TOP_POSITION
        else:
            if PLAY_WIDTH - CARD_SIZE[0] * num_cards < 0:
                pass
            else:
                return TOP_X + CARD_SIZE[0] / 2 * index, TOP_Y
    else:
        if index == 1:
            return PLAY_BOTTOM_POSITION
        else:
            if PLAY_WIDTH - CARD_SIZE[0] * num_cards < 0:
                pass
            else:
                return BOTTOM_X + CARD_SIZE[0] / 2 * index, BOTTOM_Y


def get_status():
    return STATUS


def set_status(status):
    global STATUS
    STATUS = status


def get_status_message():
    if not pygame.font.get_init():
        pygame.font.init()

    font = pygame.font.SysFont('Arial', 30)
    return font.render(STATUS, False, (0, 0, 0))


def set_player_card_rects(hand):
    global PLAYER_CARD_RECTS

    first = get_card_position(0, len(hand), False)
    second = get_card_position(1, len(hand), False)

    if second[0] - first[0] < CARD_SIZE[0]:
        overlap = CARD_SIZE[0] - (second[0] - first[0])
        width = CARD_SIZE[0] - overlap
        for index in range(0, len(hand)):
            top_left = get_card_position(index, len(hand), False)

            PLAYER_CARD_RECTS.append(pygame.Rect(top_left, (width, CARD_SIZE[1])))
    else:
        for index in range(0, len(hand)):
            top_left = get_card_position(index, len(hand), False)

            PLAYER_CARD_RECTS.append(pygame.Rect(top_left, CARD_SIZE))

    print 'Set Rects for {} cards!'.format(len(hand))


def is_click_valid(event):
    for rect in PLAYER_CARD_RECTS:
        if rect.collidepoint(event.pos):
            return True

    return False


def get_clicked_index(event):
    for index in range(0, len(PLAYER_CARD_RECTS) - 0):
        if PLAYER_CARD_RECTS[index].collidepoint(event.pos):
            return index


def is_valid_attack(cards_in_play, card):
    if len(cards_in_play) == 0:
        return True
    else:
        valid_ranks = []

        for _card in cards_in_play:
            if _card.rank in valid_ranks:
                continue
            else:
                valid_ranks.append(_card.rank)

        if card.rank in valid_ranks:
            return True

    return False


def can_player_defend(player, to_defend, trump_suit):
    hand = player.hand
    valid_suits = [to_defend.suit, trump_suit]

    for card in hand:
        if card.suit in valid_suits and card.value > to_defend.value:
            return True

    return False
