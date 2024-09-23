my_list = []
while True:
    x = int(input('Введите любое целое число, чтобы закончить ввод данных, наберите "-1": '))
    if x == -1:
            print('Ввод данных закончен. Перейдем к обработке списка')
            break
    my_list.append(x)
print('Список:', my_list)
list_length = len(my_list)
print('Длина списка', list_length)
sum_loop = 0
for num in my_list:
    sum_loop += num
print('Сумма элементов через цикл:', sum_loop)
sum_method = sum(my_list)
print('Сумма элементов через метод sum():', sum_method)
print("Четные элементы списка:")
for num in my_list:
    if num %2 == 0:
        print(num)