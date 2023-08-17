#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = [0, 1]
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        count = 2
        while count < length:
            fib_list.append(fib_list[-1] + fib_list[-2])
            count = count + 1
        print(fib_list)

    

print_fibonacci(0)