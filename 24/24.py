# observer_procedural.py

# Глобальные переменные
temperature = 0
observers = []        # список функций-подписчиков


# === Функции-подписчики ===
def phone_app(temp):
    print(f"  [Телефон] Погода: {temp}°C")

def smart_watch(temp):
    print(f"  [Часы] {temp}°C")

def website(temp):
    print(f"  [Сайт] Температура: {temp}°C")


# === Основные функции ===
def add_observer(func):
    """Добавить приложение в список уведомлений"""
    observers.append(func)
    print(f"Подписчик добавлен: {func.__name__}")

def remove_observer(func):
    """Убрать из подписки"""
    if func in observers:
        observers.remove(func)
        print(f"Подписчик удалён: {func.__name__}")
    else:
        print("Такого подписчика нет!")

def set_temperature(new_temp):
    """Изменить температуру и оповестить всех"""
    global temperature
    temperature = new_temp
    print(f"\nТемпература изменилась: {temperature}°C")
    notify_all()

def notify_all():
    """Пройти по всем подписчикам и вызвать их"""
    for obs in observers:
        obs(temperature)   # вызываем функцию с текущей температурой


# === ТЕСТ ПРОГРАММЫ ===
def main():
    print("Запускаем метеостанцию...\n")

    # Подписываем приложения
    add_observer(phone_app)
    add_observer(smart_watch)
    add_observer(website)

    print("\n" + "-"*35)

    # Меняем погоду
    set_temperature(25)
    set_temperature(18)

    print("\n" + "-"*35)

    # Убираем сайт из подписки
    remove_observer(website)

    # Ещё раз меняем — сайт уже не получит
    set_temperature(30)

if __name__ == "__main__":
    main()