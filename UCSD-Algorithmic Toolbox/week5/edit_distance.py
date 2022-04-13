# Uses python3
# learn math from here: https://www.python-course.eu/levenshtein_distance.php
def edit_distance(s, t):
    #write your code here
    rows = len(s) + 1
    cols = len(t) + 1
    delete = insert = substitute = 1

    # create a matrix with the size of rows*cols
    distance_matrix = [[0 for col in range(cols)] for row in range(rows)]
    for col in range(cols):
        distance_matrix[0][col] = col
    for row in range(rows):
        distance_matrix[row][0] = row

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = substitute
            distance_matrix[row][col] = \
            min(distance_matrix[row-1][col]+insert,distance_matrix[row][col-1]+insert,distance_matrix[row-1][col-1]+cost)

    return distance_matrix[rows-1][cols-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
