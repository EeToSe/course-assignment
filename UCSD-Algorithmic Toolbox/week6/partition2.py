# Uses python3
import sys


def partition2(A):
    summation = sum(A)
    n = len(A)
    if summation % 2 != 0:
        return 0
    # 10/2 = 5.0 while 10//2 = 5
    dp = [[1 for _ in range(n+1)] for _ in range(summation//2 + 1)]
    for i in range(1, summation//2+1):
        dp[i][0] = 0
    for i in range(1, summation//2+1):
        for j in range(1, n+1):
            if i >= A[j-1]:
                dp[i][j] = dp[i - A[j-1]][j-1] or dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]


def partition_space(A):
    summation = sum(A)
    n = len(A)
    if summation % 2 != 0:
        return 0
    dp = [0 for _ in range(summation//2 + 1)]
    dp[0] = 1
    for j in range(1, n+1):
        for i in range(summation//2, 0, -1):
            if i >= A[j-1]:
                dp[i] = dp[i-A[j-1]] or dp[i]
    return dp[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition2(A))
    print(partition_space(A))
