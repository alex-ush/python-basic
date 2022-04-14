numbers = int(input('Введите любое число, а я найду в нем самую большую цифру: '))
input_numbers = numbers
max_number = 0

while numbers > 0:
    step_number = numbers % 10
    if step_number > max_number:
        max_number = step_number
    numbers = numbers // 10

print(f'В вашем числе {input_numbers} самая большая цифра {max_number}')
