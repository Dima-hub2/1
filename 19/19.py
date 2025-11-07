class Author:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f'Автор: {self.name}, должность: {self.position}'

class Article:
    def __init__(self, title, topic):
        self.title = title
        self.topic = topic

    def __str__(self):
        return f'Статья: "{self.title}", тема: {self.topic}'
class Journal:
    def __init__(self, name, authors, articles):
        self.name = name
        self.authors = authors      # список авторов
        self.articles = articles    # список статей

    def __str__(self):
        text = f'Журнал: "{self.name}"\n'
        text += "\nАвторы:\n"
        for a in self.authors:
            text += f'  - {a.name}, {a.position}\n'
        text += "\nСтатьи:\n"
        for s in self.articles:
            text += f'  - "{s.title}" ({s.topic})\n'
        return text

authors = []
articles = []
journals = []

while True:
    print("\nМЕНЮ:")
    print("1. Создать новый объект")
    print("2. Показать все объекты")
    print("3. Показать подробную информацию об объекте")
    print("4. Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        print("\nЧто создать?")
        print("1. Автора")
        print("2. Статью")
        print("3. Журнал")
        sub = input("Введите номер: ")

        if sub == "1":
            name = input("Введите ФИО автора: ")
            position = input("Введите должность: ")
            author = Author(name, position)
            authors.append(author)
            print("Автор создан!")

        elif sub == "2":
            title = input("Введите название статьи: ")
            topic = input("Введите тему статьи: ")
            article = Article(title, topic)
            articles.append(article)
            print("Статья создана")

        elif sub == "3":
            if not authors or not articles:
                print("Сначала создайте хотя бы одного автора и одну статью!")
            else:
                name = input("Введите название журнала: ")

                print("\nДоступные авторы:")
                for i, a in enumerate(authors):
                    print(f"{i + 1}. {a.name}")

                selected_authors = []
                print("Введите номера авторов через запятую (например: 1,2,3): ")
                a_nums = input().split(",")
                for n in a_nums:
                    index = int(n.strip()) - 1
                    if 0 <= index < len(authors):
                        selected_authors.append(authors[index])

                print("\nДоступные статьи:")
                for i, art in enumerate(articles):
                    print(f"{i + 1}. {art.title}")

                selected_articles = []
                print("Введите номера статей через запятую (например: 1,2): ")
                s_nums = input().split(",")
                for n in s_nums:
                    index = int(n.strip()) - 1
                    if 0 <= index < len(articles):
                        selected_articles.append(articles[index])

                journal = Journal(name, selected_authors, selected_articles)
                journals.append(journal)
                print("Журнал создан!")

    elif choice == "2":
        print("\nАвторы:")
        if not authors:
            print("  нет авторов")
        else:
            for a in authors:
                print(" ", a)

        print("\nСтатьи:")
        if not articles:
            print("  нет статей")
        else:
            for a in articles:
                print(" ", a)

        print("\nЖурналы:")
        if not journals:
            print("  нет журналов")
        else:
            for j in journals:
                print(" ", j.name)

    elif choice == "3":
        print("\nЧто показать?")
        print("1. Автора")
        print("2. Статью")
        print("3. Журнал")
        sub = input("Введите номер: ")

        if sub == "1":
            for a in authors:
                print(a)
        elif sub == "2":
            for a in articles:
                print(a)
        elif sub == "3":
            for j in journals:
                print(j)

    elif choice == "4":
        print("Программа завершена.")
        break

    else:
        print("Неверный пункт меню!")
