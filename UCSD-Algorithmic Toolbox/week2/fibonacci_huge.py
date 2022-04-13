# Uses python3
import sys

def fibonacci(n):
    if n <= 1:
        return n
    previous, current = 0,1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current

# a given m ranges from 3 to m * m
def calc_pisano(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

def get_fibonacci_huge_naive(n, m):
    return fibonacci(n) % m

def get_fibonacci_huge_efficent(n, m):
    reminder = n % calc_pisano(m)
    return fibonacci(reminder) % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    #print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_efficent(n, m))
