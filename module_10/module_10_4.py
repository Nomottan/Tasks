from threading import Thread
from queue import Queue
from random import randint
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def __run__(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self._queue = Queue()
        self.tables = []
        for table in tables:
            self.tables.append(table)
        self.vacancy_table = True

    def guest_arrival(self, *guests):
        for guest in guests:
            if self.vacancy_table:
                for table in self.tables:
                    if not table.guest:
                        table.guest = guest
                        print(f"{guest.name} сел(-а) за стол номер {table.number}")
                        table.guest.start()
                        self.vacancy_table = True
                        break
                    else:
                        self.vacancy_table = False
            else:
                self._queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.vacancy_table and not self._queue.empty():
            for table in self.tables:
                if table.guest:
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушел(ушла)")
                        table.guest = None
                        if not self._queue.empty():
                            table.guest = self._queue.get()
                            print(f"{table.guest.name} сел(-а) за стол номер {table.number}")
                            table.guest.start()
                        else:
                            self.vacancy_table = True
                            print(f"Стол номер {table.number} свободен")

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()