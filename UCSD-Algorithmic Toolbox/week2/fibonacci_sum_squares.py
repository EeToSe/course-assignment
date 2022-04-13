# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        tmp = current
        current = (previous + current) % 10
        previous = tmp
    return current

def fibonacci_sum_squares_efficient(n):
    # The last digits repeat every 60 numbers.
    mulitply = get_fibonacci_last_digit(n%60)*get_fibonacci_last_digit((n+1)%60)
    return( mulitply % 10)

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_efficient(n))
