from logic.park import *


class AbstractFactory(object):

    def __init__(self, animal_factory=None):
        self.animal_factory = animal_factory

    def generate_exemplar(self):
        return self.animal_factory()


class Computer:
    def __init__(self):
        self.name = "survive_computer"

    def compute_deaths(self, park):
        park_deaths = dict()

        for animal_type in park.animals:
            # print("______________________________")
            # print("index:", animal_type, len(park.animals[animal_type]))

            park_deaths[animal_type] = self.die(park.animals[animal_type][0], park)

            if len(park.animals[animal_type]) <= -park_deaths[animal_type]:
                park.animals[animal_type] = park.animals[animal_type][:1]
            else:
                park.animals[animal_type] = park.animals[animal_type][:park_deaths[animal_type]]
            # print(len(park.animals[animal_type]))
            # print("--")
            # print("morti: ", park_deaths[animal_type])
            # print("index:", animal_type, len(park.animals[animal_type]))
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

    def compute_births(self, park):
        pass

    def compute_survivors(self, park):
        pass

    def compute_phase(self, park):
        animals_after_deaths = self.compute_deaths(park)

        # births = self.compute_births(park)
        # park = park + births
        # park = self.compute_survivors(park)

        #final_park.init_park()
        #print(animals_after_deaths)
        return animals_after_deaths


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

