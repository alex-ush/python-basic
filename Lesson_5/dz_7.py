import json

with open('text_7_json.json', 'w', encoding='utf-8') as result_j, open('text_7.txt', 'r', encoding='utf-8') as raw_data:
    profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in raw_data}
    # print(profit)
    result = [profit, {
        'Средняя прибыль': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                 len([int(i) for i in profit.values() if int(i) > 0]))
    }]
    # print(result)
    json.dump(result, result_j, ensure_ascii=False, indent=2)
