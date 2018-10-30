class Park:
    def __init__(self, temperature, animals, dimension):
        self.temperature = temperature
        self.animals = animals
        self.big_carn = 0
        self.small_carn = 0
        self.big_erb = 0
        self.small_erb = 0
        self.dimension = dimension


# count how many animals of each "big/small", eating "meat/plants"
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