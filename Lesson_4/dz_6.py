from itertools import count, cycle

for num in count(3):
    if num > 10:
        break
    else:
        print(num)

с = 0
for el in cycle(['learn', 'python']):
    if с > 5:
        break
    print(el)
    с += 1

my_count = count(7)
my_cycle = cycle('ABC')

for _ in range(5):
    print('(my_count, my_cycle) = ({},{})'.format(next(my_count), next(my_cycle)))
