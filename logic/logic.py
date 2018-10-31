from logic.animals import *
import random
import numpy


# here i follow the Abstract factory Pattern in order to create the several animal factories that i need

class AbstractFactory(object):

    def __init__(self, animal_factory=None):
        self.animal_factory = animal_factory

    def generate_exemplar(self):
        return self.animal_factory()


# the "computer" of the passing of the time

class Computer:
    def __init__(self):
        self.name = "survive_computer"

# deaths

    def compute_deaths(self, park):
        park_deaths = dict()        # how many deaths for each animal

        for animal_type in park.animals:
            if len(park.animals[animal_type]) > 1:
                park_deaths[animal_type] = self.die(park.animals[animal_type][0], park)
                for dead in range(0, park_deaths[animal_type]):
                    if len(park.animals[animal_type]) > 20:
                        park.animals[animal_type].pop()         # each fight that kills animal

        return park

    @staticmethod                  # compute the death of single species
    def die(animal, park):
        tot_erb = park.small_erb + park.big_erb
        tot_carn = park.small_carn + park.big_carn
        puppy_shield = 0

        if animal.diet == "meat":
            if tot_carn < 0.5 * tot_erb:                        # if there is enough erb to fight
                deaths = 0.15*len(park.animals[animal.name])
            else:
                deaths = 0.3*len(park.animals[animal.name]) # more  kills among carnivores (each other)
        else:
            if animal.size == "big":
                deaths = 0.3*len(park.animals[animal.name])
            else:
                deaths = 0.3*len(park.animals[animal.name])

        if animal.name[:5] == 'puppy':
            puppy_shield = 0.02 * len(park.animals[animal.name])      # puppies are super protected from predators!!

        return int(deaths + puppy_shield)

# births

    def compute_births(self, park):
        park_births = dict()

        for animal_type in park.animals:
            species = animal_type[6:]
            if animal_type[:5] == "adult":  # let's consider only the adults..
                # ow many puppies?
                park_births[animal_type] = self.generate_puppies(park.animals[animal_type][0], park, species)
                call = "puppy_{}_factory.generate_exemplar()".format(species)

                for i in range(0, park_births[animal_type]):    # puppies born
                    park.animals["puppy_{}".format(species)].append(eval(call))

        return park

    @staticmethod
    def generate_puppies(animal, park, species):
        tot_erb = park.small_erb + park.big_erb
        tot_carn = park.small_carn + park.big_carn
        adult_of_species = "adult_" + species
        # how many puppies we can the populations generate?
        if animal.diet == "meat":
            if animal.size == "big":
                births = len(park.animals[adult_of_species]) * 0.2 + 0.1 * tot_carn + animal.n_puppies
            else:
                births = len(park.animals[adult_of_species]) * 0.4 + 0.1 * tot_erb + animal.n_puppies
        else:
            if animal.size == "big":
                births = len(park.animals[adult_of_species]) * 0.1 + 0.1 * tot_carn + animal.n_puppies
            else:
                births = len(park.animals[adult_of_species]) * 0.1 + 0.1 * tot_erb + animal.n_puppies

        return int(births)

# age

    @staticmethod
    def compute_age(park):
        for animal in park.animals.keys():
            species = animal[6:]

            if animal[:5] == "adult":                       # if is adult, just add 1 year
                for exemplar in park.animals[animal]:
                    exemplar.age += 1
                    if exemplar.age > exemplar.death:
                        park.animals[animal].remove(exemplar)   # death by oldness

            else:                                           # else if is older than 2, it becomes an adult
                for exemplar in park.animals[animal]:
                    exemplar.age += 1
                    if exemplar.age >= 1:
                        park.animals["puppy_" + animal[6:]].remove(exemplar)
                        call = "adult_{}_factory.generate_exemplar()".format(species)
                        park.animals["adult_" + animal[6:]].append(eval(call))

    @staticmethod
    def compute_death_by_temp(park):

        if park.temperature < 13:                           # lower avg bound
            park.temperature += random.randint(1, 6)
        elif park.temperature > 35:                         # upper avg bound
            park.temperature += random.randint(0, -4)
        else:
            park.temperature += random.randint(-2, +2)      # variation

        for animal_type in park.animals.keys():             # how will each exemplar survive this temperature?
            for exemplar in park.animals[animal_type]:
                if exemplar.climate not in [x for x in range(park.temperature-5, park.temperature+5)]:
                    park.animals[animal_type].remove(exemplar)
        print("temperature --->", park.temperature)

# complete phase

    def compute_phase(self, park):          # a complete age
        self.compute_deaths(park)
        self.compute_births(park)
        self.compute_age(park)
        self.compute_death_by_temp(park)
        return park


def anim_gen(*args):                # starting park generator
    park = dict()
    adults = ['adult_lion', 'adult_hyena', 'adult_zebra', 'adult_gnu',
              'puppy_lion', 'puppy_hyena', 'puppy_zebra', 'puppy_gnu']
    for arg in range(0, len(args)):
        park[adults[arg]] = []
        for i in range(0, args[arg]):
            call = str(adults[arg]) + '_factory' + '.generate_exemplar()'
            park[adults[arg]].append(eval(call))
    return park


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


