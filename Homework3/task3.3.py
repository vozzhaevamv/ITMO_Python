def cube(x):
    return x ** 3
numbers = [1, 2, 3,]
def own_map(func, numbers):
    result = []
    for x in numbers:
        result.append(func(x))
    return result
result = own_map(cube,numbers)
print(result)