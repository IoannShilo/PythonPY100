a = int(input("Введите число: "))

condition_1 = a % 2 == 0
condition_2 = a % 3 == 0

if condition_1:
    print("число кратно двум")
elif condition_2:
    print("Число кратно трём")
else:
    print('Число не кратно двум или трем')