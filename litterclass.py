from familytreedata import FamilyCat


class Litter:
    def __init__(self, size):
        self.size = size
        self.kittens = []
        for i in range(self.size):
            self.kittens.append(FamilyCat(0, 0, 0, 0, 1))
