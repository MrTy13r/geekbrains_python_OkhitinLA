"""5.7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл"""

from statistics import mean

with open("file_for_task_5.7.txt", encoding='utf-8') as my_file:
    firm_dict = {}
    for n in my_file:
        x = n.split(' ')
        firm_dict[x[0]] = int(x[2]) - int(x[3])
    profit_list = [n for n in firm_dict.values() if n > 0]
    avg_profit_dict = {"average_profit": round(mean(profit_list), 2)}

list_result = [firm_dict, avg_profit_dict]

print(list_result)

import json

with open('file_json_task_5.7.json', 'w') as my_file2:
    json.dump(list_result, my_file2)
