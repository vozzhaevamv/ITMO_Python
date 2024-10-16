import re
file_way = r"C:\Users\Masha\Desktop\text.txt"
file = open(file_way, "r", encoding="utf-8")
content = file.read()
file.close()
print("Файл считан:", content)
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, content)
print("Электронные почты:", emails)
numbers = r'(\+?\d{1,3}[-.\s]?)?\(?\d{1,4}?\)?[-.\s]?\d{3}[-.\s]?\d{4}'
numbers1 = re.findall(numbers, content)
print ("Номера телефонов:", numbers1)
file.close()
file_way2 = r"C:\Users\Masha\Desktop\textnew.txt"
file2 = open(file_way2, "w", encoding="utf-8")
file2.write("Электронные почты:")
for email in emails:
        file2.write(email_pattern)
for number in numbers:
        file2.write(numbers)
file2.close()
file2 = open(file_way2, "r", encoding="utf-8")
content2 = file2.read()
file2.close()
print("Файл считан:", content2)
