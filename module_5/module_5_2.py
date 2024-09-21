class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = int(num_of_floors)

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return self.name

    def go_to(self, new_floor):
        num_of_floors = int(self.num_of_floors)
        if new_floor > num_of_floors:
            print (f"Этаж {new_floor} в здании {self.name} не существует")
            return
        for f in range(1, new_floor+1):
            print(f)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))