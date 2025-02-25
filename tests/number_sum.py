def number_sum():
    n = int(input("Введите число: "))
    spisok = list(range(1, n + 1))  # Создаём список [1, 2, ..., n]
    summa = sum(spisok)            # Суммируем все элементы списка
    print("Числа:", *spisok)
    print(f"Сумма чисел: {summa}")

number_sum()