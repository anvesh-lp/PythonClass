from random import randint as r


class Dice:
    def __init__(self, si=6):
        self.size = si

    def randomeNumber(self):
        return r(1, self.size)


d1 = Dice()
d2 = Dice(12)

print(d1.randomeNumber() + d2.randomeNumber())
