# Uses python3
import sys

def optimal_summands(n):
    assert(1<=n<=10**9 )
    summands = []
    left_prizes = n
    current_prizes = 1
    #write your code here
    for _ in range(n):
        if(left_prizes>=current_prizes):
            summands.append(current_prizes)
            left_prizes -= current_prizes
            current_prizes += 1
        else:
            summands[-1] += left_prizes
            break
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
