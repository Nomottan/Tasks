def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        prime = "Простое"
        for x in range(2, res//2):
            if not res % x:
                prime = "Составное"
        print(prime)
        return res
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
