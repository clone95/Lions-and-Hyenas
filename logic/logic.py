from logic.animals import *
import random


class AbstractFactory(object):

    def __init__(self, animal_factory=None):
        self.animal_factory = animal_factory

    def generate_exemplar(self):
        return self.animal_factory()


class Computer:
    def __init__(self):
        self.name = "survive_computer"

# deaths

    def compute_deaths(self, park):
        park_deaths = dict()

        for animal_type in park.animals:
            park_deaths[animal_type] = self.die(park.animals[animal_type][0], park)
            if len(park.animals[animal_type]) <= -park_deaths[animal_type]:
                park.animals[animal_type] = park.animals[animal_type][:1]
            else:
                park.animals[animal_type] = park.animals[animal_type][:park_deaths[animal_type]]
        return park

    @staticmethod
    def die(animal, park):
        tot_erb = park.small_erb + park.big_erb
        tot_carn = park.small_carn + park.big_carn
        puppy_shield = 0

        if animal.diet == "meat":
            if tot_carn < 0.2 * tot_erb:
                deaths = -(0.1*tot_carn)
            else:
                deaths = -(0.1*tot_carn)
        else:
            if animal.size == "big":
                deaths = -(0.2*park.big_carn)
            else:
                deaths = -(0.3*park.small_carn)

        if animal.name[:5] == 'puppy':
            puppy_shield = 5

        return int(deaths + puppy_shield)

# births

    def compute_births(self, park):
        park_births = dict()

        for animal_type in park.animals:
            species = animal_type[6:]
            if animal_type[:5] == "adult":
                park_births[animal_type] = self.generate_puppies(park.animals[animal_type][0], park, species)
                call = "puppy_{}_factory.generate_exemplar()".format(species)

                for i in range(0, park_births[animal_type]):
                    park.animals["puppy_{}".format(species)].append(eval(call))

        return park

    @staticmethod
    def generate_puppies(animal, park, species):
        tot_erb = park.small_erb + park.big_erb
        tot_carn = park.small_carn + park.big_carn
        births = 0
        adult_of_species = "adult_" + species
        # how many puppies we can the populations generate?
        if animal.diet == "meat":
            if animal.size == "big":
                births = len(park.animals[adult_of_species]) * 0.2 + random.randint(2, 20)
            else:
                births = len(park.animals[adult_of_species]) * 0.4 + random.randint(2, 40)
        else:
            if animal.size == "big":
                births = len(park.animals[adult_of_species]) * 0.2 + random.randint(2, 20)
            else:
                births = len(park.animals[adult_of_species]) * 0.4 + random.randint(2, 40)

        return int(births)

# age
    @staticmethod
    def compute_age(park):

        for animal in park.animals.keys():
            species = animal[6:]
            if animal[:5] == "adult":
                for exemplar in park.animals[animal]:
                    exemplar.age += 1
                    if animal == "adult_lion":

                        print(len(park.animals[animal]))
                    if exemplar.age > exemplar.death and len(park.animals[animal]) > 1:
                        park.animals[animal].remove(exemplar)
                        print("a")
            else:
                for exemplar in park.animals[animal]:
                    exemplar.age += 1

                if exemplar.age > 1:

                    if len(park.animals["puppy_" + animal[6:]]) > 1:

                        park.animals["puppy_" + animal[6:]].remove(exemplar)
                        print(len(park.animals["adult_" + animal[6:]]))
                        call = "puppy_{}_factory.generate_exemplar()".format(species)
                        park.animals["adult_" + animal[6:]].append(eval(call))
                        print(len(park.animals["adult_" + animal[6:]]))




        pass


# complete phase

    def compute_phase(self, park):
        self.compute_deaths(park)
        self.compute_births(park)
        self.compute_age(park)
        # park = park + births
        # park = self.compute_survivors(park)

        #final_park.init_park()
        #print(animals_after_deaths)

        return park


def anim_gen(*args):
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

# def calculate_population(animal_list):
#     types = set()
#     exemplars = dict()
#
#     for element in animal_list:
#         if element.name not in types:
#             types.add(element.name)
#
#     for animal_type in types:
#         exemplars[animal_type] = 1
#
#     for animal in animal_list:
#         exemplars[animal.name] += 1
#
#     return exemplars


# calculate_population(animal_list)

