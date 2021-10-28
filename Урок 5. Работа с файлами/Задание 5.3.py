"""5.3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников"""

from statistics import mean

with open("file_for_task_5.3.txt", encoding='utf-8') as my_file:
    my_list = [line.split() for line in my_file.readlines()]
    print("Сотрудники с окладом менее 20000:")
    for idx, n in enumerate(my_list):
        if float(my_list[idx][1]) < 20000:
            print(my_list[idx][0])

    salary_list = []
    for idx, n in enumerate(my_list):
        salary_list.append(float(my_list[idx][1]))

    slary_list_less_20000 = []
    for idx, n in enumerate(my_list):
        if float(my_list[idx][1]) < 20000:
            slary_list_less_20000.append(float(my_list[idx][1]))

    print(f"\nСредний оклад всех сотрудников равен {mean(salary_list)}")
    print(f"\nСредний оклад сотрудников с ЗП менее 20000 равен {mean(slary_list_less_20000)}")
