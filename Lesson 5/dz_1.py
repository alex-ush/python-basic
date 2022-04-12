with open('text_1.txt', 'a', encoding='utf-8') as my_file:
    while True:
        add_text = input('Что хотите записать в файл? Введите "q", чтобы закончить ')
        if add_text != 'q':
            print(add_text, file=my_file)
        else:
            print('Ок, закончили')
            break
