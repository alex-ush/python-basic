from random import randint


numbers = []
for i in range(15):
    numbers.append(randint(1, 150))
# можно было записать вот так numbers = [randint(1, 150) for _ in range(15)]

greatest = [numbers[num] for num in range(1, len(numbers)) if numbers[num] > numbers[num - 1]]

print(numbers)
print(greatest)
