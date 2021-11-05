"""8.2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой"""

# создаём класс, который будет заниматься делением

class Math:
    numerator: int
    denomerator: int

    @staticmethod
    def division(numerator: int, denomerator: int):
        if denomerator == 0:
            raise DivisionByZeroError
        else:
            return round(numerator / denomerator, 2)

# создаём класс-исключение при делении на ноль

class DivisionByZeroError(Exception):
    def __str__(self):
        return "Ошибка! Деление на ноль"


# проверяем на корректных данных

print(Math.division(4, 2))

# проверяем на некорректных данных (то есть при делении на ноль)
# и дополнительно обернём в try и except для красивого вывода

try:
    print(Math.division(4, 0))
except DivisionByZeroError as exception:
    print("Ошибка! На ноль делить нельзя")
