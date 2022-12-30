# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('first.txt', 'r', encoding= 'utf-8') as text:
    equation1 = text.readline()
with open('second.txt', 'r',  encoding= 'utf-8') as text:
    equation2 = text.readline()

print(equation1)
print(equation2)

my_dict1 = {}
equation1 = equation1.replace(' + ', ' ').replace('*x ', '*x**1 ').replace(' = 0', '')

equation1 = equation1.split()
equation1[-1] = equation1[-1] + '*x**0'
for i in range(len(equation1)):
   equation1[i] = equation1[i].split('*x**')
   my_dict1[int(equation1[i][1])] = int(equation1[i][0])

print(my_dict1)

my_dict2 = {}
equation2 = equation2.replace(' + ', ' ').replace('*x ', '*x**1 ').replace(' = 0', '')

equation2 = equation2.split()
equation2[-1] = equation2[-1] + '*x**0'
for i in range(len(equation2)):
   equation2[i] = equation2[i].split('*x**')
   my_dict2[int(equation2[i][1])] = int(equation2[i][0])

print(my_dict2)

my_dict3 = {}
maximum = (max(max(my_dict1), max(my_dict2)))
for i in range(maximum, -1, -1):
    first = my_dict1.get(i)
    second = my_dict2.get(i)
    if first !=None or second != None:
        my_dict3[i] = (first if first != None else 0) + (second if second != None else 0)

print(my_dict3)

eq_str = ''
for k, v in my_dict3.items():
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
data = open('file3.txt', 'w')
data.writelines(eq_str)
data.close()