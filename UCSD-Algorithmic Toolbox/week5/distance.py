# Uses python3
def edit_distance(t, s):
    rows = len(t) + 1
    cols = len(s) + 1
    dist = [[0 for col in range(cols)] for row in range(rows)]
    # initialize the distance matrix
    for row in range(1, rows):
        dist[row][0] = row

    for col in range(1, cols):
        dist[0][col] = col

    for row in range(1, rows):
        for col in range(1, cols):
            substitution = 0
            if t[row-1] != s[col-1]:
                substitution = 1
            dist[row][col] = min(dist[row - 1][col] + 1, dist[row][col - 1] + 1, dist[row - 1][col - 1] + substitution)
    for row in range(rows):
        print(dist[row])
    return dist


if __name__ == "__main__":
    print(edit_distance(input(), input()))
