from logic import *


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


class Park:
    def __init__(self, temperature, animals, dimension):
        self.temperature = temperature
        self.animals = animals
        self.big_carn = 0
        self.small_carn = 0
        self.big_erb = 0
        self.small_erb = 0
        self.dimension = dimension

    def init_park(self):
        for animal in self.animals:
            if self.animals[animal][0].size == "big":
                if self.animals[animal][0].diet == "meat":
                    self.big_carn += len(self.animals[animal])
                else:
                    self.big_erb += len(self.animals[animal])
            else:
                if self.animals[animal][0].diet == "meat":
                    self.small_carn += len(self.animals[animal])
                else:
                    self.small_erb += len(self.animals[animal])


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


animal_pool = anim_gen(20, 50, 200, 400, 8, 12, 20, 45)
park = Park(20, animal_pool, 2500)
park.init_park()
print(park.big_carn)
print(park.big_erb)

comp = Computer()
a = comp.compute_deaths(park)
print(a)

