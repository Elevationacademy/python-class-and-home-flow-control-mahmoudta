import random

class Deck:
    def __iniy__(self):
        self.cardlist = []
        self.creat()

    def creat(self):
        for s in ['Red', 'Blue', 'Green', 'Yellow']:
            for v in range(1, 11):
                self.cardlist.append([s, v])

    def shuffledeck(self):
        random.shuffle(self.cardlist)

    def deal(self):
        card = random.pop(self.cardlist)
        return card



