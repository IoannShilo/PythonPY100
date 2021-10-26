def func(list_: list) -> list:
    mean = sum(list_) // len(list_)
    return [item for item in list_ if item > mean]

if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
    print(func(list_))