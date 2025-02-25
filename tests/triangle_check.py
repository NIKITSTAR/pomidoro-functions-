def check_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("Ошибка: Несуществующий треугольник")
    else:
        if a == b == c:
            print("Результат: Треугольник равносторонний")
        elif a == b or b == c or a == c:
            print("Результат: Треугольник равнобедренный")
        else:
            print("Результат: Треугольник разносторонний")

side1 = int(input("Введите длину первой стороны: "))
side2 = int(input("Введите длину второй стороны: "))
side3 = int(input("Введите длину третьей стороны: "))

check_triangle(side1, side2, side3)
