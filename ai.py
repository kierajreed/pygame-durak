import utils

class AiPlayer(object):
    def __init__(self):
        self.hand = []
        self.isHuman = False

    def chooseCardToAttack(self, cardsInPlay):
        maxValue = 24
        selectedCardIndex = None
        for index in range(0, len(self.hand)):
            card = self.hand[index]

            if card.value < maxValue:
                selectedCardIndex = index
                maxValue = card.value

        return self.hand.pop(selectedCardIndex)

    def chooseCardToDefend(self, attackingCard, trump_suit):
        maxValue = 24
        selectedCardIndex = None
        valid_suits = [attackingCard.suit, trump_suit]

        for index in range(0, len(self.hand)):
            card = self.hand[index]

            if card.suit in valid_suits:
                if card.value < maxValue and card.value > attackingCard.value:
                    selectedCardIndex = index
                    maxValue = card.value

        return self.hand.pop(selectedCardIndex)
