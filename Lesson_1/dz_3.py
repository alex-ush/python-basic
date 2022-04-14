# первый вариант
number = input('Введите любое число от 1 до 9: ')
sum_number = int(number) + int(number + number) + int(number + number + number)
print(sum_number)

# еще один способ решения задачи
number_int = int(number)
sum_number = number_int + number_int * 11 + number_int * 111
print(sum_number)
