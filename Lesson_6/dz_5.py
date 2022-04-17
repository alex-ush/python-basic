class Stationery:
    def __init__(self, title="Канцелярия"):
        self.title = title

    def draw(self):
        print(f'{self.title} поможет тебе творить')


class Pen(Stationery):
    def draw(self):
        print(f'Ручкой лучше всего {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Карандашом удобно {self.title}')


class Marker(Stationery):
    def draw(self):
        print(f'Маркером можно {self.title}')

stationery = Stationery()
pen = Pen('писать')
pencil = Pencil('чертить')
marker = Marker('рисовать')

my_stationery = [stationery, pen, pencil, marker]

for i in my_stationery:
    i.draw()
