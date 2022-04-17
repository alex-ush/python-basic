from random import choice


class Car:
    direction = ['left', 'right']

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'Ваша машина: {n}, цвет: {c}.\nЭто полицейский автомобиль? {p}')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self):
        print(f'{self.name}: Машина повернула {choice(self.direction)}.')

    def show_speed(self):
        print(f'{self.name}: Скорость машины: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость машины: {self.speed}, так быстро нельзя!'\
            if self.speed > 60 else super().show_speed()


class SportCar(Car):
    """ Sport Car """


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость машины: {self.speed}, так быстро нельзя!' \
            if self.speed > 40 else super().show_speed()


class PoliceCar(Car):
    def __init__(self, n, c, s):
        super().__init__(n, c, s, p=True)


town = TownCar('Honda Fit', 'Синий', 75)
sport = SportCar('Nissan TG-R', 'Белый', 180)
work = WorkCar('Dodge Ram', 'Красный', 40)
police = PoliceCar('Ford Mondeo', 'Синий', 90)

all_cars = [town, sport, work, police]

for i in all_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
