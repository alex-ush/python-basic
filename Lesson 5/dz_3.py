from statistics import mean

with open('text_3.txt', 'r', encoding='utf-8') as salary:
    salary_dict = {line.split()[0]: float(line.split()[1]) for line in salary}
    print(f'Средняя заработная плата всех сотрудников: {round(mean(salary_dict.values()), 2)}')
    print(f'Заработали менее 20 т.р.: {[i[0] for i in salary_dict.items() if i[1] < 20000]}')
