my_dict = {'a': 1, 'b': 2, 'c': 3}
dict2 = {}
for char, num in my_dict.items(): # Проходим по элементам исходного словаря
    dict2[num] = char # В новом словаре ключом будет число, а значением - буква
print(dict2)
