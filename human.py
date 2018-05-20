from player import Player
import pygame
import utils

class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def chooseCardToAttack(self, cardsInPlay):
        utils.setStatus('Choose a card to attack with!')

        return None

    def chooseCardToDefend(self, attackingCard):
        return None
