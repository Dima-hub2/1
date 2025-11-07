class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # метод, который будет переопределяться (полиморфизм)
    def show_info(self):
        return f"Человек: {self.name}, возраст: {self.age}"

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def show_info(self):
        return f"Студент: {self.name}, возраст: {self.age}, курс: {self.course}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        return f"Преподаватель: {self.name}, возраст: {self.age}, предмет: {self.subject}"

class Headofdepartment(Teacher):
    def __init__(self, name, age, subject, department):
        super().__init__(name, age, subject)
        self.department = department

    def show_info(self):
        return (f"Заведующий кафедрой: {self.name}, возраст: {self.age}, "
                f"кафедра: {self.department}, предмет: {self.subject}")


# -------- Главная часть программы --------
people = []  # общий список всех объектов

while True:
    print("\nМЕНЮ:")
    print("1. Добавить объект")
    print("2. Показать все объекты")
    print("3. Продемонстрировать полиморфизм")
    print("4. Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        print("\nКого добавить?")
        print("1. Студента")
        print("2. Преподавателя")
        print("3. Заведующего кафедрой")

        sub = input("Введите номер: ")

        name = input("Введите ФИО: ")
        age = input("Введите возраст: ")

        if sub == "1":
            course = input("Введите курс: ")
            s = Student(name, age, course)
            people.append(s)
            print("Студент добавлен!")

        elif sub == "2":
            subject = input("Введите предмет: ")
            t = Teacher(name, age, subject)
            people.append(t)
            print("Преподаватель добавлен!")

        elif sub == "3":
            subject = input("Введите предмет: ")
            department = input("Введите кафедру: ")
            h = Headofdepartment(name, age, subject, department)
            people.append(h)
            print("Заведующий кафедрой добавлен!")

    elif choice == "2":
        if not people:
            print("Список пуст!")
        else:
            print("\nСписок всех объектов:")
            for p in people:
                print(" -", p.show_info())

    elif choice == "3":
        if not people:
            print("Список пуст!")
        else:
            print("\nПолиморфизм в действии:")
            for p in people:
                # у всех классов метод одинаковый по названию,
                # но работает по-разному — это и есть полиморфизм
                print(p.show_info())

    elif choice == "4":
        print("Программа завершена.")
        break

    else:
        print("Неверный пункт меню!")

