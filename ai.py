import utils

class AiPlayer(object):
    def __init__(self):
        self.hand = []
        self.isHuman = False

    def chooseCardToAttack(self, cardsInPlay):
        maxValue = 24
        selectedCard = None
        for card in self.hand:
            if card.value < maxValue:
                selectedCard = card
                maxValue = selectedCard.value

        return selectedCard

    def chooseCardToDefend(self, attackingCard):
        return None
