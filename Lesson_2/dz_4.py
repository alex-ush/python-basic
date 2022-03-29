words = input('Введите несколько слов через пробел: ').split()

for index, word in enumerate(words, 1):
    print(f'{index}) {word[:10]}')
