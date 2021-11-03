"""7.2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
 — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
 Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property"""

from abc import ABC, abstractmethod


# создаём родительский класс

class Clothes(ABC):
    name: str

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass


# создаём дочерний класс Coat (пальто)

class Coat(Clothes):
    v: float
    # v - volume, т.е. размер

    def __init__(self, name, v) -> None:
        self.v = v
        super().__init__(name)

    @property
    def tissue_consumption(self):
        return round(self.v / 6.5 + 0.5, 2)


# создаём дочерний класс Suit (костюм)

class Suit(Clothes):
    h: float
    # h - height, т.е. рост

    def __init__(self, name, h) -> None:
        self.h = h
        super().__init__(name)

    @property
    def tissue_consumption(self):
        return round(2 * self.h + 0.3, 2)


# проверяем работу методов


Coat1 = Coat('Zara', 48)
print("\nРасчёт по пальто\n")
print(f"Расход ткани для {Coat1.name} равен {Coat1.tissue_consumption}")

print("---------------------")

Suit1 = Suit('Armani', 183)
print("\nРасчёт по костюму\n")
print(f"Расход ткани для {Suit1.name} равен {round(2 * Suit1.h + 0.3, 2)}")


# функция для общего подсчёта расхода ткани

def sum_tissue_consumption(clothes: list[Clothes]):
    listX = []
    for n in clothes:
        listX.append(n.tissue_consumption)
    return sum(listX)

print(f"\nОбщий расход ткани равен {sum_tissue_consumption([Coat1, Suit1])}")
