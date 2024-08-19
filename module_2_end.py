import random

number = random.randrange(3,21)
print(number)
protopassword = []
password = []
for i in range(1, number): #
    for j in range(1, i):
        if i == j:
            break
        if number % (i + j) == 0:
            protopassword.append([j, i])
protopassword.sort()
for i in range(0, len(protopassword)): # раскрытие вложенных списков
    password.append(protopassword[i][0])
    password.append(protopassword[i][1])
strpassword = ''
for i in range(0, len(password)):
    strpassword += str(password[i])
print(strpassword)
