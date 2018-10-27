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
        for animal_type in park:
            park_deaths[animal_type] = self.die(animal_type)
        return park_deaths

    def die(self, animal):
        if animal.diet == "meat":
            pass
        else:
            pass

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

