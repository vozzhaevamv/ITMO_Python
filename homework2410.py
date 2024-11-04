my_list = ['tree', 'mountain', 'river', 'cloud', 'book', 'chair', 'light', 'window', 'phone', 'mirror', 'sky', 'dream', 'road', 'smile', 'shadow']
word_weights = []
def function(word):
    return sum(ord(char) for char in word)
word_weights = []
for word in my_list:
    weight = function(word)
    word_weights.append((word, weight))
word_weights_sorted = sorted(word_weights, key=lambda item: item[1])
print(word_weights_sorted)
user_word = input("Введите слово для поиска: ")
user_weight = function(user_word)

weights_only = [weight for word, weight in word_weights_sorted]
low = 0
high = len(weights_only) - 1
found = False
index = -1

while low <= high:
    mid = (low + high) // 2
    if weights_only[mid] == user_weight:
        found = True
        index = mid
        break
    elif weights_only[mid] < user_weight:
        low = mid + 1
    else:
        high = mid - 1

if found:
    word = word_weights_sorted[index][0]  # Получаем слово по индексу
    print(f"Слово '{word}' найдено с весом {user_weight} на индексе {index}.")
else:
    print("Слово не найдено.")