# Функции для зала (все уникальные, без повторного использования)
def living_room_tv_on():
    print(f"ТВ в зале включается... (65 дюймов, 4K)")

def living_room_tv_off():
    print(f"ТВ в зале выключается...")

def living_room_console_on():
    print(f"Приставка в зале грузится... (PS5)")

def living_room_console_off():
    print(f"Приставка в зале спит...")

def living_room_sound_play():
    print(f"Муз. центр в зале: громкость 70%")

def living_room_sound_off():
    print(f"Звук в зале выключен.")

def living_room_lights_off():
    print(f"Свет в зале тухнет...")

def living_room_lights_on():
    print(f"Свет в зале включается...")

# Функции для кухни (полностью дублируют зал, но с другими значениями)
def kitchen_tv_on():
    print(f"ТВ в кухне включается... (32 дюйма, Full HD)")

def kitchen_tv_off():
    print(f"ТВ в кухне выключается...")

def kitchen_console_on():
    print(f"Приставка в кухне грузится... (Apple TV)")

def kitchen_console_off():
    print(f"Приставка в кухне спит...")

def kitchen_sound_play():
    print(f"Муз. центр в кухне: громкость 50%")

def kitchen_sound_off():
    print(f"Звук в кухне выключен.")

def kitchen_lights_off():
    print(f"Свет в кухне тухнет...")

def kitchen_lights_on():
    print(f"Свет в кухне включается...")

# Функции для спальни (тоже полное дублирование)
def bedroom_tv_on():
    print(f"ТВ в спальне включается... (43 дюйма, Smart)")

def bedroom_tv_off():
    print(f"ТВ в спальне выключается...")

def bedroom_console_on():
    print(f"Приставка в спальне грузится... (Chromecast)")

def bedroom_console_off():
    print(f"Приставка в спальне спит...")

def bedroom_sound_play():
    print(f"Муз. центр в спальне: громкость 40%")

def bedroom_sound_off():
    print(f"Звук в спальне выключен.")

def bedroom_lights_off():
    print(f"Свет в спальне тухнет...")

def bedroom_lights_on():
    print(f"Свет в спальне включается...")

# Функции режимов для каждой комнаты (тоже без повторного использования)
def living_room_watch_movie():
    print("     КОМНАТА: ЗАЛ — РЕЖИМ КИНО")
    living_room_tv_on()
    living_room_console_on()
    living_room_sound_play()
    living_room_lights_off()
    print("   Фильм начался! Наслаждайся!\n")

def living_room_turn_off():
    print("\nВыключаем всё в зале...")
    living_room_tv_off()
    living_room_console_off()
    living_room_sound_off()
    living_room_lights_on()
    print("   Зал выключен.\n")

def kitchen_watch_movie():
    print("     КОМНАТА: КУХНЯ — РЕЖИМ КИНО")
    kitchen_tv_on()
    kitchen_console_on()
    kitchen_sound_play()
    kitchen_lights_off()
    print("   Фильм на кухне! Готовь ужин!\n")

def kitchen_turn_off():
    print("\nВыключаем всё на кухне...")
    kitchen_tv_off()
    kitchen_console_off()
    kitchen_sound_off()
    kitchen_lights_on()
    print("   Кухня выключена.\n")

def bedroom_watch_movie():
    print("     КОМНАТА: СПАЛЬНЯ — РЕЖИМ КИНО")
    bedroom_tv_on()
    bedroom_console_on()
    bedroom_sound_play()
    bedroom_lights_off()
    print("   Фильм в спальне... Тихо!\n")

def bedroom_turn_off():
    print("\nВыключаем всё в спальне...")
    bedroom_tv_off()
    bedroom_console_off()
    bedroom_sound_off()
    bedroom_lights_on()
    print("   Спальня выключена. Спокойной ночи!\n")

def show_menu():
    print("           УМНЫЙ ДОМ: ВЫБЕРИ КОМНАТУ")
    print("1. Зал — кинотеатр")
    print("2. Кухня — лёгкий просмотр")
    print("3. Спальня — тихий вечер")
    print("0. Выключить всё и выйти")

# Основная программа
print("Привет! Добро пожаловать в умный дом.\n")

while True:
    show_menu()
    choice = input("Выбери комнату (0–3): ").strip()

    if choice == "1":
        living_room_watch_movie()
    elif choice == "2":
        kitchen_watch_movie()
    elif choice == "3":
        bedroom_watch_movie()
    elif choice == "0":
        print("\nВыключаем весь дом...")
        living_room_turn_off()
        kitchen_turn_off()
        bedroom_turn_off()
        print("Дом выключен. До свидания!")
        break
    else:
        print("Введи 0, 1, 2 или 3!\n")