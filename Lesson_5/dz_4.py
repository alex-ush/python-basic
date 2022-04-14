trans_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('text_4_trans.txt', 'w', encoding='utf-8') as file_t:
    with open('text_4.txt', 'r', encoding='utf-8') as file_o:
        file_t.writelines([line.replace(line.split()[0], trans_dict.get(line.split()[0])) for line in file_o])
