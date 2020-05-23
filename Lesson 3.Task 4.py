#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Урок 3. Задача 4. Определить, какое число в массиве встречается чаще всего

# Создание массива
from random import randint
a = [randint(1, 100) for _ in range(100)]
print (f'Исходный массив:\n{a}')
count = 0

# Поиск повторяющегося элемента
for i in range(len(a)):
    if a.count(a[i]) > count:
        count = a.count(a[i])
        elem = a[i]
       
# Проверка условия, что в массиве есть повторяющиеся элементы
if count > 1:
    print(f'Наиболее часто встречающийся элемент в массиве: {elem}\nКоличество повторений: {count}')
else:
    print('В исходном массиве нет повторяющихся элементов')

