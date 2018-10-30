# Lions-and-Hyenas

## Why?
I made this project to practice the Design Pattern theory, because the degree course was only theoretical and i think that the "learn by doing" way is far more effective to get into things. The structure of the project is based on the use of the Abstract Factory pattern, concretizing in the Factory Method pattern.

## What?
I imagined a virtual Savanna environment, with animal playing around inside (i mean, killing each other in the race for survival).
The first thing i did was a research about the bioma itself, and in particular i was looking for a group of species that truly interact each other in the real world.
During this journey i finally found an interesting micro-system (because, of course, this model is a super-semplification of the reality) that was fitting my needs.
The four animals population which you can play with are Lions, Hyenas, Zebras and Gnus.
The program wants to simulate the changes in populations during the time.
It wasn't a random animal choice, in fact we have two carnivores and two herbivores, with different sizes and habits, that really interact in the African Savanna.

The inspiration for the choice came from this video   (2 min)  -->   https://www.youtube.com/watch?v=_t1cHIgYFWo

The subtle tension and precise balance with which the two species relate to each other is impressive. Everyone knows their place in the food chain, and which is the final line that triggers the fight in front of the carcass of a prey.
So, not every lion is also a King.

## How to run the simulation
Clone the repo, and set the initial amount of each animal (you have the possibility to start with adults, or adults or puppies of each species), then you can run the simulations of how thepopulations of each species evolve during the time.
Epochs are set to 50, but you can choose the amount that you prefer.
I also imlemented a plotting function that displays with lovely colorful lines the evolution of the environment (how many exemplars are alive during each era).
Note that populations tend to grow fast, if the conditions are favorable, thus for a high amount of epochs a not trascurable amount of computation power is required.


I attach screenshots from some interesting runs.

In this simulation, we can see how the Lion (RED) and Hyena (ORANGE) populations are related in some way.
This is not surprending: in fact they fight a lot between them and they share the same resources.

![Figure 1-1](https://raw.github.com/clone95/Lions-and-Hyenas/master/1.PNG "1") 

Here we notice he important phenomenon of the scarcity - aboundance of resources: when herbivores populations decrease, also carnivores populations do. When they rise, also they do.

![Figure 1-1](https://raw.github.com/clone95/Lions-and-Hyenas/master/2.PNG "2") 

Here we have a bit crazy behavior of the populations, with the Hyena intensively following the Lions Trend in the end, but before that they followed the vanilla behavior (inverse proportionality).
We canalso see that the Hyenas number cause not small problems to Zebras, rapidly declining when Hyenas population spreads.

![Figure 1-1](https://raw.github.com/clone95/Lions-and-Hyenas/master/8.PNG "8") 



