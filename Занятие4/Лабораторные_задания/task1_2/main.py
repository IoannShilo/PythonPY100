def func_1(n, m):
    return [i ** 2 for i in range(n, m) if i % 2 != 0]

if __name__ == "__main__":
    # Write your solution here
    n = 1
    m = 21
    print(func_1(n, m))
