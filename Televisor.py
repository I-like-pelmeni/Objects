class Televisor:

    @property
    def chanel(self):
        chanel = self.chanel
        if chanel > 20:
            print("Нельзя перемистится на этот канал")
        
    @property
    def voice(self):
        voice = self.voice
        if voice > 100:
            print("Нельзя сделать звук громче 100")

    

    def __init__(self, chanel, voice):
        self.chanel = chanel
        self.voice = voice
    
    def talk(self):
        print("Вы сейчас на канале номер ",self.chanel, "Громкость ",self.voice)

def main():
    crit_chanel = input("На какой канал хотите попасть? ")
    crit = Televisor(crit_chanel)

    choice = None
    while choice != 0:
        print \
        ("""
        0 - Узнать на каком я сейчас канале
        1 - Узнать уровень громкости
        """)

        choice = input("Ваш выбор:")
        print()


    if choice > 1 < 8:
        print("Это спортивные каналы")
    elif choice > 7 < 13:
        print("Это каналы про природу")
    elif choice > 12 < 20:
        print("Это новостые каналы")

    elif choice == "1":
        crit.chanel
    elif choice == "2":
        crit.voice

    else:
        print("Изыините, в меню нет пункта", choice)

main()

