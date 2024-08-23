calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    list_to = (len(string), string.upper(), string.lower())
    return list_to


def is_contains(string, list_to_search):
    count_calls()
    for elems in list_to_search:
        if string.upper() == elems.upper():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
