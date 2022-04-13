#!/usr/bin/python3

def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    # first make sure that one could make it to the distance
    stops.append(d)
    refills = 0
    left_fuel = m
    for stop in range(len(stops)):
        if stop == 0:
            distance = stops[0]
        else:
            distance = stops[stop] - stops[stop-1]

        if distance > left_fuel:
            return -1
        elif stop == len(stops) - 1:
            break
        else:
            left_fuel -= distance
            if left_fuel >= stops[stop+1] - stops[stop]:
                pass
            else:
                refills +=1
                left_fuel = m
    return refills

if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
