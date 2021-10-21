def my_func1(month=10, b=10000, c=5000):
    total_roshod = 0
    total_dohod = 0
    while month > 0:
        total_roshod = total_roshod + b
        add_ = b * 0.03
        b = b + add_
        month -= 1
        total_dohod = total_dohod + c
        total_summ = total_roshod - total_dohod
    return total_summ


if __name__ == "__main__":
    #month = 10
    #b = 10000
    print(int(my_func1()))
