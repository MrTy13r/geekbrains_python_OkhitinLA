"""8.1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
 преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
 (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных"""

# создаём класс

class Date:
    def __init__(self, date: str):
        nums = Date.extractor(date)
        self.validator(nums)

    @classmethod
    def extractor(cls, date: str) -> list:
        return [int(n) for n in date.split('-')]

    @staticmethod
    def validator(nums: list):
        day, month, year = nums
        assert 1 <= day <= 31, "Ошибка: день может быть только от 1 до 31"
        assert 1 <= month <= 12, "Ошибка: месяц может быть только от 1 до 12"
        assert 0 <= year <= 2500, "Ошибка: год состоит из 4 цифр от 0 до 2500"


# создаём дату 1 и проверяем метод извлечения цифр

Date1 = Date("03-11-2021")
print(Date.extractor('03-11-2021'))

# создаём некорректные даты и прверяем валидацию

Date2 = Date("32-11-2021")
Date3 = Date("03-13-2021")
Date4 = Date("03-11-2600")
