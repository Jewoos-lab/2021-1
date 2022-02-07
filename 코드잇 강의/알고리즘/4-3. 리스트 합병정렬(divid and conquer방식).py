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

#합병 정렬
def merge_sort(my_list):
    #base case
    if len(my_list) < 2:
        return my_list

    # my_list를 반으로 쪼갠다
    mid = len(my_list) // 2
    left_list = my_list[:mid]
    right_list = my_list[mid:]

    #merge_sort 함수를 재귀적으로 호출하여 부분 문제 해결(conquer)하고,
    #합친다(combine)
    return merge(merge_sort(left_list), merge_sort(right_list))

print(list(set(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))