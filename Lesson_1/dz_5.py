revenue = int(input('Какую выручку получила ваша фирма в прошлом квартале? '))
expenses = int(input('Теперь напишите сумму всех издержек: '))

profit = revenue - expenses

if profit > 0:
    print('Отлично, вы заработали {}'.format(profit))
    print('Ваша рентабельность составила:', round(profit / revenue * 100, 2), '%')
    staff = int(input('Сколько человек работает в вашей компании? '))
    staff_profit = round(profit / staff)
    print('В прошлом квартале вы заработали {} на каждого сотрудника'.format(staff_profit))
elif profit == 0:
    print('Ноль - это отлично! В следующем квартале выйдете в плюс!')
else:
    print('что-то пошло не так, у вас убыток {}'.format(profit))
