#!/usr/bin/env python
# coding: utf-8

# Урок 2. Задача 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

# In[8]:


n = int(input('Введите количество элементов n:'))
a = 1
sum = 0
i = 0
for i in range(n):
        sum = sum + a
        print(a)
        a = a / -2
        i += 1
print('Сумма элементов ряда =',sum)    


# In[ ]:




