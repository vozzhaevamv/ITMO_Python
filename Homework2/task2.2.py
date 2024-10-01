persons = [('John', 20), ('Nick', 15), ('Kate', 25),('Stif',19)]
sorted_data_list = sorted((i for i in persons if i[1]>18))
print (sorted_data_list)
