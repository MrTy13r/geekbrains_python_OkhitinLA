"""5.4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл"""

import os

if os.path.exists("file_for_task_5.4_rus.txt"):
    os.remove("file_for_task_5.4_rus.txt")

with open("file_for_task_5.4.txt", encoding='utf-8') as my_file:
    my_list = [line.split() for line in my_file.readlines()]
    my_list[0][0] = my_list[0][0].replace('One', 'Один')
    my_list[1][0] = my_list[1][0].replace('Two', 'Два')
    my_list[2][0] = my_list[2][0].replace('Three', 'Три')
    my_list[3][0] = my_list[3][0].replace('Four', 'Четыре')
    for idx, n in enumerate(my_list):
        print(f"{my_list[idx][0]} {my_list[idx][1]} {my_list[idx][2]}")
        with open("file_for_task_5.4_rus.txt", 'a', encoding='utf-8') as my_file_rus:
            my_file_rus.writelines(f"{my_list[idx][0]} {my_list[idx][1]} {my_list[idx][2]}\n")
