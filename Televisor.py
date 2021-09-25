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
    crit_name = input("На какой канал хотите попасть? ")
    crit = Televisor(crit_name)


