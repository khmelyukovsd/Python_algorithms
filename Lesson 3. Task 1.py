#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Урок 1 Задача 1. В диапазоне натуральных чисел от 2 до 99 определить, 
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов
    
b = dict.fromkeys(range(2, 10), 0)
n = 0
for key, value in divs.items():
    for a in range(2, 100):
        if a % key == 0:
            b[key] += 1
    print (f'Количество чисел, кратных {key}: {b[key]}')        

