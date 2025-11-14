from abc import ABC, abstractmethod

class Person(ABC):
    '''Абстрактный класс для людей'''

    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def get_info(self) -> tuple[str, str]:
        return (self.name, self.role)

    @abstractmethod
    def __str__(self) -> str:
        '''Абстрактный метод, который должен быть реализован каждым наследником'''
        pass

class Student(Person):
    def __init__(self, name: str, course: int):
        super().__init__(name=name, role='студент')
        self.course = course
        
    def __str__(self) -> str:
        '''Реализация абстрактного метода для студента'''
        return f'Роль: {self.role}, Имя: {self.name}, Курс: {self.course}.'

class Teacher(Person):
    def __init__(self, name: str, position: str):
        super().__init__(name=name, role='преподаватель')
        self.position = position
    
    def __str__(self) -> str:
        '''Реализация абстрактного метода для преподавателя'''
        return f'Роль: {self.role}, Имя: {self.name}, Должность: {self.position}.'

class DepartmentHead(Person):
    def __init__(self, name: str, department: str, academic_degree: str = ""):
        super().__init__(name=name, role='заведующий кафедрой')
        self.department = department
        self.academic_degree = academic_degree
    
    def __str__(self) -> str:
        '''Реализация абстрактного метода для заведующего кафедрой'''
        degree_info = f", Ученая степень: {self.academic_degree}" if self.academic_degree else ""
        return f'Роль: {self.role}, Имя: {self.name}, Кафедра: {self.department}{degree_info}.'

class Discipline:
    def __init__(self, teacher: Teacher, students: list[Student], name: str, department_head: DepartmentHead = None):
        self.teacher = teacher
        self.students = students
        self.name = name
        self.department_head = department_head

    def __str__(self) -> str:
        students_names = [s.get_info()[0] for s in self.students]
        department_info = f", Зав. кафедрой: {self.department_head.get_info()[0]}" if self.department_head else ""
        return f'Дисциплина: "{self.name}". Преподаватель: {self.teacher.get_info()[0]}. Студенты: ({", ".join(students_names)}){department_info}'

def create_student_from_input(student_input: str) -> Student:
    '''Создает объект Student из строки ввода'''
    parts = student_input.rsplit(' ', 1)
    if len(parts) == 2:
        name, course_str = parts
        try:
            course = int(course_str)
            return Student(name.strip(), course)
        except ValueError:
            raise ValueError(f"Некорректный формат курса: {course_str}")
    else:
        raise ValueError(f"Некорректный формат ввода студента: {student_input}")

def main():
    all_objects = []
    department_heads = []
    
    menu = '''
    1. Создание нового объекта "Discipline".
    2. Вывод всех объектов.
    3. Вывод конкретного объекта.
    4. Создать заведующего кафедрой.
    0. Завершение работы программы.
    '''

    while True:
        print(menu)
        try:
            menu_item = int(input("Введите номер команды: ").strip())
        except ValueError:
            print("Пожалуйста, введите число.")
            continue

        if not (0 <= menu_item <= 4):
            print("Вы ввели неверную команду, попробуйте ещё раз.")
            continue
        
        match menu_item:
            case 0:
                print("Программа завершила свою работу.")
                break

            case 1:
                try:
                    # Ввод данных преподавателя
                    teacher_input = input("Введите ФИО преподавателя и его должность через запятую: ").strip()
                    teacher_parts = teacher_input.split(', ')
                    if len(teacher_parts) != 2:
                        print("Неверный формат ввода преподавателя. Используйте: ФИО, должность")
                        continue
                    
                    teacher_name, teacher_position = teacher_parts
                    
                    # Ввод названия дисциплины
                    discipline_name = input("Введите название дисциплины: ").strip()
                    if not discipline_name:
                        print("Название дисциплины не может быть пустым.")
                        continue
                    
                    # Ввод студентов
                    students_input = input("Введите ФИО студентов и их курс через запятую (например: Иван Иванов 2, Петр Петров 3): ").strip()
                    if not students_input:
                        print("Должен быть указан хотя бы один студент.")
                        continue
                    
                    # Создание объектов студентов
                    student_entries = students_input.split(', ')
                    students_list = []
                    for entry in student_entries:
                        try:
                            student = create_student_from_input(entry)
                            students_list.append(student)
                        except ValueError as e:
                            print(f"Ошибка при создании студента: {e}")
                            continue
                    
                    if not students_list:
                        print("Не удалось создать ни одного студента.")
                        continue
                    
                    # Создание объекта преподавателя
                    teacher_obj = Teacher(teacher_name, teacher_position)
                    
                    # Выбор заведующего кафедрой (опционально)
                    department_head_obj = None
                    if department_heads:
                        print("\nДоступные заведующие кафедрой:")
                        for i, head in enumerate(department_heads):
                            print(f"{i}: {head.name} - {head.department}")
                        
                        add_head = input("Добавить заведующего кафедрой? (y/n): ").strip().lower()
                        if add_head == 'y':
                            try:
                                head_index = int(input("Введите индекс заведующего кафедрой: "))
                                if 0 <= head_index < len(department_heads):
                                    department_head_obj = department_heads[head_index]
                                else:
                                    print("Неверный индекс.")
                            except ValueError:
                                print("Неверный формат индекса.")
                    
                    # Создание объекта дисциплины
                    discipline_obj = Discipline(teacher_obj, students_list, discipline_name, department_head_obj)
                    all_objects.append(discipline_obj)
                    
                    print("Объект успешно создан!")
                    
                except Exception as e:
                    print(f"Произошла ошибка при создании объекта: {e}")
                
                continue

            case 2:
                if not all_objects:
                    print('Нет ни одного созданного объекта. Попробуйте для начала ввести команду 1.')
                    continue
                
                print("Вывод содержимого всех объектов:")
                for i, obj in enumerate(all_objects):
                    print(f"{i}: {obj}")
                    print("-" * 50)
                
                continue

            case 3:
                if not all_objects:
                    print('Нет ни одного созданного объекта.')
                    continue
                    
                try:
                    inx = int(input("Введите индекс интересующего объекта: ").strip())
                except ValueError:
                    print("Пожалуйста, введите число.")
                    continue

                if not (0 <= inx < len(all_objects)):
                    print("Индекс выходит за допустимый диапазон. Попробуйте ещё раз.")
                    continue
                    
                obj = all_objects[inx]
                print(f"\n=== Дисциплина: {obj.name} ===")
                print(f"Преподаватель: {obj.teacher}")
                if obj.department_head:
                    print(f"Заведующий кафедрой: {obj.department_head}")
                print("Студенты:")
                for student in obj.students:
                    print(f"  - {student}")
                print()
                
                continue

            case 4:
                try:
                    name = input("Введите ФИО заведующего кафедрой: ").strip()
                    if not name:
                        print("ФИО не может быть пустым.")
                        continue
                        
                    department = input("Введите название кафедры: ").strip()
                    if not department:
                        print("Название кафедры не может быть пустым.")
                        continue
                        
                    degree = input("Введите ученую степень (если есть, иначе нажмите Enter): ").strip()
                    
                    department_head = DepartmentHead(name, department, degree)
                    department_heads.append(department_head)
                    print(f"Заведующий кафедрой '{department}' успешно создан!")
                    
                except Exception as e:
                    print(f"Ошибка при создании заведующего кафедрой: {e}")
                
                continue
                
if __name__ == "__main__":
    main()