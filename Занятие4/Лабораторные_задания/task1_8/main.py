def func_(list_):
    return [i ** 3 for i in list_ if i > 0]


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
print(func_(list_))