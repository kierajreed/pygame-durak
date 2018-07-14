class AiPlayer(object):
    def __init__(self):
        self.hand = []
        self.isHuman = False

    def choose_card_to_attack(self, cards_in_play):
        max_value = 24
        selected_card_index = None
        for index in range(0, len(self.hand)):
            card = self.hand[index]

            if card.value < max_value:
                selected_card_index = index
                max_value = card.value

        return self.hand.pop(selected_card_index)

    def choose_card_to_defend(self, attacking_card, trump_suit):
        max_value = 24
        selected_card_index = None
        valid_suits = [attacking_card.suit, trump_suit]

        for index in range(0, len(self.hand)):
            card = self.hand[index]

            if card.suit in valid_suits:
                if max_value > card.value > attacking_card.value:
                    selected_card_index = index
                    max_value = card.value

        return self.hand.pop(selected_card_index)
