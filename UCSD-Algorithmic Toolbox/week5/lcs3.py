#Uses python3

import sys

def lcs3(a, b, c):
    rows = len(a) + 1
    cols = len(b) + 1
    sets = len(c) + 1
    LCS = [[[0 for set in range(sets)] for col in range(cols)] for row in range(rows) ]

    for set in range(1,sets):
        for col in range(1,cols):
            for row in range(1,rows):
                if a[row-1] == b[col-1] and a[row-1] == c[set-1]:
                    LCS[row][col][set] = LCS[row-1][col-1][set-1] + 1
                else:
                    LCS[row][col][set] = \
                    max(LCS[row-1][col][set], LCS[row][col-1][set], LCS[row][col][set-1])
    return LCS[rows-1][cols-1][sets-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]

    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]

    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
