class Televisor:

    @property
    def chanel(self):
        chanel = self.chanel
        if chanel < 5:
            m = "прекрасно"
        elif 5 <= chanel <= 10:
            m = "неплохо"
        elif 11 <= chanel <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def __init__(self, chanel, voice):
        self.chanel = chanel
        self.voice = voice
    
    def talk(self):
        print("Вы сейчас на канале номер ",self.chanel, "Громкость ",self.voice)

def main():
    crit_name = input("На какой канал хотите попасть? ")
    crit = Televisor(crit_name)


