def max_in_lyst(my_lyst):
    result = my_lyst[0]
    for elem in (my_lyst):
        if result < elem:
            result = elem
    return result


def count_chet(my_lyst):
    count = 0
    for elem in my_lyst:
        if elem % 2 == 0:
            count += 1
    return count


def uniq_lyst(my_lyst):
    uniq = []
    for elem in my_lyst:
        if elem not in uniq:
            uniq.append(elem)
    return uniq

my_lyst = [4, 2, 4, 1, 3, 7, 19, 8, 3]

print(max_in_lyst(my_lyst))
print(count_chet(my_lyst))
print(uniq_lyst(my_lyst))
