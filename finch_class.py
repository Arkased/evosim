import random

NEW_FOOD = 1
AGGRO_SD = .1

BREED_COST = 1
FOOD_UPKEEP = 1
AGGRO_COST = .33
AGGRO_SHARES = 2
PASSIVE_SHARES = 1


# noinspection PyTypeChecker
class Finch:
    BREED_THRESHOLD = 2

    def __init__(self, aggression=False):
        if aggression:
            self.aggression = min(max(0, aggression), 1)
        else:
            self.aggression = random.uniform(0, 1)
        self.food = NEW_FOOD
        self.shares = None

    def __repr__(self):
        return str(self.aggression)

    def compete(self):
        if random.uniform(0, 1) <= self.aggression:
            self.food -= AGGRO_COST
            self.shares = AGGRO_SHARES
        else:
            self.shares = PASSIVE_SHARES
        return self.shares

    def upkeep(self):
        if self.food < FOOD_UPKEEP:
            return False
        else:
            self.food -= FOOD_UPKEEP
            return True

    def breed(self, other):
        if self.food < self.BREED_THRESHOLD or other.food < self.BREED_THRESHOLD:
            print("cannot breed. food: " + self.food + ", " + other.food)
            raise Exception
        else:
            self.food -= BREED_COST
            other.food -= BREED_COST
            aggression = (self.aggression + other.aggression) / 2 + random.normalvariate(0, AGGRO_SD)
            return Finch(aggression)
