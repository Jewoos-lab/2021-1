
#반복문이 1개 있기때문에 시간복잡도 O(n)

def select_stops(water_stops, capacity):
    # 코드를 작성하세요.

    KM = 0
    min_stops = []

    for i in range(len(water_stops)):
        if water_stops[i] - KM > capacity:
            min_stops.append(water_stops[i-1])
            KM = water_stops[i-1]
        else:
            continue

    min_stops.append(water_stops[-1])

    return min_stops


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))