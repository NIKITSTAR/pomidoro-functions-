from datetime import datetime

def age_massage(year):
    """
    Запрашивает у пользователя год рождения и выводит сообщение о возрасте.

    Args:
        year (str): Сообщение, отображаемое пользователю для запроса года рождения.

    Действия:
        Вычисляет возраст, вычитая введённый год из текущего года, и выводит сообщение:
            - Если возраст меньше 18: "Вы еще молоды, учеба — ваш путь!"
            - Если возраст от 18 до 65: "Отличный возраст для карьерного роста!"
            - Если возраст больше 65: "Пора наслаждаться заслуженным отдыхом!"
    """
    value = input(year)
    age = datetime.now().year - int(value)
    print(f'Ваш возраст: {age}')
    if age < 18:
        print("Вы еще молоды, учеба — ваш путь!")
    elif 18 <= age <= 65:
        print("Отличный возраст для карьерного роста!")
    else:
        print("Пора наслаждаться заслуженным отдыхом!")

age_massage('Какой ваш год рождения? ')
