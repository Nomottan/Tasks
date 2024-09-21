class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = int(num_of_floors)
    def go_to (self, new_floor):
        num_of_floors = int(self.num_of_floors)
        if new_floor > num_of_floors:
            print (f"Этаж {new_floor} в здании {self.name} не существует")
            return
        for f in range(1, new_floor):
            if f == 0:
                continue
            print(f)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)