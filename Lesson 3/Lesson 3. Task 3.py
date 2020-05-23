#!/usr/bin/env python
# coding: utf-8

# In[177]:


# Урок 3. Задача 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

# Создание массива
from random import randint
a = [randint(1, 100) for _ in range(20)]
print (f'Исходный массив:\n{a}')
min_a = 100
max_a = 0

# Поиск минимумов и максимумов массива и их индексов
for i in range(len(a)):
    if a[i] > max_a:
        max_a = a[i]
print(f'\nМаксимальный элемент массива: {max_a}')

for i in range(len(a)):
    if a[i] < min_a:
        min_a = a[i]
print(f'\nМинимальный элемент массива: {min_a}')

index_min = a.index(min(a))
index_max = a.index(max(a))


# Проверка условия, что в массиве один минимум и один максимум
if a.count(max_a) == 1 & a.count(min_a) == 1:
    if index_min < index_max:
        a.insert(index_max, min_a)
        a.remove(max_a)
        a.insert(index_min, max_a)
        a.remove(min_a)
        print(f'\nИтоговый массив:\n{a}')
    else:
        a.insert(index_min, max_a)
        a.remove(min_a)
        a.insert(index_max, min_a)
        a.remove(max_a)
        print(f'\nИтоговый массив:\n{a}')
elif a.count(min_a) == 1:
    print('\nВ массиве 2 максимальных значения!')
else:
    print('\nВ массиве 2 минимальных значения!')

