from animals import *


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
            park_deaths[animal_type] = self.die(park.animals[animal_type][0], park)
        return park_deaths

    @staticmethod
    def die(animal, park):
        tot_erb = park.small_erb + park.big_erb
        tot_carn = park.small_carn + park.big_carn
        puppy_shield = 0

        if animal.diet == "meat":
            if tot_carn < 0.2 * tot_erb:
                deaths = -(0.1*tot_carn)
            else:
                deaths = -(0.3*tot_carn)
        else:
            if animal.size == "big":
                deaths = -(0.3*park.big_carn)
            else:
                deaths = -(0.3*park.small_carn)

        if animal.name[:5] == 'puppy':
            puppy_shield = 2

        return deaths + puppy_shield



    @staticmethod
    def subtract_deaths(dic1, dic2):
        for el in dic1:
            dic1[el] = dic1[el] - dic2[el]
        return dic1

    def compute_births(self, park):
        pass

    def compute_survivors(self, park):
        pass

    def compute_phase(self, park):
        deaths = self.compute_deaths(park)
        park = self.subtract_deaths(park, deaths)
        # births = self.compute_births(park)
        # park = park + births
        # park = self.compute_survivors(park)
        return park


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

