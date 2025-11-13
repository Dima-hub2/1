class TV:
    def __init__(self, location, size, resolution):
        self.location = location
        self.size = size
        self.resolution = resolution

    def on(self):
        print(f"ТВ в {self.location} включается... ({self.size} дюймов, {self.resolution})")

    def off(self):
        print(f"ТВ в {self.location} выключается...")

class Console:
    def __init__(self, location, model):
        self.location = location
        self.model = model

    def on(self):
        print(f"Приставка в {self.location} грузится... ({self.model})")

    def off(self):
        print(f"Приставка в {self.location} спит...")

class SoundSystem:
    def __init__(self, location, volume):
        self.location = location
        self.volume = volume

    def play(self):
        print(f"Муз. центр в {self.location}: громкость {self.volume}%")

    def off(self):
        print(f"Звук в {self.location} выключен.")

class Lights:
    def __init__(self, location):
        self.location = location

    def off(self):
        print(f"Свет в {self.location} тухнет...")

    def on(self):
        print(f"Свет в {self.location} включается...")

#ЗАЛ
tv_living = TV("зале", 65, "4K")
console_living = Console("зале", "PS5")
sound_living = SoundSystem("зале", 70)
lights_living = Lights("зале")

#КУХНЯ
tv_kitchen = TV("кухне", 32, "Full HD")
console_kitchen = Console("кухне", "Apple TV")
sound_kitchen = SoundSystem("кухне", 50)
lights_kitchen = Lights("кухне")

#СПАЛЬНЯ
tv_bedroom = TV("спальне", 43, "Smart")
console_bedroom = Console("спальне", "Chromecast")
sound_bedroom = SoundSystem("спальне", 40)
lights_bedroom = Lights("спальне")

class LivingRoomFacade:
    def __init__(self):
        self.tv = tv_living
        self.console = console_living
        self.sound = sound_living
        self.lights = lights_living

    def watch_movie(self):
        print("     КОМНАТА: ЗАЛ — РЕЖИМ КИНО")        
        self.tv.on()
        self.console.on()
        self.sound.play()
        self.lights.off()
        print("   Фильм начался! Наслаждайся!\n")

    def turn_off(self):
        print("\nВыключаем всё в зале...")
        self.tv.off()
        self.console.off()
        self.sound.off()
        self.lights.on()
        print("   Зал выключен.\n")


class KitchenFacade:
    def __init__(self):
        self.tv = tv_kitchen
        self.console = console_kitchen
        self.sound = sound_kitchen
        self.lights = lights_kitchen

    def watch_movie(self):
        print("     КОМНАТА: КУХНЯ — РЕЖИМ КИНО")
        self.tv.on()
        self.console.on()
        self.sound.play()
        self.lights.off()
        print("   Фильм на кухне! Готовь ужин!\n")

    def turn_off(self):
        print("\nВыключаем всё на кухне...")
        self.tv.off()
        self.console.off()
        self.sound.off()
        self.lights.on()
        print("   Кухня выключена.\n")


class BedroomFacade:
    def __init__(self):
        self.tv = tv_bedroom
        self.console = console_bedroom
        self.sound = sound_bedroom
        self.lights = lights_bedroom

    def watch_movie(self):
        print("     КОМНАТА: СПАЛЬНЯ — РЕЖИМ КИНО")
        self.tv.on()
        self.console.on()
        self.sound.play()
        self.lights.off()
        print("   Фильм в спальне... Тихо!\n")

    def turn_off(self):
        print("\nВыключаем всё в спальне...")
        self.tv.off()
        self.console.off()
        self.sound.off()
        self.lights.on()
        print("   Спальня выключена. Спокойной ночи!\n")


def show_menu():
    print("           УМНЫЙ ДОМ: ВЫБЕРИ КОМНАТУ")
    print("1. Зал — кинотеатр")
    print("2. Кухня — лёгкий просмотр")
    print("3. Спальня — тихий вечер")
    print("0. Выключить всё и выйти")


print("Привет! Добро пожаловать в умный дом.\n")

# Создаём фасады
living_room = LivingRoomFacade()
kitchen = KitchenFacade()
bedroom = BedroomFacade()

while True:
    show_menu()
    choice = input("Выбери комнату (0–3): ").strip()

    if choice == "1":
        living_room.watch_movie()
    elif choice == "2":
        kitchen.watch_movie()
    elif choice == "3":
        bedroom.watch_movie()
    elif choice == "0":
        print("\nВыключаем весь дом...")
        living_room.turn_off()
        kitchen.turn_off()
        bedroom.turn_off()
        print("Дом выключен. До свидания!")
        break
    else:
        print("Введи 0, 1, 2 или 3!\n")