user_name = input("Как тебя зовут? ")
user_age = int(input("Сколько тебе лет? "))


user_weight = float(input("Укажи свой вес в кг: "))
user_height = float(input("Укажи свой рост в метрах (например, 1.75): "))


bmi = user_weight / (user_height ** 2)


water_needed = user_weight * 30


print(f"Привет, {user_name}!")
print(f"Тебе {user_age} лет.")
print(f"Твой Индекс Массы Тела: {round(bmi, 1)}")
print(f"Рекомендуемая норма воды: {round(water_needed / 1000, 2)} л. в день")
print("Расчет окончен. Будьте здоровы!")
