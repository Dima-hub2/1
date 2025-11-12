class Person:
    '''Абстрактный класс для людей'''
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
    def get_info(self) -> tuple[str, str]:
        return (self.name, self.role)
    def __str__(self) -> str:
        '''Метод который должен быть переопределён каждым наследником'''
        pass

class Student(Person):
    def __init__(self, name: str, course: int):
        super().__init__(name=name, role='студент')
        self.course = course
       
    def __str__(self) -> str:
        '''Реализация абстрактого метода для студента'''
        return f'Роль: {self.role}, Имя {self.name}, Курс: {self.course}.'
  
class Teacher(Person):
    def __init__(self, name: str, position: str):
        super().__init__(name=name, role='преподаватель')
        self.position = position
   
    def __str__(self) -> str:
        '''Реализация абстракция метода для преподавателя'''
        return f'Роль: {self.role}, Имя {self.name}, Позиция: {self.position}.'

class HeadOfDepartment(Teacher):
    def __init__(self, name: str, department: str):
        super().__init__(name=name, position='заведующий кафедрой')
        self.department = department
   
    def __str__(self) -> str:
        return f'Роль: {self.role}, Имя {self.name}, Кафедра: {self.department}.'

class Discipline:
    def __init__(self, teacher: Teacher, students: list[Student], name: str):
        self.teacher = teacher
        self.students = students
        self.name = name
    def __str__(self) -> str:
        students = [s.get_info()[0] for s in self.students]
        return f'Дисциплина: "{self.name}". Преподаватель: {self.teacher.get_info()[0]}. Студенты: ({", ".join(students)})'

   
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
        menu_item = int(input("Введите номер команды: ").strip())
        if not (0 <= menu_item <= 3):
            print("Вы ввели неверную команду, попробуйте ещё раз.")
            continue
       
        match menu_item:
            case 0:
                print("Программа завершила свою работу.")
                break
            case 1:
                teacher_input = input("Введите ФИО преподавателя и его должность через запятую: ").strip()
                if ', ' not in teacher_input:
                    print("Неверный формат. Пример: Иванов И.И., доцент")
                    continue
                teacher_data = teacher_input.split(', ')
                name_teacher = teacher_data[0]
                position = teacher_data[1]

                # Поддержка заведующего кафедрой
                if position.lower() == 'заведующий кафедрой':
                    department = input("Введите название кафедры: ").strip()
                    teacher = HeadOfDepartment(name_teacher, department)
                else:
                    teacher = Teacher(name_teacher, position)

                discipline = input("Введите Дисциплину: ").strip()
                students_input = input("ФИО студентов и их курс через запятую (Иванов И.И. 3, Петров П.П. 2): ").strip()
                
                if not students_input:
                    print("Должен быть указан хотя бы один студент. Попробуйте ещё раз.")
                    continue
                
                raw_students = students_input.split(', ')
                students = []
                for s in raw_students:
                    parts = s.rsplit(' ', 1)
                    if len(parts) != 2:
                        print(f"Неверный формат студента: {s}")
                        continue
                    name = parts[0]
                    course = int(parts[1])
                    students.append(Student(name, course))
                
                if len(students) == 0:
                    print("Не удалось создать ни одного студента.")
                    continue
                
                discipline_obj = Discipline(teacher, students, discipline)
                all_objects.append(discipline_obj)
                print("Объект успешно создан!")
                continue
            case 2:
                if len(all_objects) == 0:
                    print('Нет ни одного созданного объекта. Попробуйте для начала ввести команду 1.')
                    continue
               
                print("Вывод содержимого всех объектов.")
                for obj in all_objects:
                    print(obj)
               
                continue
            case 3:
                if len(all_objects) == 0:
                    print("Нет объектов для вывода.")
                    continue
                inx = int(input(f"Введите индекс интересующего объекта (0-{len(all_objects)-1}): ").strip())
                if not(0 <= inx < len(all_objects)):
                    print("Индекс выходит за допустимый диапазон. Попробуйте ещё раз.")
                    continue
                   
                print(f'Название дисциплины: {all_objects[inx].name}')
                print(f'Участники:')
                print(f'{all_objects[inx].teacher}')
                for s in all_objects[inx].students:
                    print(s)
               
                continue
               
if __name__ == "__main__":
    main()