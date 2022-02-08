class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

#Create Object
loc_1 = Location("Wanslou", "Ndjamena")

#Call method from Location class
loc_1.myLocation()

loc_2 = Location("Xing Li", "China")
loc_3 = Location("Malala", "Kapenguria")

loc_2.myLocation()
loc_3.myLocation()

your_loc = Location("Nairobi", "Kenya")
your_loc.myLocation()
# loc = Location("Apocalypto", "Kilgoris")
# print(loc.name)
# print(loc.country)
# print(type(loc))
