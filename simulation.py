from logic import *
import inspect



adult_lion_factory = AbstractFactory(AdultLion)
puppy_lion_factory = AbstractFactory(PuppyLion)
adult_hyena_factory = AbstractFactory(AdultHyena)
adult_zebra_factory = AbstractFactory(AdultZebra)
adult_gnu_factory = AbstractFactory(AdultZebra)
adult_zebra_factory = AbstractFactory(AdultZebra)

def park_gen(*args):
    park = dict()
    adults = ['adult_lion', 'adult_hyena', 'adult_zebra', 'adult_gnu']
    for arg in range(0, len(args)):
        park[adults[arg]] = []
        for i in range(0, args[arg]):
            call = str(adults[arg]) + '_factory' + '.generate_exemplar()'
            park[adults[arg]].append(eval(call))
    return park

parco = park_gen(2,3,4,5)
print(parco)
# computer
computer = Computer()

park = {}
print(park)
new_park = computer.compute_phase(park)
print(new_park)

