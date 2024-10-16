letters = 'abcdefghijklmnopqrstuvwxyz'
letters2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
characters = r'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
all_characters = letters+letters2+digits+characters
length = int(input("Введите желаемое количество случайных символов: "))
import random
random_characters = ''.join(random.choices(all_characters, x=length))
print(f"Случайные символы: {random_characters}")