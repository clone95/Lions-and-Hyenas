from logic.park import *
from logic.animals import *
from logic.logic import *



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
comp = Computer()


print(len(park.animals["adult_lion"]))

for a in park.animals:
    print(len(park.animals[a]))
a = comp.compute_phase(park)
print("\n", len(a.animals["adult_lion"]))

b = comp.compute_phase(a)
print("\n", len(b.animals["adult_lion"]))
c = comp.compute_phase(b)





