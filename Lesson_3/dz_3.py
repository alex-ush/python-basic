def max_num(num_1, num_2, num_3):
    mn_list = [num_1, num_2, num_3]
    mn_list.remove(min(mn_list))
    return sum(mn_list)


print(max_num(int(input('Введите первое число: ')),
              int(input('Введите второе число: ')),
              int(input('Введите третье число: '))))
