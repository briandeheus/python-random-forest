from random import choice


class RandomForest:
    FORESTS = []

    def __init__(self):
        if self.FORESTS:
            return

        with open("forests") as f:
            self.FORESTS = f.read().splitlines()

    def get(self):
        return choice(self.FORESTS)

