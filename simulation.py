from logic.park import *
from logic.animals import *
from logic.logic import *
import matplotlib.pyplot as plt
import numpy as np

# adults animal factory
puppy_lion_factory = AbstractFactory(PuppyLion)
puppy_hyena_factory = AbstractFactory(PuppyHyena)
puppy_zebra_factory = AbstractFactory(PuppyZebra)
puppy_gnu_factory = AbstractFactory(PuppyGnu)
# puppies animal factory
adult_lion_factory = AbstractFactory(AdultLion)
adult_hyena_factory = AbstractFactory(AdultHyena)
adult_zebra_factory = AbstractFactory(AdultZebra)
adult_gnu_factory = AbstractFactory(AdultZebra)




animal_pool = anim_gen(60, 50, 200, 200, 8, 12, 20, 45)
park = Park(20, animal_pool, 2500)
park.init_park()
comp = Computer()

statistics = {}

for animal in park.animals:
        statistics[animal] = []
n = 100
for age in range(0, n):
    for animal in park.animals:
        statistics[animal].append(len(park.animals[animal]))
    park = comp.compute_phase(park)


# set figsize -> big
plt.rcParams["figure.figsize"] = [16, 9]
# observations of the environment
x = np.arange(100)
# plots every species
for key in statistics.keys():
    plt.plot(x, statistics[key])

# creates the legenda with all the species colours
legenda = []
for key in statistics.keys():
    legenda.append('y = {}'.format(key))
# puts the legenda in the proper position and adjust the text dimension
plt.legend(legenda, loc="upper left", prop={'size': 12})

# show the plot
# plt.show()


