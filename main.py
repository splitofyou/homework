#N1
n1 = float(input("Введите первое число: "))
n2 = float(input("Введите второе число: "))

maxn = max(n1, n2)

print(f"Максимальное число: {maxn}")

#N2
n1 = float(input("Введите первое число: "))
n2 = float(input("Введите второе число: "))
n3 = float(input("Введите третье число: "))

choice = input("Введите 'max' для максимума, 'min' для минимума или 'avg' для среднего арифметического: ")

if choice == 'max':
    result = max(n1, n2, n3)
elif choice == 'min':
    result = min(n1, n2, n3)
elif choice == 'avg':
    result = (n1 + n2 + n3) / 3
else:
    result = "Неверный выбор"

print(f"Результат: {result}")

#N3
number = float(input("Введите число: "))

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")

#N4
n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
n3 = int(input("Введите третье число: "))

even= sum(num % 2 == 0 for num in [n1, n2, n3])

print(f"Количество четных чисел: {even}")

#N5
n1 = float(input("Введите первое число: "))
n2 = float(input("Введите второе число: "))
n3 = float(input("Введите третье число: "))

choice = input("Введите 'sum' для суммы или 'prod' для произведения: ")

if choice == 'sum':
    result = n1 + n2 + n3
elif choice == 'prod':
    result = n1 * n2 * n3
else:
    result = "Неверный выбор"

print(f"Результат: {result}")

#N6
m = float(input("Введите количество метров: "))

choice = input("Введите 'miles' для миль, 'inches' для дюймов или 'yards' для ярдов: ")

if choice == 'miles':
    result = m * 0.000621371
elif choice == 'inches':
    result = m * 39.3701
elif choice == 'yards':
    result = m * 1.09361
else:
    result = "Неверный выбор"

print(f"Результат: {result}")

#N7
mnth = int(input("Введите номер месяца (от 1 до 12): "))

if mnth in [12, 1, 2]:
    season = "Зима"
elif mnth in [3, 4, 5]:
    season = "Весна"
elif mnth in [6, 7, 8]:
    season = "Лето"
elif mnth in [9, 10, 11]:
    season = "Осень"
else:
    season = "Неверный месяц"

print(f"Пора года: {season}")