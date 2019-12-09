from contracts import contract

@contract(x='int,>=0')
def print_number_digit_by_digit(x):
    while x > 0:
        digit = x % 10
        print(digit)
        x = x // 10


x = int(input("Введите x >= 0:"))
print_number_digit_by_digit(x)
print('Завершение программы')

