def func_(list_):
    chet_ = 0
    nechet_ = 0
    for i in list_:
        if i % 2 == 0:
            chet_ += 1
        elif i % 2 != 0:
            nechet_ += 1

    return chet_, nechet_


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(func_(list_))
