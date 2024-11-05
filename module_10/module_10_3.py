import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance =0
        self.lock = threading.Lock()

    def deposit(self):
        count = 0
        while count != 100:
            dep = randint(50, 500)
            self.balance += dep
            print(f"Пополнение: {dep}.Баланс:{self.balance}")
            count += 1
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        count = 0
        while count != 100:
            tak = randint(50, 500)
            if tak <= self.balance:
                self.balance -= tak
                print(f"Снятие {tak}.Баланс:{self.balance}")
            else:
                self.lock.acquire()
            sleep(0.001)
            count += 1



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()


print(f'Итоговый баланс: {bk.balance}')
