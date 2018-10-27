from animals import *

class AbstractFactory(object):

    def __init__(self, animal_factory=None):
        self.animal_factory = animal_factory

    def generate_exemplar(self):
        return self.animal_factory()


class SurviveComputer:
    def __init__(self):
        self.name = "survive_computer"

    def survive_phase(self, park):
        print(self.name, park.animals)
        pass


class Park:
    def __init__(self, animals, meat, plants):
        self.animals = animals
        self.meat = meat
        self.plants = plants


adult_lion_factory = AbstractFactory(AdultLion)
puppy_lion_factory = AbstractFactory(PuppyLion)
adult_hyena_factory = AbstractFactory(AdultHyena)

animal_list = []

for el in range(1, 5):
    animal_list.append(adult_lion_factory.generate_exemplar())
    animal_list.append(puppy_lion_factory.generate_exemplar())
    animal_list.append(adult_hyena_factory.generate_exemplar())

animal_list.append(adult_hyena_factory.generate_exemplar())
animal_list.append(adult_hyena_factory.generate_exemplar())
animals = dict(dict())


def calculate_population(animal_list):
    types = set()
    exemplars = dict()

    for element in animal_list:
        if element.name not in types:
            types.add(element.name)

    for animal_type in types:
        exemplars[animal_type] = 1

    for animal in animal_list:
        exemplars[animal.name] += 1

    return exemplars


# calculate_population(animal_list)

