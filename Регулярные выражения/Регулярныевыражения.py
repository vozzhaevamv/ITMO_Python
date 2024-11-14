import re
file_way = r"C:\Users\Masha\Downloads\HP1RUS.TXT"
with open(file_way, "r", encoding="windows-1251") as file:
    content = file.read()
pattern = r'\bГарри\b'
name = re.findall(pattern, content)
count = len(name)
print("Количество упоминаний 'Гарри':", count)
pattern2 = r'^(Мистер|Миссис)\s+Дарсли'
lines = content.splitlines()
for line in lines:
    if re.match(pattern2, line):
        print("Найдено совпадение:", line)
pattern3 = r'\bХогвартс\b'
_, count_hogwarts_replacements = re.subn(pattern3, 'Итмо', content)
print("Количество замен 'Хогвартс' на 'Итмо':", count_hogwarts_replacements)
sentences = re.split(r'(?<=[.!?]) +', content.strip())
print("Количество предложений в тексте:", len(sentences))
