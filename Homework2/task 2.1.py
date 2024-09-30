list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list_all=[]
for i in list1:
    list_all.append (list1[i-1])
    list_all.append (list2[i-1])
print(list_all)
