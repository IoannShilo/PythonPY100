def my_func(nakoplen_, dohod, rashod):

    month = 0
    while nakoplen_ > 0:
        nakoplen_ = nakoplen_ + dohod - rashod
        month += 1
        rost_cen = rashod * 0.05
        rashod = rashod + rost_cen
        print(month)


if __name__ == "__main__":
    s = 50000
    a = 5000
    b = 10000
    print(my_func(s, a, b))