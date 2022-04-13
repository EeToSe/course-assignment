# Uses python3
import sys

def fibonacci_sum_efficent(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        sum += current
        sum = sum % 10
    return sum

def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    next  = 1
    current = 0

    for i in range(to + 1):
        if i >= from_:
            sum += current
            sum %= 10
        current, next = next, (current + next) % 10

    return sum

def fibonacci_partial_sum_efficient(from_, to):
    from_sum = fibonacci_sum_efficent((from_-1)%60)
    to_sum =  fibonacci_sum_efficent(to%60)
    if to_sum < from_sum:
      return to_sum+10-from_sum
    else:
      return to_sum - from_sum

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_efficient(from_, to))
