import time
import threading


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.count = 100
        self.power = power
        self.timer = 0

    def battle(self):
        while self.count > 0:
            self.count -= self.power
            time.sleep(0.1)
            self.timer += 1
            print(f"{self.name}, сражается {self.timer} день(дня), осталось {self.count} воинов")

    def run(self):
        self.battle()
        print(f"{self.name} одержал победу спустя {self.timer} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
