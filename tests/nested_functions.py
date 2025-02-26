def calculator():
    # Вложенные функции для каждой операции
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        # Добавим проверку деления на ноль
        if y == 0:
            return "Ошибка: деление на ноль!"
        return x / y

    # Запрашиваем входные данные у пользователя
    value1 = float(input('Введите первое число: '))
    value2 = float(input('Введите второе число: '))
    operation = input('Выберите операцию (+, -, *, /): ')

    # Выполняем операцию
    if operation == '+':
        result = add(value1, value2)
    elif operation == '-':
        result = subtract(value1, value2)
    elif operation == '*':
        result = multiply(value1, value2)
    elif operation == '/':
        result = divide(value1, value2)
    else:
        result = 'Неизвестная операция.'

    # Выводим результат
    print('Результат:', result)
    return result

calculator()
