#!/usr/bin/env python
# coding: utf-8

# Урок 1. Задача 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# In[17]:


a = input('Введите первую букву: ')
b = input('Введите вторую букву: ')
print ('Место буквы', a, 'в алфавите =', ord(a)-64)
print ('Место буквы', b, 'в алфавите =', ord(b)-64)
print ('Между', a, 'и', b, '-', abs(ord(a)-ord(b)), 'букв')
