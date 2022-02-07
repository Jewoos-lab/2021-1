# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    min = distance(coordinates[0], coordinates[1])
    min_pair = [coordinates[0], coordinates[1]]
    for i in coordinates:
        for j in coordinates:
            #store1, store2 = distance(i, j)
            lst = distance(i, j)
            #if distance(i, j) < min and distance(i, j) != 0:

            if distance(i, j) < min and distance(i, j) != 0:
                min = distance(i, j)
                min_pair = [i, j]
            #print(i, j, lst)

    return min_pair

# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))