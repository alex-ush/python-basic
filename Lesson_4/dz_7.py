def fact_func(number):
    f_num = 1
    for i in range(1, number + 1):
        yield f'{i} = {f_num}'
        f_num *= i + 1


for el in fact_func(int(input('Факториал какого числа вы хотите вычислить? '))):
    print(el)
