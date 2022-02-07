#리스트 합병은 반드시 정렬된 상태로 합병할 것.

def merge(list1, list2):
    i = 0
    j = 0
    merged_list = []

    #보시다시피 두 리스트 중 하나만 소진되어도 while문은 종료됩니다.
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1
    #소진되지 않은 리스트가 무엇인지 판별하고 남은 항목을 추가시켜라

    if i == len(list1):
        merged_list += list2[j:]
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list

print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))