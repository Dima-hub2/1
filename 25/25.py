def tv_on():
    print("ТВ включается...")

def tv_off():
    print("ТВ выключается...")

def console_on():
    print("Приставка грузится...")

def console_off():
    print("Приставка спит...")

def lights_on():
    print("Свет включается...")

def lights_off():
    print("Свет выключается...")

def sound_set(volume=70):
    print(f"Громкость на {volume}...")

def netflix_open():
    print("Netflix открывается...")

# МЕНЮ
def show_menu():
    print("\n     УМНЫЙ ПУЛЬТ")
    print("1. Смотреть кино")
    print("2. Просто ТВ")    
    print("3 Выключить всё")

# ОСНОВНАЯ ПРОГРАММА
print("Привет! Это умный пульт (готовые сценарии без паттернов).")

while True:
    show_menu()
    choice = input("Что делаем? (1-3): ").strip()

    if choice == "1":
        # СЦЕНАРИЙ "СМОТРЕТЬ КИНО
        print("\n РЕЖИМ: КИНО")
        tv_on()
        console_on()
        lights_off()
        sound_set(70)  # громкость для кино
        netflix_open()
        print("Фильм начался! Приятного просмотра!")

    elif choice == "2":
        # СЦЕНАРИЙ ПРОСТО ТВ
        print("\n РЕЖИМ: ПРОСМОТР ТВ")
        tv_on()
        lights_on()    
        sound_set(40)  
        print("Телепередача включена!")    

    elif choice == "3":
        # СЦЕНАРИЙ "ВЫКЛЮЧИТЬ ВСЁ"
        print("\n ВЫКЛЮЧЕНИЕ СИСТЕМЫ")
        console_off()
        tv_off()
        lights_on()
        print("Все устройства выключены. До свидания!")
        break

    else:
        print("Введите число от 0 до 3!")