"""힙은 형태 속성 때문에 항상 완전 이진 트리입니다.
 그렇기 때문에 일반적으로 배열, 또는 파이썬 리스트를 써서 구현합니다."""

def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp

def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    if 0 < left_child_index < tree_size:
        largest = max(tree[index], tree[left_child_index])
        if largest == tree[left_child_index]:
            swap(tree, index, left_child_index)
            heapify(tree, left_child_index, tree_size)
        elif largest == tree[right_child_index]:
            swap(tree, index, right_child_index)
            heapify(tree, right_child_index, tree_size)

    if 0 < right_child_index < tree_size:
        largest = max(tree[index], tree[right_child_index])

        if largest == tree[left_child_index]:
            swap(tree, index, left_child_index)
            heapify(tree, left_child_index, tree_size)
        elif largest == tree[right_child_index]:
            swap(tree, index, right_child_index)
            heapify(tree, right_child_index, tree_size)

    # 코드잇 해답 내가 쓴게 더 이해잘되긴 함.
# def heapify(tree, index, tree_size):
#     """heapify 함수"""
#
#     # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
#     left_child_index = 2 * index
#     right_child_index = 2 * index + 1
#
#     # 코드를 쓰세요.
#     largest = index  # 일단 부모 노드의 값이 가장 크다고 설정
#
#     # 먼저 왼쪽 자식 노드의 값과 비교
#     # 0 < left_child_index <tree_size를 통해 먼저 왼쪽 자식 노드가 있는지 확인
#     # tree[largest] < tree[left_child_index]를 통해 왼쪼 자식 노드값이 부모 노드값보다 큰지 확인
#     # 왼쪽 자식 노드값이 더 크면 largest 변수에 왼쪽 자식 노드의 인덱스 저장
#     if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
#         largest = left_child_index
#
#     # 오른쪽 자식 노드의 값과 비교
#     if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
#         largest = right_child_index
#
#     if largest != index:  # 부모 노드의 값이 자식 노드의 값보다 작으면
#         swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꾼다.
#         heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를 개상으로 또 heapify 함수 호출한다.


# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree)