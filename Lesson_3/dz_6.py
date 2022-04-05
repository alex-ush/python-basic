def some_f():
    for word in input('Введите несколько слов через пробел: ').split():
        letters = 0
        for letter in word:
            if 97 <= ord(letter) <= 122:
                letters += 1
        if letters == len(word):
            print(word.title())
        else:
            print(f'В слове {word} - есть заглавные буквы, используйте только маленькие буквы')


some_f()
