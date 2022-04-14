with open('text_1.txt', 'r', encoding='utf-8') as my_file_2:
    num_string = 0
    count = my_file_2.readlines()
    for index, value in enumerate(count, 1):
        num_words = len(value.split())
        num_string += 1
        print(f'В строке {index} слов: {num_words}')
    print(f'Всего строк в файле: {num_string}')
