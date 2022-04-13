# Uses python3
#!/usr/bin/python3
from sys import stdin

class ItemValue:
    """Item Value DataClass"""
    def __init__(self, wt, val, ind):
        """Initial item information"""
        self.weight = wt
        self.value = val
        self.index = ind
        self.cost = val / wt

    def __lt__(self, other):
        return self.cost < other.cost

def get_optimal_value(capacity, weights, values):
    # satisfy the contraints
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(values)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in values)

    items_list = []
    for i in range(len(weights)):
        items_list.append(ItemValue(weights[i], values[i], i))
    # To remember, see the __lt__ method to tell python how to compare the list element
    items_list.sort(reverse = True)

    value = 0
    for i in items_list:
        if capacity >= i.weight:
            capacity -= i.weight
            value += i.value
        else:
            value += capacity*i.cost
            break
    return value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
