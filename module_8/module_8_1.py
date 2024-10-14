
def add_everything_up(par1, par2):
    try:
        res = par1 + par2
    except TypeError:
        res = str(par1) + str(par2)
    finally:
        return res
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
