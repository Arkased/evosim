from matplotlib import pyplot
from finch_class import Finch
import finch_class
import random
from statistics import mean

STARTING_POP = 100
BUNDLES_PER_TURN = 50
FOOD_PER_BUNDLE = 2

data = []
means = []
population = [Finch() for _ in range(STARTING_POP)]
foods = []


def turn():
    # compete for food
    foods.extend([[] for _ in range(BUNDLES_PER_TURN)])
    for finch in population:
        random.choice(foods).append(finch)
    for food in foods[:]:
        if food:
            foods.remove(food)
            total_shares = sum([finch.compete() for finch in food])
            for finch in food:
                finch.food += finch.shares / total_shares * FOOD_PER_BUNDLE
                finch.shares = None


    # breed
    breedables = filter(lambda finch: finch.food > Finch.BREED_THRESHOLD, population)
    try:
        population.append(breedables.__next__().breed(breedables.__next__()))
    except StopIteration:
        pass
    random.shuffle(population)

    # consume food (or starve)
    for finch in population:
        if not finch.upkeep():
            population.remove(finch)

    # record data
    aggros = [finch.aggression for finch in population]
    data.append(aggros)
    avg = mean(aggros)
    means.append(avg)
    print(avg)
