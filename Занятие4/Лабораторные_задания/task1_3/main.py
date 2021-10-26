def func_(list_):
   return len([i for i in range(list_) if i % 2 == 0])

if __name__ == "__main__":
   list_ = 10
print(func_(list_))
