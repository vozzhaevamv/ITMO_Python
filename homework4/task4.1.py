file_path = open(r"C:\Users\Masha\Desktop\text.txt", "r")
with open(r"C:\Users\Masha\Desktop\text.txt", "r", encoding="utf-8") as file:
    content = file_path.read()
print("Файл считан:", content)
import re
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, content)
print("Электронные почты:", emails)
numbers = r'(\+?\d{1,3}[-.\s]?)?\(?\d{1,4}?\)?[-.\s]?\d{3}[-.\s]?\d{4}'
numbers1 = re.findall(numbers, content)
print ("Номера телефонов:", numbers1)
output_file_path = open(r"C:\Users\Masha\Desktop\destination.txt", "r")
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for email in emails:
        output_file.write(email_pattern)
    for number in numbers:
        output_file.write(numbers)
with open(output_file_path, "r", encoding="utf-8") as output_file:
    content1 = output_file.read()
print(content1)