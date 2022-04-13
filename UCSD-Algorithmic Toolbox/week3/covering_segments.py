# Uses python3
import sys
from collections import namedtuple

class PointsValue:
    """ Points Item which contain start and end """
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self,other):
        return self.end < other.end

def optimal_points(starts,ends):
    segments = []
    for i in range(len(starts)):
        segments.append(PointsValue(starts[i], ends[i]))
    # To remember, see the __lt__ method to tell python how to compare the list element
    segments.sort()

    points = []
    earliest_end = segments[0].end
    points.append(earliest_end)
    for s in segments:
        if s.start > earliest_end:
            earliest_end = s.end
            points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    starts = data[::2]
    ends = data[1::2]
    points = optimal_points(starts,ends)
    print(len(points))
    print(*points)
