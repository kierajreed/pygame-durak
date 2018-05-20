from player import Player
import utils

class AiPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def chooseCardToAttack(self, cardsInPlay):
        utils.setStatus('Waiting for opponent...')

        return None

    def chooseCardToDefend(self, attackingCard):
        return None
