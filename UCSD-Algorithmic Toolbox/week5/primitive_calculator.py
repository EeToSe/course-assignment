# Uses python3
import sys

def greedy_calculate(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence(n):
    if n == 1:
        solutions = [[1]]
    if n == 2:
        solutions = [[1],[1,2]]

    solutions = [[1],[1,2],[1,3]]

    for i in range(3,n):
        number = i+1
        # caculate *2 case
        s2_solution = solutions[number//2-1][:]
        s2_solution.append(number//2*2)
        for i in range(number%2):
            s2_solution.append(number)

        # caculate *3 case
        s3_solution = solutions[number//3-1][:]
        s3_solution.append(number//3*3)
        if number % 3 == 1:
            s3_solution.append(number)
        if number % 3 == 2:
            s3_solution.append(number-1)
            s3_solution.append(number)

        if len(s2_solution) <= len(s3_solution):
            solutions.append(s2_solution)
        else:
            solutions.append(s3_solution)
    return solutions[n-1]


def dp_calculate(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 2]]
    if n == 3:
        return [[1], [1, 2], [1, 3]]
    solutions = [[1], [1, 2], [1, 3]]
    for i in range(3, n):
        number = i+1
        # important here! shallow copy
        # initial the solution with the operation - add 1
        solution = solutions[i - 1][:]

        if number % 2 == 0:
            solution1 = solutions[int(number/2) - 1][:]
            if len(solution1) < len(solution):
                solution = solution1

        if number % 3 == 0:
            solution2 = solutions[int(number/3) - 1][:]
            if len(solution2) < len(solution):
                solution = solution2

        solution += [number]
        solutions.append(solution)
    return solutions[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = dp_calculate(n)
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
