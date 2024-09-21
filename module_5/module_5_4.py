class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

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

    def go_to(self, new_floor):
        num_of_floors = int(self.num_of_floors)
        if new_floor > num_of_floors:
            print (f"Этаж {new_floor} в здании {self.name} не существует")
            return
        for f in range(1, new_floor+1):
            print(f)

    def __del__(self):
        print(f"{self.name} снесен, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)