#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0, 1,]
    i = 1
    while len(fibonacci) < length:
        nextNum = fibonacci[i-1] + fibonacci[i]
        fibonacci.append(nextNum)
        i += 1
    if length == 0:
        fibonacci.clear()
    elif length == 1:
        del(fibonacci[1])
    print(fibonacci)

print_fibonacci(9)