if __name__ == "__main__":
    n = 27031997
print(list(str(n)))

summ_ = [int(d) for d in str(n)]
print(sum(summ_))

sum_even = 0
for i in summ_:
    if i % 2 == 0:
        sum_even += i
print(sum_even)

print(len(summ_))

print(min(summ_), max(summ_))

print(summ_[0::2], summ_[1::2])

print(summ_[0]- summ_[7])

min_index = None
min_value = min(summ_)
for index, value in enumerate(summ_):
    if value == min_value:
        min_index = index
        break
print(min_value, min_index)
