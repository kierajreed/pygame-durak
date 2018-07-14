class Card(object):
    def __init__(self, rank, suit, is_trump):
        self.rank = rank
        self.suit = suit
        self.filename = rank[:1] + suit[:1] + '.png'
        self.value = self.get_value()
        if is_trump:
            self.value += 9

    def get_value(self):
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

    def to_string(self):
        try:
            int(self.rank)
            return ['#', '#', '#', '#', '#', '#', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'][int(self.rank)] + ' of ' + self.suit
        except ValueError:
            return self.rank + ' of ' + self.suit

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.to_string()
