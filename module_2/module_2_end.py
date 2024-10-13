import random

number = random.randrange(3, 21)
protopassword = []
password = ''

for i in range(1, number):  #
    for j in range(1, i):
        if i == j:
            break
        if number % (i + j) == 0:
            protopassword.append([j, i])

protopassword.sort()

for i in range(0, len(protopassword)):  # раскрытие вложенных списков
    password += str(protopassword[i][0])
    password += str(protopassword[i][1])

print(password)
