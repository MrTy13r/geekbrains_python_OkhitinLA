"""8.7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата"""


# создаём класс

class ComplexNumber:
    a: float
    b: float

    def __init__(self,  a: float, b: float):
        self.a = a
        self.b = b

    def __add__(self, other: 'ComplexNumber'):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other: 'ComplexNumber'):

        num1 = (self.a * other.a) + (self.b * other.b * -1)
        num2 = (self.a * other.b) + (self.b * other.a)

        return ComplexNumber(num1, num2)

    def __str__(self):
        return f"{self.a} + {self.b}i"

# создаём косплексные числа


ComplexNumber1 = ComplexNumber(11, 78)
ComplexNumber2 = ComplexNumber(13, 67)

# производим вычисления

print(f"Результат сложения: {ComplexNumber1 + ComplexNumber2}")

print(f"Результат умножения: {ComplexNumber1 * ComplexNumber2}")
