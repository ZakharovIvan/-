class country:
    unique_id = 0
    def __init__(self, name, mainl, currency):
        self.id = country.unique_id
        self.name = name
        self.mainl = mainl
        self.currency = currency
        self.c_ids = []
        country.unique_id += 1

    def out(self):
        print str(self.id) + ': ' + self.name + ', ' + self.mainl + ' > ' + self.currency + '\n\t>' + str(self.c_ids)

class city:
    unique_id = 0
    def __init__(self, name, population, area, c_id):
        self.id = city.unique_id
        self.name = name
        self.population = population
        self.area = area
        self.c_id = c_id
        city.unique_id += 1

    def out(self):
        print str(self.id) + ': ' + self.name + '> ' + str(self.c_id) + '\n\tp: ' + str(self.population) + '| a: ' + str(self.area)