
x = int(input("Введите x >= 0:"))
while x < 0:
    print("Вы ввели отрицательное число!")
    x = int(input("Введите x >= 0:"))
    

while x > 0:
    digit = x % 10
    print(digit)
    x = x // 10
assert x == 0, "Пользователь ввёл отрицательное число..."
print('Завершение программы')
