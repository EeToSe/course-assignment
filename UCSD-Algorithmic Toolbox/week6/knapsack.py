# Uses python3
import sys
# all the items have the same value per unit of weight

def greedy_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def dp_weight(W, w) -> object:
    n = len(w)
    # K[i][w] 前i件物品放入一个容量为w的可以获得的最大重量
    K = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(1, n + 1):
        for weight in range(1, W+1):
            if w[i-1] <= weight:
                K[i][weight] = max(K[i-1][weight], K[i-1][weight-w[i-1]] + w[i-1])
            else:
                K[i][weight] = K[i-1][weight]

    for i in K:
        print(i)
    return K[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(dp_weight(W, w))