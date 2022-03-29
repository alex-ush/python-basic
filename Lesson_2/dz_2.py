list_2 = list(input('Введите число: '))

print(list_2)

for i in range(1, len(list_2), 2):
    list_2[i - 1], list_2[i] = list_2[i], list_2[i - 1]

print(list_2)
