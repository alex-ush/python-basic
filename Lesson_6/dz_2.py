class RoadCount:
    def __init__(self, le, wi):
        self._length = le
        self._width = wi

    def count(self, weight=25, thickness=5):
        print(f"Необходимо {self._length * self._width * weight * thickness / 1000:0.0f} тонн асфальта")


my_road = RoadCount(int(input('Введите ширину дороги в метрах: ')), int(input('Введите длину дороги в метрах: ')))
my_road.count()
