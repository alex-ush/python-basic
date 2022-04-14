# простой способ
def simple(num_1, num_2):
    s_result = num_1 ** num_2
    return round(s_result, 7)


print(simple(7.3, -2))


# без **
def hard(num_1, num_2):
    h_result = 1
    for num in range(abs(num_2)):
        h_result /= num_1
    return round(h_result, 7)


print(hard(7.3, -2))
