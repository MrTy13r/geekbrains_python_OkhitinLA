"""5.2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке"""

my_file = open(r'file_for_task_5.2.txt')

print(f"Вот содержимое файла:\n{my_file.read()}")

my_file.close()

print("\n---- Выполнение задания ----\n")

my_file = open(r'file_for_task_5.2.txt')

file_list = my_file.readlines()

counter = 0

for num, line in enumerate(file_list):
    x = len(line.replace('\n', ''))
    print(f"Количество слов в строке {num+1}: {x}")
    counter += 1

print(f"\nКоличество строк в файле: {counter}")
