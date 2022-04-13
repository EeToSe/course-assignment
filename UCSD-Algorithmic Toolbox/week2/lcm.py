# Uses python3
import sys

def gcd_efficent(a, b):
    current_gcd = 1
    while True:
        reminder = a % b
        a = b
        b = reminder
        if reminder == 0:
            break
    return a

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b

def lcm_efficent(a, b):
    if(a==0 or b==0):
        return 0
    else:
        return int (a*b/gcd_efficent(a,b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_efficent(a, b))
