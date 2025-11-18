# Функции для телевизоров
def tv_on(location, size, resolution):
    print(f"ТВ в {location} включается... ({size} дюймов, {resolution})")

def tv_off(location):
    print(f"ТВ в {location} выключается...")

# Функции для приставок
def console_on(location, model):
    print(f"Приставка в {location} грузится... ({model})")

def console_off(location):
    print(f"Приставка в {location} спит...")

# Функции для музыкальных центров
def sound_play(location, volume):
    print(f"Муз. центр в {location}: громкость {volume}%")

def sound_off(location):
    print(f"Звук в {location} выключен.")

# Функции для света
def lights_off(location):
    print(f"Свет в {location} тухнет...")

def lights_on(location):
    print(f"Свет в {location} включается...")

# Данные устройств (вместо объектов)
devices = {
    'living_room': {
        'tv': {'location': 'зале', 'size': 65, 'resolution': '4K'},
        'console': {'location': 'зале', 'model': 'PS5'},
        'sound': {'location': 'зале', 'volume': 70},
        'lights': {'location': 'зале'}
    },
    'kitchen': {
        'tv': {'location': 'кухне', 'size': 32, 'resolution': 'Full HD'},
        'console': {'location': 'кухне', 'model': 'Apple TV'},
        'sound': {'location': 'кухне', 'volume': 50},
        'lights': {'location': 'кухне'}
    },
    'bedroom': {
        'tv': {'location': 'спальне', 'size': 43, 'resolution': 'Smart'},
        'console': {'location': 'спальне', 'model': 'Chromecast'},
        'sound': {'location': 'спальне', 'volume': 40},
        'lights': {'location': 'спальне'}
    }
}

# Функции-фасады для комнат
def living_room_watch_movie():
    print("     КОМНАТА: ЗАЛ — РЕЖИМ КИНО")
    room = devices['living_room']
    tv_on(room['tv']['location'], room['tv']['size'], room['tv']['resolution'])
    console_on(room['console']['location'], room['console']['model'])
    sound_play(room['sound']['location'], room['sound']['volume'])
    lights_off(room['lights']['location'])
    print("   Фильм начался! Наслаждайся!\n")

def living_room_turn_off():
    print("\nВыключаем всё в зале...")
    room = devices['living_room']
    tv_off(room['tv']['location'])
    console_off(room['console']['location'])
    sound_off(room['sound']['location'])
    lights_on(room['lights']['location'])
    print("   Зал выключен.\n")

def kitchen_watch_movie():
    print("     КОМНАТА: КУХНЯ — РЕЖИМ КИНО")
    room = devices['kitchen']
    tv_on(room['tv']['location'], room['tv']['size'], room['tv']['resolution'])
    console_on(room['console']['location'], room['console']['model'])
    sound_play(room['sound']['location'], room['sound']['volume'])
    lights_off(room['lights']['location'])
    print("   Фильм на кухне! Готовь ужин!\n")

def kitchen_turn_off():
    print("\nВыключаем всё на кухне...")
    room = devices['kitchen']
    tv_off(room['tv']['location'])
    console_off(room['console']['location'])
    sound_off(room['sound']['location'])
    lights_on(room['lights']['location'])
    print("   Кухня выключена.\n")

def bedroom_watch_movie():
    print("     КОМНАТА: СПАЛЬНЯ — РЕЖИМ КИНО")
    room = devices['bedroom']
    tv_on(room['tv']['location'], room['tv']['size'], room['tv']['resolution'])
    console_on(room['console']['location'], room['console']['model'])
    sound_play(room['sound']['location'], room['sound']['volume'])
    lights_off(room['lights']['location'])
    print("   Фильм в спальне... Тихо!\n")

def bedroom_turn_off():
    print("\nВыключаем всё в спальне...")
    room = devices['bedroom']
    tv_off(room['tv']['location'])
    console_off(room['console']['location'])
    sound_off(room['sound']['location'])
    lights_on(room['lights']['location'])
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