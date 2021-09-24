class Football:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def talk(self):
        print("Меня зовут ", self.name, ", и я стою на позиции ", self.position)

def main():
    crit1 = Football('Даниил Каценев', 'вратаря')
    crit1.talk()
    crit2 = Football('Юрий Романюк', 'защитника')
    crit2.talk()
    crit3 = Football('Эдуард Сарапий', 'защитника')
    crit3.talk()
    crit4 = Football('Владислав Нетхий', 'полузащитника')
    crit4.talk()
    crit5 = Football('Руслан Шомин', 'нападающего')
    crit5.talk()
    crit6 = Football('Артур Денчук', 'вратаря')
    crit6.talk()
    crit7 = Football('Владимир Шопин', 'защитника')
    crit7.talk()
    crit8 = Football('Александр Рыбка', 'вратаря')
    crit8.talk()
    crit9 = Football('Евгений Рязанцев', 'нападающего')
    crit9.talk()
    crit10 = Football('Егор демченко', 'полузащитника')
    crit10.talk()
    crit11 = Football('Сергей Горбунов', 'полузащитника')
    crit11.talk()
    print("Всё мы играем за Металист!!")

main()