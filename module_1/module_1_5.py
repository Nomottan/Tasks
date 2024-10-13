#Задача 1
immutable_var = 1, "один", True
print(immutable_var)

#Задача 2
#immutable_var[0]=2
#нельзя, потому что тип данных не предусмотренный к изменению подобно списку

#Задача 3
mutable_list = [1, "один", True]
mutable_list[1] = "Один"
print(mutable_list)