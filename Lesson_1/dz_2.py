time = int(input('Введите любое количество секунда, а я переведу в чч:мм:сс! '))

hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = (time - hours * 3600) % 60

print(f'{time} секунд - это {hours}:{minutes}:{seconds}')
