class LearningCourse:
    def __init__(self, name, length, cost):
        self.name = name  
        self.length = length  
        self.cost = cost  

    def details(self):
        return f"Курс: {self.name}, Продолжительность: {self.length} часов, Стоимость: {self.cost}"

class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand  
        self.model = model  
        self.year = year  

    def details(self):
        return f"Транспортное средство: {self.brand} {self.model}, Год выпуска: {self.year}"
class Automobile(Transport):
    def __init__(self, brand, model, year, license_plate):
        super().__init__(brand, model, year)
        self.license_plate = license_plate  # Номерной знак автомобиля

    def details(self):
        return f"{super().details()}, Номерной знак: {self.license_plate}"

class Teacher:
    def __init__(self, name, experience, field):
        self.name = name  
        self.experience = experience  
        self.field = field  

    def details(self):

        return f"Преподаватель: {self.name}, Стаж: {self.experience} лет, Специализация: {self.field}"


class Learner:
    def __init__(self, name, age, enrolled_course):
        self.name = name  
        self.age = age  
        self.enrolled_course = enrolled_course 

    def details(self):
   
        return f"Студент: {self.name}, Возраст: {self.age}, Записан на курс: {self.enrolled_course.details()}"


if __name__ == "__main__":

    course = LearningCourse("Базовый курс вождения", 20, 30000.00)
    car = Automobile("Renault", "Clio", 2020, "ABC123")
    instructor = Teacher("Олег", 5, "Вождение автомобиля")
    student = Learner("Я", 24, course)

 
    print(course.details())
    print(car.details())
    print(instructor.details())
    print(student.details())
