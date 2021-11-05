"""8.4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
 (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
 В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники"""

"""8.5. Продолжить работу над предыдущим заданием. Разработать методы, отвечающие за приём оргтехники на склад 
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, 
а также других данных, можно использовать любую подходящую структуру, например словарь"""

"""8.6. Продолжить работу над предыдущим заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных"""


class Warehouse:
    max_count: int
    equipments: list

    def __init__(self, count = 0):
        self.max_count = count
        self.equipments = []

    def store(self, equipments: list):
        if len(self.equipments) >= self.max_count:
            raise CapacityException(len(self.equipments), len(self.equipments) + len(equipments))
        elif len(equipments) > (self.max_count - len(self.equipments)):
            raise CapacityException(self.max_count, len(self.equipments) + len(equipments))

        self.equipments.extend(equipments)

    def __str__(self):
        return f"На текущий момент на складе следующая техника: {self.equipments}"


class CapacityException(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return f"Не хватает места на складе, текущее = {self.current}, необходимое = {self.needle}"


class OfficeEquipment:
    brand: str
    model: str
    price: int

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        assert isinstance(self.price, int), "Цена должна быть числом"

    def __str__(self):
        return f"{self.brand} {self.model}"

    def __repr__(self):
        return self.__str__()

class Printer(OfficeEquipment):
    print_type: str # лазерный, струйный и т.д.

    def __init__(self, brand, model, price, print_type):
        super().__init__(brand, model, price)
        self.print_type = print_type


class Scanner(OfficeEquipment):
    scanner_type: str # ручной, протяжный, 3D и т.д.

    def __init__(self, brand, model, price, scanner_type):
        super().__init__(brand, model, price)
        self.scanner_type = scanner_type


class Xerox(OfficeEquipment):
    print_color: str # цветная, чёрно-белая

    def __init__(self, brand, model, price, print_color):
        super().__init__(brand, model, price)
        self.print_color = print_color


# создаём объект склад

main_warehouse = Warehouse(2)

# создаём экземпляры офисной техники
office_equipment1 = Printer('Epson', 'L132', 13823, 'Струйный')
office_equipment2 = Scanner('Fujitsu', 'fi-7160', 62305, 'Протяжный')
office_equipment3 = Xerox('Pantum', 'M6700D', 12989, 'Чёрно-белая')


# выведем созданные объекты
print("Созданные объекты\n")
print(office_equipment1)
print(office_equipment2)
print(office_equipment3)

# пытаемся создать объект, где цена указана как строка

print("\nПытаемся создать объект, где цена указана как строка")

try:
    office_equipment4 = Xerox('Xiaomi', 'XC434', '33456', 'Цветная')
except AssertionError as exception:
    print("\nНе удалось создать объект - Цена должна быть числом")

# добавляем на склад две единицы орг.техники
main_warehouse.store([office_equipment1, office_equipment2])
print("\nДобавили на склад две единицы орг.техники, при этом на складе всего два места\n")
print("Выводим что сейчас лежит на складе\n")
print(main_warehouse)

# попытаемся добавить на склад третью единицу орг.техники

print("\nПытаемся добавить на склад третью единицу орг.техники\n")

try:
    main_warehouse.store([office_equipment3])
except CapacityException as exception:
    print(f"На складе закончилось место!")

print("\nНе получилось, т.к. на складе всего 2 места, третья единица не влезает\n")
