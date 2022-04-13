# Uses python3
import sys


def get_change(m):
    # Dynamic Programming
    change = [2, 4, 8]
    coin = [0] * (m + 1)
    coin[0] = 0
    for i in range(1, m + 1):
        current = []
        for j in change:
            if i - j >= 0:
                current.append(coin[i - j] + 1)
        coin[i] = min(current)
    return coin[m]


def recursive_change(m):
    # Recursive method
    # initial condition / stop criteria
    if m == 0:
        return 0
    MinNumCoins = m
    change = [2, 4, 8]
    for i in change:
        if m >= i:
            NumCoins = recursive_change(m - i)
            if NumCoins + 1 < MinNumCoins:
                MinNumCoins = NumCoins + 1
    return MinNumCoins

def dp_change(m):
    # Dynamic Programming
    # start from 0
    MinNumCoins = [0] * (m+1)
    change = [1, 3, 4]
    for money in range(1, len(MinNumCoins)):
        MinNumCoins[money] = m
        for coin in change:
            if money >= coin:
                NumCoins = MinNumCoins[money-coin] + 1
                if NumCoins < MinNumCoins[money]:
                    MinNumCoins[money] = NumCoins
    return MinNumCoins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(f'dp result {dp_change(m)}')
    # print(f'recursive result {get_change(m)}')
