# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random
import operator

# генерация случайного массива
array = [round(random.uniform(0, 49), 2) for _ in range(10)]
print(array)

# функция сортировки слиянием
def merge_sort(array, compare=operator.lt):
    if len(array) < 2:
        return array[:]
    else:
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle], compare)
        right = merge_sort(array[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

print(merge_sort(array))