from datetime import datetime


def age_massage(year):
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