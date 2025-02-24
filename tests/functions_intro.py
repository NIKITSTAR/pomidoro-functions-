def greet_user(name):
    value = input(name)
    if value.isalpha():
        print(f"Привет, {value}! Добро пожаловать в мир Python!")
    else:
        print("Ошибка: введите только буквы без пробелов и цифр")

def calculate_sum(a, b):
    return a + b

greet_user("Введите ваше имя: ")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print("Сумма чисел:", calculate_sum(a, b))
