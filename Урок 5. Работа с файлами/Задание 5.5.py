"""5.5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран"""

while True:
    with open('file_for_task_5.5.txt', 'a') as my_file:
        number = input("Добавьте в файл числа через пробел: ")
        my_file.write(f"{number} ")
        break

with open('file_for_task_5.5.txt', 'r') as my_file2:
    number_list = my_file2.read().split()
    print(f"Сумма всех текущих чисел в файле: {sum(int(x) for x in number_list)}")
