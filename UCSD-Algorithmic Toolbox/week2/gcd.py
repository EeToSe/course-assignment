# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_efficent(a, b):
    current_gcd = 1
    # by default, a is larger
    while True:
        reminder = a % b
        a = b
        b = reminder
        if reminder == 0:
            break
    return a

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_efficent(a, b))
