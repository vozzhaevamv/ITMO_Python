def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 
n = int(input("Введите целое число: "))
if is_prime(n):
    print("Простое число:", n)
else:
    print("Не является простым числом:", n)