#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Урок 3. Задача 5. В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». 
# Это два абсолютно разных значения

# Создание массива
from random import randint
a = [randint(-100, 100) for _ in range(100)]
print (f'Исходный массив:\n{a}')
max_b = -100
b = []

# Создание массива из отрицательных чисел
for i in range(len(a)):
    if a[i] < 0:
        b.append(a[i])
print(f'\nМассив из отрицательных элементов массива а:\n{b}')

# Поиск максимального из отрицательных элементов
for i in range(len(b)):
    if b[i] > max_b:
        max_b = b[i]
print(f'\nМаксимальный отрицательный элемент массива: {max_b}')
print(f'\nИндекс максимального отрицательного: {b.index(max_b)}')

