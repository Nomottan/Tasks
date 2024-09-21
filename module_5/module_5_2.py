class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = int(num_of_floors)

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return self.name

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
