#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Урок 3. Задача 6. В одномерном массиве найти сумму элементов, 
# находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.

# Создание массива
from random import randint
a = [randint(0, 10) for _ in range(10)]
print (f'Исходный массив:\n{a}')
min_a = 100
max_a = 0
b = []
sum = 0

# Поиск минимумов и максимумов массива
for i in range(len(a)):
    if a[i] > max_a:
        max_a = a[i]
print(f'\nМаксимальный элемент массива: {max_a}')

for i in range(len(a)):
    if a[i] < min_a:
        min_a = a[i]
print(f'\nМинимальный элемент массива: {min_a}')

# Проверка условия, что в массиве не повторяются экстремумы
if a.count(max_a) == 1 & a.count(min_a) == 1:
    if a.index(min_a) < a.index(max_a):
        for i in range(a.index(min_a),a.index(max_a)):
            sum = sum + a[i]
        print(f'\nСумма элементов массива между минимальным и максимальным элементами: {sum - min_a}')
    else:
        for i in range(a.index(max_a),a.index(min_a)):
            sum = sum + a[i]
        print(f'\nСумма элементов массива между минимальным и максимальным элементами: {sum - max_a}')
elif a.count(min_a) == 1:
    print('\nВ массиве 2 максимальных значения!')
else:
    print('\nВ массиве 2 минимальных значения!')

