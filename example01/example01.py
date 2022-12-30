# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

import random


k = int(input('Введите степень к:'))

equation ={}

for i in range(k, -1, -1):
    equation[i] = random.randint(0, 100)
print(equation)

eq_str = ''
for k, v in equation.items():
    if k == 1:
      eq_str += f'{v}*x + '
    elif k == 0:
      eq_str += f'{v} + '
    elif v == 1:
      eq_str += f'x**{k} + '
    elif v == 0:
      eq_str += f''
    else:
      eq_str += f'{v}*x**{k} + '
else:
  eq_str = eq_str[:-3]
eq_str = eq_str + ' = 0'

print(eq_str)


data = open('first.txt', 'w')
data.writelines(eq_str)
data.close()