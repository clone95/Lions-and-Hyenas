

class AbstractFactory(object):

    def __init__(self, animal_factory=None):
        self.animal_factory = animal_factory

    def generate_exemplar(self):
        return self.animal_factory()


#   Lion  ----------------------------------------------------------------------------


class AdultLion(object):

    def __init__(self):
        self.name = "adult_lion"
        self.age = 2
        self.death = 10
        self.weight = 200
        self.size = "big"
        self.diet = "meat"
        self.climate = 25
        self.group_dimension = 6
        self.n_puppies = 4
        self.area_for_animal = 25


class PuppyLion(object):

    def __init__(self):
        self.name = "puppy_lion"
        self.age = 0
        self.weight = 50
        self.size = "big"
        self.diet = "meat"
        self.climate = 25
        self.group_dimension = 6
        self.area_for_animal = 25


#   Hyena  ----------------------------------------------------------------------------


class AdultHyena(object):

    def __init__(self):
        self.name = "adult_hyena"
        self.age = 2
        self.death = 15
        self.weight = 50
        self.size = "small"
        self.diet = "meat"
        self.climate = 23
        self.group_dimension = 15
        self.n_puppies = 6
        self.area_for_animal = 4


class PuppyHyena(object):

    def __init__(self):
        self.name = "puppy_hyena"
        self.age = 0
        self.weight = 50
        self.size = "small"
        self.diet = "meat"
        self.climate = 25
        self.group_dimension = 15
        self.area_for_animal = 4


#   Zebra  ----------------------------------------------------------------------------


class AdultZebra(object):

    def __init__(self):
        self.name = "adult_zebra"
        self.age = 2
        self.death = 400
        self.weight = 50
        self.size = "big"
        self.diet = "plants"
        self.climate = 22
        self.group_dimension = 30
        self.n_puppies = 1
        self.area_for_animal = 16


class PuppyZebra(object):

    def __init__(self):
        self.name = "puppy_zebra"
        self.age = 0
        self.weight = 50
        self.size = "small"
        self.diet = "plants"
        self.climate = 22
        self.group_dimension = 30
        self.area_for_animal = 16


# Gnu   ----------------------------------------------------------------------------


class AdultGnu(object):

    def __init__(self):
        self.name = "adult_gnu"
        self.age = 2
        self.death = 20
        self.weight = 150
        self.size = "medium"
        self.diet = "plants"
        self.climate = 22
        self.group_dimension = 80
        self.n_puppies = 1
        self.area_for_animal = 9


class PuppyGnu(object):

    def __init__(self):
        self.name = "puppy_gnu"
        self.age = 0
        self.weight = 50
        self.size = "small"
        self.diet = "plants"
        self.climate = 22
        self.group_dimension = 80
        self.area_for_animal = 9









adult_lion_factory = AbstractFactory(AdultLion)
puppy_lion_factory = AbstractFactory(PuppyLion)
adult_hyena_factory = AbstractFactory(AdultHyena)

lions = []

for el in range(1, 5):
    lions.append(adult_lion_factory.generate_exemplar())
    lions.append(puppy_lion_factory.generate_exemplar())
    lions.append(adult_hyena_factory.generate_exemplar())


print([animal.diet for animal in lions])
