rost=float(input("Введите ваш рост в метрах: "))
ves=float(input("Введите ваш вес в кг: "))

bmi = round(ves/(rost**2))

if bmi<18.5:
    print(f"Ваш индекс BMI равен: {bmi} это низкий вес...нужно набирать")
elif bmi<25:
    print(f"Ваш индекс BMI равен: {bmi} это нормальный вес.")
elif bmi<30:
    print(f"Ваш индекс BMI равен: {bmi} у Вас предожирение.")
elif bmi<35:
    print(f"Ваш индекс BMI равен: {bmi} у Вас ожирение.")
else:
    print(f"Ваш индекс BMI равен: {bmi} Вы клинический жирдяй")
