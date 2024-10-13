from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

    def __contains__(self, product):
        if isinstance(product, Product):
            return self.name == product.name
        if isinstance(product, str):
            return self.__str__ == product



class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()

    def add(self, *products):
        add_products = []
        file = open(self.__file_name, 'r')
        content = str(file.read())
        file.close()
        for product in products:
            if str(product) not in content and product not in add_products:
                add_products.append(product)
            else:
                print(f"Продукт {str(product)} уже есть в магазине")
        if len(add_products) >= 0:
            file = open(self.__file_name, 'a')
            for product in add_products:
                file.write(f'{str(product)} \n')
            file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())



