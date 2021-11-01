"""6.1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на
ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод"""


import time

class TrafficLight:
    __color: str

    def running(self):
        print('\nДля выключения светофора нажмите Ctrl+F2\n')
        while True:
            self.__color = 'Красный'
            print('\033[91m' + self.__color + ' - 7 секунд')
            time.sleep(7)
            self.__color = 'Жёлтый'
            print('\033[33m' + self.__color + ' - 2 секунды')
            time.sleep(2)
            self.__color = 'Зелёный'
            print('\033[32m' + self.__color + ' - 6 секунд')
            time.sleep(6)


# проверяем


try:
    trafficlight_test_1 = TrafficLight()
    trafficlight_test_1.running()
except KeyboardInterrupt:
    print("\nСветофор выключен")
