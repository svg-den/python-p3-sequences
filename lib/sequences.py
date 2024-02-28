#!/usr/bin/env python3

# lib/sequences.py

def print_fibonacci(length):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < length:
        number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(number)

    print(fibonacci_sequence[:length])

pass
