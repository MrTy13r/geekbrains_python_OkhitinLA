"""6.4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
 который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости"""


# создаём родительский класс


class Car:
    speed: float
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"Машина {self.name} стартовала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction: str):
        if direction == "налево" or direction == "направо":
            print(f"Машина {self.name} повернула {direction}")
        else:
            print("Ошибка, неверное значение для поворота")

    def show_speed(self):
        print(f"Текущая скорость равна {self.speed} км/ч")


# создаём дочерние классы


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"ВНИМАНИЕ! Превышение скорости!")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"ВНИМАНИЕ! Превышение скорости!")

class PoliceCar(Car):
    is_police: bool = True


# создаём экземпляры

car1 = TownCar(70, "Синий", "Volvo")
car2 = SportCar(150, "Чёрный", "BMW")
car3 = WorkCar(40, "Жёлтый", "Ford")
car4 = PoliceCar(100, "Белый", "Toyota")


# выполняем методы

car1.go()
car1.turn("налево")
car1.show_speed()
car1.stop()

print('---------------------------------')

car2.go()
car2.turn("направо")
car2.show_speed()
car2.stop()

print('---------------------------------')

car3.go()
car3.show_speed()
car3.turn("налево")
car3.stop()

print('---------------------------------')

car4.go()
car4.show_speed()
car4.turn("налево")
car4.turn("направо")
car4.stop()
