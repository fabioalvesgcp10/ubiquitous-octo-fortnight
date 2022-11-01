def fib(i):
    if i < 2:
        return i
    return fib(i-1)+fib(i-2)


if __name__ == "__main__":
    for i in range(0, 10):
        print(fib(i))