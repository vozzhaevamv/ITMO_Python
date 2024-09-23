my_list = [x for x in range(1, 60, 2)]
print(my_list)
numbers = [x for x in my_list if (x % 3 == 0 or x % 5 == 0) and x % 15 != 0]
print(' Числа, делящиеся на 3 или на 5 и при этом не делящиеся на 15:',numbers)
print('Последний элемент созданного списка',numbers[-1])