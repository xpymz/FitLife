# Проект FitLife - MVP версия 1.0

# Константы
WATER_PER_KG = 30
ML_IN_LITER = 1000


def main():
    # 1. Знакомство
    user_name = input('Как вас зовут? ')

    # Безопасный ввод возраста
    while True:
        try:
            user_age = int(
                input('Сколько вам лет? (введите целое число): ')
            )
            break
        except ValueError:
            print(
                'Ошибка: возраст должен быть целым числом. '
                'Попробуйте еще раз.'
            )

    # 2. Сбор данных
    while True:
        try:
            weight_input = input('Какой у вас вес (кг)? ')
            user_weight = float(weight_input.replace(',', '.'))

            height_input = input('Какой у вас рост (м)? ')
            user_height = float(height_input.replace(',', '.'))
            break
        except ValueError:
            print(
                'Ошибка: вес и рост должны быть числами. '
                'Попробуйте еще раз.'
            )

    # 3. Подсчет ИМТ
    bmi = user_weight / (user_height ** 2)

    # 4. Подсчет воды: вес * 30 мл
    water_needed = user_weight * WATER_PER_KG

    # 5. Подсчет воды в литрах
    water_liters = water_needed / ML_IN_LITER

    # 6. Вывод красивого результата
    print(
        f'Отчет для пользователя: {user_name} ({user_age} г.)\n'
        f'Твой Индекс Массы Тела: {round(bmi, 1)}\n'
        f'Рекомендуемая норма воды: {round(water_liters, 1)} л. в день\n'
        f'Расчет окончен. Будьте здоровы!'
    )


# 7. Точка входа в программу
if __name__ == '__main__':
    main()
