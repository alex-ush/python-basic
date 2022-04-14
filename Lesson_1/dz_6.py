now = int(input('Сколько бегаете сейчас? '))
aim = int(input('Сколько хотите пробегать? '))
days = 1

print(f'{days}-й день: {now}')

while now < aim:
    now *= 1.1 #тоже самое, что now = now + now * 0.1
    days += 1
    print(f'{days}-й день: {now:0.2f}')

print(f'Чтобы пробежать {aim} киллометров вам потребуется еще {days} дней тренировок')