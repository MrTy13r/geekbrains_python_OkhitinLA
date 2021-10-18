"""3.3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов"""

# Поступим хитрО: превратим полученные значения в список, отсториуем его в обратном порядке,
# и сложим первые два числа в списке. Это значительно проще вложенных if


def my_func(num1, num2, num3):
    list_func = [num1, num2, num3]
    max_number = sorted(list_func, reverse=True)[0]
    second_max_number = sorted(list_func, reverse=True)[1]
    print(max_number + second_max_number)


# Проверяем функцию

my_func(10, 200, 30)
