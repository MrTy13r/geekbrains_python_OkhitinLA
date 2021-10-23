"""4.6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее"""

# Итератор A

print("Итератор A")

start_num = int(input("Введите начальное значение: "))
end_num = int(input("Введите конечное значение: "))

from itertools import count

for x in count(start_num):
    if x > end_num:
        break
    else:
        print(x)

# Итератор Б

print("Итератор Б")

from itertools import cycle

my_list = input("Введите список чисел через запятую: ").split(",")
my_list = [int(x) for x in my_list]
print(f"Ваш список: {my_list}")

iterations = int(input("Максимальное количество выводов: "))

counter = 0

for num in cycle(my_list):
    if counter >= iterations:
        break
    else:
        print(num)
    counter += 1
