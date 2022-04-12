with open('text_6.txt', 'r', encoding='utf-8') as raw_data:
    first = raw_data.readlines()
    # print(first)
    for el in first:
        second = ''.join((i if i in '0123456789' else ' ') for i in el)
        # print(second)
        third = [int(i) for i in second.split()]
        # print(third)
        print(f'{el.split()[0]} {sum(third)}')
