list_5 = [9, 7, 5, 3, 3, 2, 1]
add_next = ''
print(f' У нас есть вот такой список: {list_5}')

while add_next != 'no':
    index = 0
    new_number = int(input('Какое число вы хотите добить в список? '))

    for number in list_5:
        if new_number <= number:
            index += 1
        else:
            list_5.insert(index, new_number)
            break
    print(f'Готово: {list_5}')
    add_next = input('Если хотите добавить еще одно число нажмите Enter, если нет, введите no: ')
print('Ок, закончили')
