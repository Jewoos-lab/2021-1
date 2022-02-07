"""partition 함수를 작성하다 보면 코드가꽤나 지저분해질 수 있습니다.
특히 리스트에서 값들의 위치를 바꿔주는 경우가 많은데요.
코드가 지저분해지는 걸 방지하기 위해서 swap_elements라는 함수를 먼저 작성하겠습니다."""

def swap_elements(my_list, index1, index2):
    my_list[index2], my_list[index1] = my_list[index1], my_list[index2]

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    #먼저 파티션 함수에는 그룹(Small, Big, Unknown, Pivot)과 사용되는
    #변수들(start, b, i, p)을 생각할 것.
    #시작할때 항상 i,b는 같다.
    i = start
    b = start
    p = end

    #이제 반복문을 통해 pivot값을 기준으로 왼쪽(<pivot) 오른쪽(>pivot) 나누기
    while i < p:
        if my_list[i] >= my_list[p]:
            i += 1
        else:
            swap_elements(my_list, i, b)
            b += 1
            i += 1
    # 마지막으로 big그룹의 b와 pivot의 위치를 바꿔준다
    swap_elements(my_list, b, p)
    return b


list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)