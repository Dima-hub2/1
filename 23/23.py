class TV:
    def on(self):
        print("ТВ включается...")

    def off(self):
        print("ТВ выключается...")

class Console:
    def on(self):
        print("Приставка грузится...")

    def off(self):
        print("Приставка спит...")

class Lights:
    def off(self):
        print("Свет тухнет...")

    def on(self):
        print("Свет включается...")

class SoundSystem:
    def set_volume(self, level=70):
        print(f"Громкость на {level}...")

class Netflix:
    def open(self):
        print("Netflix открывается...")


#ФАСАД — ИНТЕРФЕЙС
class HomeCinema:
    def __init__(self):
        self.tv = TV()
        self.console = Console()
        self.lights = Lights()
        self.sound = SoundSystem()
        self.netflix = Netflix()

    def watch_movie(self):
        print("\n     РЕЖИМ: КИНО")
        self.tv.on()
        self.console.on()
        self.lights.off()
        self.sound.set_volume(70)
        self.netflix.open()
        print("Фильм пошёл! Приятного просмотра!\n")

    def just_tv(self):
        print("\n Просто ТВ")
        self.tv.on()
        print("Канал «Первый» включён.\n")

    def turn_off(self):
        print("\nВыключаем всё...")
        self.tv.off()
        self.console.off()
        self.lights.on()
        print("Пока!\n")

#МЕНЮ
def show_menu():
    print("     УМНЫЙ ПУЛЬТ")
    print("1. Смотреть кино")
    print("2. Просто ТВ")
    print("0. Выключить и выйти")

#ОСНОВНАЯ ПРОГРАММА
print("Привет! Это умный пульт.\n")

# Создаём один объект — весь домашний кинотеатр
cinema = HomeCinema()

while True:
    show_menu()
    choice = input("Что делаем? (0, 1 или 2): ").strip()

    if choice == "1":
        cinema.watch_movie()
    elif choice == "2":
        cinema.just_tv()
    elif choice == "0":
        cinema.turn_off()
        break
    else:
        print("Введи 0, 1 или 2!\n")