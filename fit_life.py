# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = input('Как вас зовут?')
user_age = int(input('Сколько вам лет?'))

# 2. Сбор данных
user_weight = float(input('Какой у вас вес (кг)'))
user_height = float(input('Какой у вас рост (м)?'))

# 3. Подсчет ИМТ
bmi = user_weight / (user_height ** 2)

# 4. Подсчет воды: вес * 30 мл
water_needed = user_weight * 30

# 5. Подсчет воды в литрах
water_liters = water_needed / 1000

# 6. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {round(bmi, 1)}")
print(f"Рекомендуемая норма воды: {round(water_liters, 1)} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
