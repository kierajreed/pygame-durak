class Player(object):
    def __init__(self):
        self.hand = []

    def chooseCardToDefend(self, game_state):
        raise Exception('Abstract method from Player not implemented in {}!'.format(self.__class__.__name__))

    def chooseCardToAttack(self, game_state):
        raise Exception('Abstract method from Player not implemented in {}!'.format(self.__class__.__name__))
