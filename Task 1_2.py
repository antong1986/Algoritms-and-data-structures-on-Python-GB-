#  Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся
#  пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
#  Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
#  неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
#  Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
sign = input('Введите знак операции(+)(-)(*)(/), Для завершения программы введите 0: ')

while sign != '0':
    try:
        if sign == '+':
            print(num_1 + num_2)
        if sign == '-':
            print(num_1 - num_2)
        if sign == '*':
            print(num_1 * num_2)
        if sign == '/':
            print(num_1 // num_2)
    except ZeroDivisionError:
        print('Деление на ноль невозможно!')
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    sign = input('Введите знак операции(+)(-)(*)(/), Для завершения программы введите 0: ')
print('Программа завершена')
