class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def get_info(self):
        return (self.name, self.role)
    def __str__(self):
        pass  # будет переопределяться

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name, 'студент')
        self.course = course
    def __str__(self):
        return f'Роль: {self.role}, Имя {self.name}, Курс: {self.course}.'

class Teacher(Person):
    def __init__(self, name, position):
        super().__init__(name, 'преподаватель')
        self.position = position
    def __str__(self):
        return f'Роль: {self.role}, Имя {self.name}, Позиция: {self.position}.'

class HeadOfDepartment(Person):
    def __init__(self, name, department):
        super().__init__(name, 'заведующий кафедрой')
        self.department = department
    def __str__(self):
        return f'Роль: {self.role}, Имя {self.name}, Кафедра: {self.department}.'

class Discipline:
    def __init__(self, teacher, students, name, head=None):
        self.teacher = teacher
        self.students = students
        self.name = name
        self.head = head
    def __str__(self):
        s = [st.name for st in self.students]
        h = f' (зав. {self.head.name})' if self.head else ''
        return f'Дисциплина: "{self.name}". Преподаватель: {self.teacher.name}{h}. Студенты: ({", ".join(s)})'

def main():
    all_objects = []
    menu = '''
    1. Создание нового объекта "Discipline".
    2. Вывод объектов.
    3. Вывод конкретного объекта.
    0. Завершение работы программы.
    '''
    while True:
        print(menu)
        choice = input("Введите номер команды: ").strip()
        if choice not in ['0','1','2','3']:
            print("Неверная команда!")
            continue

        if choice == '0':
            print("Программа завершена.")
            break

        if choice == '1':
            teacher_input = input("ФИО преподавателя и должность через запятую: ").strip().split(', ')
            discipline_name = input("Дисциплина: ").strip()
            students_input = input("ФИО студентов и курс через запятую (Иванов 3, Петров 2): ").strip().split(', ')
            head_input = input("ФИО зав. кафедрой и название кафедры (или пусто): ").strip()

            # студенты
            students = []
            for s in students_input:
                if s:
                    name = s[:-2].strip()
                    course = int(s[-1])
                    students.append(Student(name, course))

            # преподаватель
            teacher = Teacher(teacher_input[0].strip(), teacher_input[1].strip())

            # зав. кафедрой (если указан)
            head = None
            if head_input:
                parts = head_input.split(', ')
                head = HeadOfDepartment(parts[0].strip(), parts[1].strip())

            disc = Discipline(teacher, students, discipline_name, head)
            all_objects.append(disc)
            print("Объект создан!")

        elif choice == '2':
            if not all_objects:
                print("Нет объектов.")
            else:
                print("Все дисциплины:")
                for obj in all_objects:
                    print(obj)

        elif choice == '3':
            if not all_objects:
                print("Нет объектов.")
                continue
            idx = int(input("Индекс объекта: ").strip())
            if 0 <= idx < len(all_objects):
                print("\nПодробно:")
                print(f'Название: {all_objects[idx].name}')
                print(f'Преподаватель: {all_objects[idx].teacher}')
                if all_objects[idx].head:
                    print(f'Зав. кафедрой: {all_objects[idx].head}')
                print("Студенты:")
                for s in all_objects[idx].students:
                    print(s)
            else:
                print("Неверный индекс!")

if __name__ == "__main__":
    main()