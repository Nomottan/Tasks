class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=None):
        self.start = start
        self.stop = stop
        if step is None:
            if self.stop > self.start:
                self.step = 1
            else:
                self.step = -1
        else:
            self.step = step
        self.pointer = start
        if self.stop > self.start and self.step <= 0:
            raise StepValueError
        if self.stop < self.start and self.step >= 0:
            raise StepValueError


    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        if self.pointer > self.stop > self.start:
            raise StopIteration
        if self.pointer < self.stop < self.start:
            raise StopIteration
        return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

