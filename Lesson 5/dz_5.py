with open('text_5.txt', 'w', encoding='utf-8') as numbers: # можно было w+
    my_nums = input('Введите несколько чисел через пробел: ')
    numbers.write(str(my_nums))

with open('text_5.txt', 'r', encoding='utf-8') as numbers:
    sum_num = numbers.readline().split()
    sum = 0
    for i in sum_num:
        if i.isdigit():
            sum += int(i)
    print(sum)
