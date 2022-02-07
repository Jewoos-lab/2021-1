def min_fee(pages_to_print):
    sorted_list = sorted(pages_to_print)

    total_fee = 0

    for i in range(len(sorted_list)):
        total_fee = total_fee + sorted_list[i] * (len(sorted_list) - i)

    return total_fee


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))