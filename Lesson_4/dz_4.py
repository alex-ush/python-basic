from random import randint


numbers = [randint(1, 15) for _ in range(20)]
uniq_num = [el for el in numbers if numbers.count(el) == 1]

print(numbers)
print(uniq_num)

# оптимизация - разобрать!
num_dic = {i: 0 for i in numbers}

for i in numbers:
    num_dic[i] += 1

print([i for i in num_dic if num_dic[i] == 1])
