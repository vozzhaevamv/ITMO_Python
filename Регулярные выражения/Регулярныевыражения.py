import re
file_way = r"C:\Users\Masha\Downloads\HP1RUS.TXT"
with open(file_way, "r", encoding="windows-1251") as file:
    content = file.read()
pattern = r'\bГарри\b' # Определяем регулярное выражение для поиска слова "Гарри"
name = re.findall(pattern, content)# Находим все упоминания "Гарри"
count = len(name)# Считаем количество упоминаний 
print("Количество упоминаний 'Гарри':", count)
pattern2 = r'\bХогвартс\b'# Определяем регулярное выражение для "Хогвартс"
_, count_hogwarts_replacements = re.subn(pattern2, 'Итмо', content)# Заменяем все вхождения "Хогвартс" на "Итмо"
print("Количество замен 'Хогвартс' на 'Итмо':", count_hogwarts_replacements)
sentences = re.split(r'(?<=[.!?]) +', content.strip())# Разделяем текст на предложения
print("Количество предложений в тексте:", len(sentences))
found_sentences = []
pattern3 = r'^(Мистер|Миссис)\s+Дарсли' # Определяем регулярное выражение для поиска "Мистер" или "Миссис" перед "Дарсли"
for sentence in sentences:
    if re.search(pattern3, sentence):
        found_sentences.append(sentence.strip())
print("Найденные предложения с 'Мистер' или 'Миссис':")
for sentence in found_sentences:
    print(sentence)
