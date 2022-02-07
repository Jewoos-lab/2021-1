#종이에 쓰니까 어느정도 이해o

def selection_sorting(list):

    for i in range(len(list) - 1):
        min_index = i
        for j in range(min_index, len(list)):
            if list[min_index] > list[j]:
                list[min_index], list[j] = list[j], list[min_index]

    return list

print(selection_sorting([1, 3, 5, 2, 9, 10]))