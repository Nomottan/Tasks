class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = int(num_of_floors)

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.num_of_floors == other.num_of_floors

    def __lt__(self, other):
        return self.num_of_floors < other.num_of_floors

    def __le__(self, other):
        return self.num_of_floors <= other.num_of_floors

    def __gt__(self, other):
        return self.num_of_floors > other.num_of_floors

    def __ge__(self, other):
        return self.num_of_floors >= other.num_of_floors

    def __ne__(self, other):
        return self.num_of_floors != other.num_of_floors

    def __add__(self, value):
        self.num_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1.name, h1.num_of_floors)
print(h2.name, h2.num_of_floors)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1.name, h1.num_of_floors)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1.name, h1.num_of_floors)

h2 = 10 + h2 # __radd__
print(h2.name, h2.num_of_floors)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
