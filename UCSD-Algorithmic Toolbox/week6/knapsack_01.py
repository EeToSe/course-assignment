# Uses python3
import sys
# items have the different value per unit of weight


def greedy_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def dp_weight(W, w, v) -> object:
    n = len(w)
    # K[i][w] 前i件物品放入一个容量为w的可以获得的最大重量
    K = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(1, n + 1):
        for weight in range(1, W+1):
            if w[i-1] <= weight:
                K[i][weight] = max(K[i-1][weight], K[i-1][weight-w[i-1]] + v[i-1])
            else:
                K[i][weight] = K[i-1][weight]

    # print 2D result
    # for i in K:
    #     print(*i)
    return K[-1][-1]


def optimize_space(W, w, v):
    # 一维滚动数组
    n = len(w)
    # For i in range(1, n+1), each iteration calculate K[weight] == K[i][weight] as calculated in dp_weight
    K = [0 for i in range(W+1)]
    for i in range(1, n+1):
        for weight in range(W, 0, -1):
            # counting the weight backwards, so we store the computation when taking i-1 items
            if w[i-1] <= weight:
                K[weight] = max(K[weight], K[weight-w[i-1]]+v[i-1])
    return K[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # input sample
    

    # W = data[0]
    # N = data[1]
    # data = data[2:]
    # w = data[:N]
    # data = data[N:]
    # v = data[:N]
    # another input sample from https://blog.csdn.net/qq_41688840/article/details/114242296
    N = data[0]
    W = data[1]
    data = data[2:]
    w = data[0::2]
    v = data[1::2]
    print(optimize_space(W, w, v))