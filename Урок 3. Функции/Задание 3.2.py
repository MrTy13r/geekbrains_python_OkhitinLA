"""3.2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой"""


def user_info(name, last_name, year_of_birth, city, email, phone_number):
    return f"{name} {last_name}, {year_of_birth}, {city}, {email}, {phone_number}"

# Вариант 1: выводим просто через функцию


print(user_info("John", "Connor", '1981', "Los Angeles", "machine_killer@t2.com", "555-55-55"))


# Вариант 2: просим пользователя вывести через input


user_name = input("Введите имя: ")
user_last_name = input("Введите фамилию: ")
user_year_of_birth = int(input("Введите год рождения: "))
user_city = input("Введите город: ")
user_email = input("Введите email: ")
user_phone_number = input("Введите номер телефона: ")

print(user_info(name=user_name,
                last_name=user_last_name,
                year_of_birth=user_year_of_birth,
                city=user_city,
                email=user_email,
                phone_number=user_phone_number))
