from constants import ML_IN_LITER, WATER_PER_KG

user_name = input("Как тебя зовут? ").title()

user_age = int(input("Сколько тебе полных лет? Введите число: "))

user_weight = float(
    input("Укажи свой вес в кг: ").replace(",", ".")
)

height_input = input(
    "Укажи свой рост в метрах (например, 1.75): "
)

height_input = height_input.replace(",", ".")
user_height = float(height_input)

bmi = user_weight / (user_height ** 2)

water_needed = user_weight * WATER_PER_KG

print(f"Привет, {user_name}!")
print(f"Тебе {user_age} лет.")
print(f"Твой Индекс Массы Тела: {round(bmi, 1)}")
print(
    f"Рекомендуемая норма воды: "
    f"{round(water_needed / ML_IN_LITER, 2)} л. в день",
)
print("Расчет окончен. Будьте здоровы!")
