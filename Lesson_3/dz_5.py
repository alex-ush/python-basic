def sum_cont():
    sum_total = 0
    while True:
        num_list = input('Введите числа через пробел, чтобы выйти введите "q": ').split()
        for num in num_list:
            if num == 'q':
                return sum_total
            else:
                try:
                    sum_total += int(num)
                except ValueError:
                    print('Встречаются буквы, если хотите закончить, введите "q"')
        print(f'Сумма ваших чисел = {sum_total}')


print(sum_cont())
