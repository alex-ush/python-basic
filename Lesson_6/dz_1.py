import time
import itertools


# class TrafficLight:
#     __color = 'nomatter'
#
#     def running(self):
#         while True:
#             print('Red')
#             time.sleep(6)
#             print('Yellow')
#             time.sleep(2)
#             print('Green')
#             time.sleep(6)
#             print('Yellow')
#             time.sleep(2)
#
#
# trafficl = TrafficLight()
# trafficl.running()


class TrafficLight:
    __color = [['red', [6, 31]], ['yellow', [2, 33]], ['green', [6, 32]], ['yellow', [2, 33]]]

    def runnig(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end='')
            time.sleep(light[1][0])


trafficl = TrafficLight()
trafficl.runnig()
