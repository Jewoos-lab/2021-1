def insertion_sort(list):
    for index in range(1, len(list)):
        for position in range(index, 0, -1):
            if list[position - 1] > list[position]:
                list[position], list[position - 1] = list[position - 1], list[position]
    return list

list = [4, 2, 7, 1, 9, 3]
print(insertion_sort(list))