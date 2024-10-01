my_dict = {'a': 1, 'b': 2, 'c': 3}
dict2 = {}
for char, num in my_dict.items():
    dict2[num] = char
print(dict2)