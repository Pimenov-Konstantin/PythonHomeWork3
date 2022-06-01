# 1. Найти НОК двух чисел
print('')
print('Task 1')
number_a = 10
number_b = 25

def nok(a, b):
    n = min(a,b)
    if n == 0: return ('Не верно')
    n = max(a,b)
    while True:
        if n%a == 0 and n%b == 0:
            return n
        n += 1

print(f'Для чисел {number_a} и {number_b} НОК = {nok(number_a, number_b)}')
print('')

# 2. Вычислить число ПИ c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.
print('Task 2')
def number_pi(d):
    nomer = 1
    pi = 0
    el = 1
    while el >= d:
        el = 1/(2*nomer -1)
        if nomer%2 == 0: pi -= el
        else: pi += el
        nomer += 1
    pi *= 4
    return (pi)

print(number_pi(0.001))
print('')

# 4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
print('Task 4')
list_vhod = [1, 2, 3, 5, 1, 5, 3, 10]
print(f'Входящий список {list_vhod}')
i = len(list_vhod)-1
while i >= 0:
    if list_vhod.count(list_vhod[i]) > 1:
        list_vhod.pop(i)
    i -= 1
print(f' Результат {list_vhod}')
print('')