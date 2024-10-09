start = int(input("Введите начало списка чисел: "))
end = int(input("Введите конец списка чисел: "))
list1 = list(range(start, end))# Генерируем последовательность чисел в диапозоне от Start до End
print("Список чисел:", list1)
cubed_list1 = list(map(lambda x: x ** 3, list1)) # используем функцию map для возведения каждого числа в 3 степень
print("Список чисел, возведённых в третью степень (с использованием map):", cubed_list1)
cubed_list2 = [ number ** 3 for number in list1]
print("Ещё список чисел, возведённых в третью степень (с использованием списка):",cubed_list2)
def cub(start, end):
		return [x ** 3 for x in range(start, end)]
cubed_list3 = cub(start, end)
print("Список чисел, возведённых в третью степень (с использованием функции):",cubed_list3)
even_list = list(filter(lambda x: x % 2 == 0, cubed_list1))
print("Четные числа из списка, возведённые в третью степень:",even_list)
from functools import reduce 
product_numbers = reduce(lambda x, y: x*y, even_list) 
print("Произведение всех элементов получившегося в п.2 списка",product_numbers)