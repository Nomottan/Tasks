class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.edible == other



class Mammal(Animal):
    def eat(self, food):
        if food == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
class Predator(Animal):
    def eat(self, food):
        if food == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
