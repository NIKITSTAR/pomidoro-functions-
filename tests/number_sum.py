def number_sum():
    n = int(input("Введите число: "))

    # Формируем список чисел [1, 2, ..., n] с помощью цикла while
    i = 1
    spisok = []
    while i <= n:
        spisok.append(i)
        i += 1

    # Суммируем числа в spisok с помощью цикла for
    summa = 0
    for num in spisok:
        summa += num

    # Выводим результаты
    print("Числа:", *spisok)
    print(f"Сумма чисел: {summa}")

number_sum()
