# Uses python3
import sys
import itertools


def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def dp_partition3(A):
    sumA = sum(A)
    if sumA % 3 != 0:
        return 0
    n = len(A)
    # https://web.cs.ucdavis.edu/~amenta/w04/dis4.pdf
    # M[sumA//3][sumA//3]
    M = [[0 for _ in range(sumA//3+1)] for _ in range(sumA//3+1)]
    M[0][0] = 1
    # only need to fill the upper triangle
    for i in range(1, n+1):
        for x in range(sumA//3, -1, -1):
            for y in range(sumA//3, -1, -1):
                if x >= A[i-1]:
                    M[x][y] = M[x - A[i-1]][y] or M[x][y]
                if y >= A[i-1]:
                    M[x][y] = M[x][y - A[i - 1]] or M[x][y]
        # for row in M:
        #     print(*row)
        # print('\n')
    return M[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(dp_partition3(A))

