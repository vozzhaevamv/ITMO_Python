def analyze_text_file(filename):
    line_count = 0  
    word_count = 0  
    char_count = 0  
    longest_word = ''  

    file = open(filename, 'r', encoding='utf-8')  

    for line in file:
        line_count += 1  # Увеличиваем счетчик строк
        char_count += len(line)  # Увеличиваем счетчик символов 
        words = line.split()  # Разделяем строку на слова
        word_count += len(words)  # Увеличиваем счетчик слов на количество слов в строке
        for word in words:
            if len(word) > len(longest_word):  
                longest_word = word  
    return line_count, word_count, char_count, longest_word              
filename = r"C:\Users\Masha\Desktop\ДЗ\task4\test.txt"
line_count, word_count, char_count, longest_word = analyze_text_file(filename)
print(f'Количество строк: {line_count}')
print(f'Количество слов: {word_count}')
print(f'Количество символов: {char_count}')
print(f'Самое длинное слово: {longest_word}')