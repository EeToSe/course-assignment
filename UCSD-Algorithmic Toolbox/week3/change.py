# Uses python3
import sys

def get_change(m):
    #write your code here
    return int(m/10)+ int((m%10)/5)+ m%5

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
