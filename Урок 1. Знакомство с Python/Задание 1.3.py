# 1.3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

# Чтобы получить nn, мы должны не сложить цифры, а соединить символы.
# Для этого мы приведём n к типу str, соединим n и n, но в итоге приведём всё к типу int,
# чтобы в дальнейшем мы смогли произвести математическую операцию.
# Для nnn аналогично

n = int(input("Введите число: "))

nn = int(str(n) + str(n))

nnn = int(str(n) + str(n) + str(n))

print(n + nn + nnn)