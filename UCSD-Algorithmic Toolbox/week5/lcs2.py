#Uses python3

import sys


def lcs2(a, b):
    rows = len(a) + 1
    cols = len(b) + 1
    LCS = [[0 for col in range(cols)] for row in range(rows)]

    for col in range(1,cols):
        for row in range(1,rows):
            if a[row-1] == b[col-1]:
                LCS[row][col] = LCS[row-1][col-1] + 1
            else:
                LCS[row][col] = \
                max(LCS[row-1][col], LCS[row][col-1])
    return LCS[rows-1][cols-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    # map(function, iterator) which returns an iterator
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
