#Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. 
#Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

sum_lim = 4000001
fib_list = [1, 2]
result = []
v = 0
w = 1

while fib_list[w] < sum_lim:
    j = fib_list[v] + fib_list[w]
    fib_list.append(j)
    v += 1
    w += 1
for k in fib_list:
  if k % 2 == 0:
    result.append(k) 
print(sum(result))