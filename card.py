class Card(object):
    def __init__(self, rank, suit, isTrump):
        self.rank = rank
        self.suit = suit
        self.filename = rank[:1] + suit[:1] + '.png'
        self.value = self.getValue()
        if(isTrump):
            self.value += 9

    def getValue(self):
        try:
            int(self.rank)
            return int(self.rank)
        except ValueError:
            if self.rank == 'Jack':
                return 11
            elif self.rank == 'Queen':
                return 12
            elif self.rank == 'King':
                return 13
            elif self.rank == 'Ace':
                return 14
            else:
                raise Exception('Invalid value!')

    def toString(self):
        try:
            int(self.rank)
            return ['#', '#', '#', '#', '#', '#', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'][int(self.rank)] + ' of ' + self.suit
        except ValueError:
            return self.rank + ' of ' + self.suit

    def __str__(self):
        return self.toString()
    def __repr__(self):
        return self.toString()
