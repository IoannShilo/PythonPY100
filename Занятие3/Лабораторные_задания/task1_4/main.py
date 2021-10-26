def task(epsilon=0.0001):
    sum_ = 0
    n = 1
    item_n = 1 / 2 ** n
    while item_n >= epsilon:
        sum_ += item_n
        n += 1
        item_n = 1 / 2 ** n
    return sum_

#if __name__ == "__main__":
    # Write your solution here
    print(task())

def task_1(epsilon=0.0001):
    sum_ = 0
    n = 1

    while True:
        item_n = 1 / 2 ** n
        if item_n <= epsilon:
            break
        sum_ += item_n
        n += 1

    return sum_
print(task_1())