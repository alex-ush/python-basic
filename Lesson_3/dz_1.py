def div(num1, num2):
    try:
        num_div = num1 / num2
    except ZeroDivisionError:
        return 'Разделить на ноль не получится!'
    return round(num_div, 2)


print(div(int(input('Введите первое число: ')), int(input('Введите второе число: '))))
