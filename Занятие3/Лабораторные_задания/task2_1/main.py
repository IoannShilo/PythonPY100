def task(str1, str2, k):
    if str1[:k] == str2[:k]:
        print('ДА')
    else:
        print('НЕТ')


if __name__ == "__main__":
    str1 = input('строка: ')
    str2 = input('строка: ')
    k = 2
    print(task(str1, str2, k))
