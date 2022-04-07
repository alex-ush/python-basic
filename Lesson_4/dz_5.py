from functools import reduce


def f_num(el_1, el_2):
    return el_1 * el_2


numbers = [el for el in range(100, 1001, 2)]

print(numbers)
print(reduce(f_num, numbers))
