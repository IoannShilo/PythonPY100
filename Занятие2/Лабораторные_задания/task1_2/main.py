a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

result_1 = a % 2 == 1
result_2 = b % 2 == 1

if result_1 and result_2:
    print('Оба числа нечетные')
elif result_1:
    print('Только число А нечетное')
elif result_2:
    print('Только число В нечетное')
else:
    print("Оба числа четные")