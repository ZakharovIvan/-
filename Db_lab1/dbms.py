from entity import country
from entity import city
from file_helper import file_helper

class dbms:
    id = 1
    name = 2
    mainl = 3
    currency = 4
    population = 5
    area = 6

    def __init__(self):
        self.countries = {}
        self.cities = {}

    def __del__(self):
        self.countries[-1] = country.unique_id
        self.cities[-1] = city.unique_id
        file_helper.dump_to_file(self.countries, "counrties.txt")
        file_helper.dump_to_file(self.cities, "cities.txt")

    def load_db(self):
        self.countries = file_helper.load_from_file("counties.txt")
        self.cities = file_helper.load_from_file("cities.txt")
        country.unique_id = self.countries[-1]
        city.unique_id = self.cities[-1]
        del self.countries[-1]
        del self.cities[-1]

    def out_countries(self):
        for i in self.countries:
            self.countries[i].out()

    @staticmethod
    def out_lands(countries):
        for i in countries:
            countries[i].out()

    def out_cityes(self):
        for i in self.cities:
           self.cities[i].out()

    def add_country(self,name, mainl, curr):
        tmp = country(name, mainl, curr)
        self.countries[tmp.id] = tmp

    def add_city(self, name, popul, area, c_id):
        tmp = city(name, popul, area, c_id)
        if c_id not in self.countries:
            print "There are no such country."
            return
        #self.countries[c_id].c_ids.append(tmp.id)
        self.cities[tmp.id] = tmp

    def del_city(self, id):
        if id in self.cities:
            #self.countries[self.cities[id].c_id].c_ids.remove(id)
            del self.cities[id]
        else:
            print "There is no city with such id"

    def del_country(self, id):
        if id in self.countries:
            # for i in self.countries[id].c_ids:
            #     self.del_city(i)
            for i in self.cities.copy():
                if self.cities[i].c_id == id:
                    self.del_city(i)
            del self.countries[id]
        else:
            print "there is no country with such id"

    def find_city(self, value, field):
        #TODO: make searching by field
        return

    def task_select(self):
        res = {}
        buf = {}
        for i in self.cities:
            id = self.cities[i].c_id
            if res.has_key(id):
                continue
            elif buf.has_key(id):
                if buf[id] > 3:
                    res[id] = self.countries[id]
                else:
                    buf[id] += 1
            else:
                buf[id] = 1
        return res


    def task_filter(self, land):
        counter = 0
        for c_id in land.c_ids:
            if self.cities[c_id].population > 1000000:
                counter += 1
        return counter > 3

    def collect_countries(self, filter):
        res = {}
        for i in self.countries:
            if filter(self.countries[i]):
                res[i] = self.countries[i]
        return res

    def update_country(self, id, atr, value):
        land = self.countries[id]
        if land is None:
            print "There is no country with such id."
        else:
            if atr == self.name:
                land.name = value
            elif atr == self.mainl:
                land.mainl = value
            elif atr == self.currency:
                land.currency = value
            else:
                print "No such field in country."

    def update_city(self, id, atr, value):
        city = self.cities[id]
        if city is None:
            print "There is no city with such id."
        else:
            if atr == self.name:
                city.name = value
            elif atr == self.population:
                city.population = value
            elif atr == self.area:
                city.area = value
            else:
                print "No such field in city."





