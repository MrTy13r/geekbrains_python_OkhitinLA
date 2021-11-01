"""6.5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра"""


# создание родительского класса


class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки")


# создание дочерних классов


class Pen(Stationery):
    title = "Ручка"
    def draw(self):
        super().draw()
        print("ручкой")


class Pencil(Stationery):
    title = "Карандаш"
    def draw(self):
        super().draw()
        print("карандашом")


class Handle(Stationery):
    title = "Маркер"
    def draw(self):
        super().draw()
        print("маркером")


# создание экземпляров классов и вызов методов


parker = Pen()
parker.draw()

print('---------------------------------')

carandache = Pencil()
carandache.draw()

print('---------------------------------')

staedtler = Handle()
staedtler.draw()
